import requests
import sys

import setting

url_endpoint = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc"
url_spec = "getCtprvnRltmMesureDnsty" # 초미세먼지 주간예보 조회
url = url_endpoint + "/" + url_spec
local_list = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주', '세종']

for local in local_list:
    params = {
        "serviceKey": setting.api_key_decode,
        "returnType": "json",
        "sidoName": local,
        "numOfRows": 100,
        "ver": "1.3",

    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        print(response.json()['response']['body']['numOfRows'])
        for item in response.json()['response']['body']['items']:
            시도명 = item['sidoName']
            측정소명 = item['stationName']
            미세먼지_등급자료_1시간내 = item['pm10Grade1h']
            초미세먼지_등급자료_1시간내 = item['pm25Grade1h']
            print(시도명, 측정소명, 미세먼지_등급자료_1시간내, 초미세먼지_등급자료_1시간내)

