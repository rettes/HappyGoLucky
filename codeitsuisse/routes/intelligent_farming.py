import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/intelligent-farming', methods=['POST'])
def evaluateFarm():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    givenString = data.get("id")
    totalPoints = 0
    outputString = ""
    dict1 = {}
    for i in range(0,len(givenString)):
        if(givenString[i] not in dict1):
            dict1[givenString[i]] = 1
        else:
            dict1[givenString[i]] = dict1[givenString[i]] + 1
    numberA = 0
    numberG = 0
    numberC = 0
    numberT = 0
    if("a" in dict1):
        numberA = dict1['a']
    if("g" in dict1):
        numberA = dict1['g']
    if("c" in dict1):
        numberA = dict1['c']
    if("t" in dict1):
        numberA = dict1['t']
    
    if(numberA >= numberG):
        for i in range(numberA):
            outputString += "aag"
            numberA -= 2
            numberG -= 1
   
        

    return json.dumps(result)


