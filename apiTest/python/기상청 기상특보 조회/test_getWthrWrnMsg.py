import requests
import sys

import setting

url_endpoint = "http://apis.data.go.kr/1360000/WthrWrnInfoService"
url_spec = "getWthrWrnMsg" # 기상특보통보문조회
url = url_endpoint + "/" + url_spec

search_date = "20220801" # 조회하려는 날짜
params = {
    "serviceKey": setting.api_key_decode,
    "dataType": "json",
    "stnId": 108,
    "fromTmFc": search_date,
    "toTmFc": search_date
}

response = requests.get(url, params=params)
print(response)
print(response.status_code)

sys.stdout = open('test_getWthrWrnMsg_data.json', 'w',encoding="UTF-8")
print(response.text)
sys.stdout.close()