import requests
import sys
import xmltodict
import json

import setting

url_endpoint = "http://apis.data.go.kr/B090041/openapi/service/RiseSetInfoService"
url_spec = "getAreaRiseSetInfo" # 초미세먼지 주간예보 조회
url = url_endpoint + "/" + url_spec

search_date = "20220801" # 조회하려는 날짜
params = {
    "serviceKey": setting.api_key_decode,
    "locdate": search_date,
    "location": "서울",

}

response = requests.get(url, params=params)
print(response)
print(response.status_code)

sys.stdout = open('test_getAreaRiseSetInfo_data.json', 'w',encoding="UTF-8")
xml_dict = xmltodict.parse(response.text)
json_object = json.dumps(xml_dict)
print(json_object) 
sys.stdout.close()