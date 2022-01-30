import requests
from bs4 import BeautifulSoup


def check_for_datasource(link, data_source):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")

    response_div = soup.find('h2', attrs={'data-source': data_source})

    print(response_div.contents[0])


check_for_datasource("https://jojowiki.com/Star_Platinum", "title")
