import json
import requests
from datetime import datetime

def callApiGET(URL, retry = "3600"):
    print(f'---- START CALL URL {URL}?limit=100 AND RETRY {retry}\n')
    return requests.get(URL+'?limit=100', {"headers": { "Retry-After": retry }})

def processingDatas(arr):
    res = []
    print("=== START ====")
    for data in arr:
        print(f'\n{data}')
    
    return res


def openFileJson(fileName):
    file = open(f'mocks/reddit/{fileName}.json')
    return json.loads(file.buffer.read())

import datetime 
  
  

def convertTimeStampToDate(timestamp):
    return datetime.fromtimestamp(int(timestamp))
