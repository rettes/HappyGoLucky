import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/contact_trace', methods=['POST'])
def evaluateTrace():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    
    infect = data.get("infected").get("name")
    ori = data.get("origin").get("name")
    clus = data.get("cluster")[0]["name"]

    infected = data.get("infected").get("genome")
    origin = data.get("origin").get("genome")
    cluster = data.get("cluster")[0]["genome"]

    arr = infected.split('-')
    arr2 = origin.split('-')
    arr3 = cluster.split('-')

    nonsilent1 = False
    nonsilent2 = False
    count1 = 0
    count2 = 0
    
    for i in range(len(arr)):
        if(arr[i] != arr2[i]):
            count1 += 1
            if(arr[i][0] != arr2[i][0]):
                nonsilent1 = True
        if(arr[i] != arr3[i]):
            count2 += 1
            if(arr[i][0] != arr3[i][0]):
                nonsilent1 = True

    for i in range(len(arr)):
         if(arr2[i] != arr3[i]):
            if(arr2[i][0] != arr3[i][0]):
                nonsilent2 = True
        
    result = []
    if(nonsilent1):
        infect += "*"
    if(nonsilent2):
        ori += "*"
    if(count1 == count2):
        result.append(infect + " -> " + ori)
        result.append(infect + " -> " + clus)
    elif(count1 >= count2):
        result.append(infect + " -> " + clus + " -> " + ori)
    else: 
        result.append(infect + " -> " + ori + " -> " + clus)

    return json.dumps(result)


