import sys
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote

TARGET_URL_BEFORE_PAGE_NUM = "http://news.donga.com/search?p="
TARGET_URL_BEFORE_KEWORD = '&query='
TARGET_URL_REST = '&check_news=1&more=1&sorting=3&search_date=1&v1=&v2=&range=3'

#기사 본문 내용 가져오기
def get_link_from_news_title(page_num, URL, output_file):
    for i in range(page_num):
        current_page_num=1+i*15
        position = URL.index('=')
        URL_with_page_num = URL[:position+1] + str(current_page_num)+ URL[position+1 :]
        print("URL_with_page_num", URL_with_page_num)
        source_code_from_URL = urlib.request.urlopen(URL_with_page_num)
        soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
        for title in soup.find_all('p', 'tit'):
            title_link = title.select('a')
            article_URL = title_link[0]['href']
            get_text(article_URL, output_file)
# 메인함수
def main(argv) :
    if len(argv)!=4:
        print("python [Module Name][Keyword][Take page number][Result file]")
        return
    keyword =argv[1]
    page_num = int(argv[2])
    output_file_name = argv[3]
    target_URL = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_KEWORD + quote(keyword) + TARGET_URL_REST
    output_file = open(output_file_name, 'w')
    get_link_from_news_title(page_num, target_URL, output_file)
    output_file.close()
    if __name__ == '__main__':
        main(sys.argv)
