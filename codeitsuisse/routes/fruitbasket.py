import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/fruitbasket', methods=['POST'])
def evaluateFruit():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    numberOfApple = data.get("maApple")
    numberOfWatermelon = data.get("maWatermelon")
    numberOfBanana = data.get("maBanana")
    result = (numberOfApple * 5)  + (numberOfWatermelon * 30) + (numberOfBanana * 10) 
    return json.dumps(result)


