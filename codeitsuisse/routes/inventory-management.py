import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/inventory-management', methods=['POST'])
def evaluate2():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("input")
    print(inputValue)
    logging.info("My result :{}".format(result))
    return json.dumps(result);


