import requests
import sys

import setting

url_endpoint = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc"
url_spec = "getCtprvnRltmMesureDnsty" # 초미세먼지 주간예보 조회
url = url_endpoint + "/" + url_spec

search_date = "2022-08-01" # 조회하려는 날짜
params = {
    "serviceKey": setting.api_key_decode,
    "returnType": "json",
    "sidoName": "서울",
    "ver": "1.1",

}

response = requests.get(url, params=params)
print(response)
print(response.status_code)

sys.stdout = open('test_getCtprvnRltmMesureDnsty_data.json', 'w',encoding="UTF-8")
print(response.text)
sys.stdout.close()