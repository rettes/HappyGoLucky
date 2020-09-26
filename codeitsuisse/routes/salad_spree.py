import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/salad-spree', methods=['POST'])
def evaluateSalad():
    #street_map = [["X", "X", "2"], ["2", "3", "X"], ["X", "3", "2"]]
    # street_map = [["2", "3", "X", "2"], ["4", "X", "X", "4"], ["3", "2", "X", "X"], ["X", "X", "X", "5"]]
    # num_salads = n
    # salad_prices_street_map = street_map
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    n = data.get("number_of_salads")
    street_map = data.get("salad_prices_street_map")
    # CODE START
    minimum = float("inf")
    for street in street_map:
        if len(street) < n:
            continue
        open_stores = []
        for i, store in enumerate(street):
            if store == "X":
                while len(open_stores) > n:
                    first = open_stores[0]
                    last = open_stores[-1]
                    if first > last:
                        del open_stores[0]
                    else:
                        del open_stores[-1]
                if sum(open_stores) < minimum and len(open_stores) == n:
                    minimum = sum(open_stores)
                open_stores = []
            else:
                open_stores.append(int(store))
            if len(open_stores) < n:
                continue
        while len(open_stores) > n:
            first = open_stores[0]
            last = open_stores[-1]
            if first > last:
                del open_stores[0]
            else:
                    del open_stores[-1]
            if sum(open_stores) < minimum and len(open_stores) == n:
                minimum = sum(open_stores)    
    result_dict = {}
    if minimum != float("inf"):
        result_dict["result"] = minimum
    else:
        result_dict["result"] = 0
    return json.dumps(result_dict)
    #print(jsonify(result_dict))



