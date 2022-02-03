import requests
from bs4 import BeautifulSoup


def check_for_datasource(link, data_source):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")

    response_div = soup.find('h2', attrs={'data-source': data_source})

    print(response_div.contents[0])


# check_for_datasource("https://jojowiki.com/Star_Platinum", "title")


def check_for_image(link):
    link = "https://jojowiki.com/Magician%27s_Red"
    # link = "https://jojowiki.com/Star_Platinum"
    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")

    img = []
    response_div = soup.find_all('div', attrs={'title': "Anime", "class": "tabbertab"})

    for each in response_div:
        new = each.find('a', attrs={'class': "image"})

        if new:
            for x in new.children:
                img.append(x["src"])
        else:
            new = response_div[0].find('a', attrs={'class': "image"})
            for x in new.children:
                print(x["src"])


check_for_image("https://jojowiki.com/Magician%27s_Red")
