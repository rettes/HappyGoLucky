import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/olympiad-of-babylon', methods=['POST'])
def evaluateOly():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    
    books = data.get("books")
    days = data.get("days")
    list.sort(days)
    numberOfBooks = 0
    count = len(days) -1
    while(count > -1):
        remainder = days[count]
        for i in range(len(books)):
            if(remainder <= 0):
                break
            if(remainder >= books[i] and books[i] != 0):
                remainder -= books[i]
                numberOfBooks += 1
                books[i] = 0
                
        count -= 1

    resultDict = {"optimalNumberOfBooks" : numberOfBooks}

    return json.dumps(resultDict)





