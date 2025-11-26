from bs4 import BeautifulSoup as bs
import requests

# step3. 입력받은 query가 포함된 url 주소(네이버 뉴스 검색 결과 페이지) 저장
url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='


def select_news(keyword):
    search_url = url +'%s'%keyword
    soup = get_html(search_url)
    
    new_titles = soup.select("span.sds-comps-text.sds-comps-text-ellipsis.sds-comps-text-ellipsis-1.sds-comps-text-type-headline1")  # step6. CSS 선택자로 뉴스 제목 가져오기
    # 적용할 때 "sds-comps-text.sds-comps-text-ellipsis.sds-comps-text-ellipsis-1.sds-comps-text-type-headline1"
    # 실제 "sds-comps-text sds-comps-text-ellipsis sds-comps-text-ellipsis-1 sds-comps-text-type-headline1"
    for i in new_titles:
        title = i.get_text()
        print(title)


def get_html(url):
    # step4. requests 패키지를 이용해 'url'의 html 문서 가져오기
    response = requests.get(url)
    html_text = response.text
    
    # step5. beautifulsoup 패키지로 파싱 후, 'soup' 변수에 저장
    return bs(response.text, 'html.parser')

if __name__ == '__main__':
    # step2. 검색할 키워드 입력
    select_news('추석')