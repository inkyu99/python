from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

def hollys_store(result):
    for page in range(1,50):
        Hollys_url = 'https://www.hollys.co.kr/store/korea/korStore.do?pageNo=%d&sido=&gugun=&store=' %page
        print(Hollys_url)
        html = urllib.request.urlopen(Hollys_url)
        soupHollys = BeautifulSoup(html, 'html.parser')
        tag_tbody = soupHollys.find('tbody')
        for store in tag_tbody.find_all('tr'):
            if len(store) <= 3:
                break
            store_td = store.find_all('td')
            store_name = store_td[1].string
            store_sido = store_td[0].string
            store_address = store_td[3].string
            store_phone = store_td[5].string
            result.append([store_name]+[store_sido]+[store_address]
                          +[store_phone])
        return

    def main():
        result = []
        print('Holly store crawling >>>>>>>>>>>>>>>>>>>>>>>')
        hollys_store(result)
        holly_tbl = pd.DataFrame(result, columns=('store', 'sido-gu', 'address', 'phone'))
        holly_tbl.to_csv('./hollys.csv', encoding='cp949', mode='w', index=True)
        del result[:]

    if __name__ == '__main__':
        main()