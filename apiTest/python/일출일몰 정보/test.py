import requests
import sys
from datetime import datetime
import xmltodict
import json

import setting

url = "http://apis.data.go.kr/B090041/openapi/service/RiseSetInfoService/getLCRiseSetInfo"

search_date = datetime.today().strftime("%Y%m%d")

params = {
    "serviceKey": setting.api_key_decode,
    "locdate": search_date,
    "longitude": 128.20000,
    "latitude": 37.1500,
    "dnYn": "y",

}

response_xml = requests.get(url, params=params)

if response_xml.status_code == 200:
    xml_dict = xmltodict.parse(response_xml.text)
    response_str = json.dumps(xml_dict)
    response_json = json.loads(response_str)

    sunrise = response_json['response']['body']['items']['item']['sunrise']
    sunset = response_json['response']['body']['items']['item']['sunset']
    print(sunrise, sunset)
