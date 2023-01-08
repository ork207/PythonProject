import requests
from bs4 import BeautifulSoup
import csv

HEADERS = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }


def get_data(url):
    response = requests.get(url=url, headers=HEADERS)
    # print(response)

    with open(file='index.html', mode='w') as file:
        file.write(response.text)

    with open(file='index.html', ) as file:
        src = file.read()

    soup = BeautifulSoup(src, 'html.parser')
    table = soup.find('table', id='holdings')

    data_th = table.find('thead').find_all('tr')[-1].find_all('th')

    table_headers = []
    for dth in data_th:
        dth = dth.text.strip()
        # print(dth)
        table_headers.append(dth)

    with open(file='data.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                table_headers
            )
        )

    tbody_trs = table.find('tbody').find_all('tr')

    table_area = []
    for tr in tbody_trs:
        table_area.append(tr)

        table_body = []
        td_a = tr.find_all('td')
        for table in td_a:
            table = table.text.strip()
            table_body.append(table)










    with open(file='data.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow(
        (
             table_body
         )
     )

    return 'Work done!'
def main():
    print(get_data(url='https://www.proshares.com/our-etfs/strategic/nobl'))


if __name__ == '__main__':
    main()