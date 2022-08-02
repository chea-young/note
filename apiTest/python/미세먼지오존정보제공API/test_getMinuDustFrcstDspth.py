import requests
import sys

import setting

# 대기질 예보통보 조회
url_endpoint = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc"
url_spec = "getMinuDustFrcstDspth" # 대기질 예보통보 조회
url = url_endpoint + "/" + url_spec

search_date = "2022-08-01" # 조회하려는 날짜
params = {
    "serviceKey": setting.api_key_decode,
    "returnType": "json",
    "searchDate": search_date,

}

response = requests.get(url, params=params)
print(response)
print(response.status_code)

sys.stdout = open('test_getMinuDustFrcstDspth_data.json', 'w',encoding="UTF-8")
print(response.text)
sys.stdout.close()