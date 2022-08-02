import requests

import setting

# 대기질 예보통보 조회
url_endpoint = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc"
url_spec = "getMsrstnAcctoRltmMesureDnsty" # 측정소별 실시간 측정정보 조회
url = url_endpoint + "/" + url_spec

search_date = "2022-07-30" # 조회하려는 날짜
params = {
    "serviceKey": setting.api_key_decode,
    "returnType": "json",
    "stationName": "종로구",
    "dataTerm": "DAILY",
    "ver": "1.1"
}

response = requests.get(url, params=params)
print(response)
print(response.status_code)
print(response.text)