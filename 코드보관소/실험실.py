import requests
from bs4 import BeautifulSoup

def get_the_page_by_beautifulsoup():
    page = requests.get("https://www.naver.com")
    soup = BeautifulSoup(page.content,'html.parser')
    print(soup.find_all('p')[0].get_text())
    print(soup.find_all('p')[1].get_text())
    print(soup.find_all('p')[2].get_text())
    print(soup.find_all('p')[3].get_text())

if __name__ =="__main__":
    get_the_page_by_beautifulsoup()