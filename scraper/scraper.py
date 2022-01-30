from bs4 import BeautifulSoup
import requests

link = "https://jojowiki.com/List_of_Stands"
response = requests.get(link)
soup = BeautifulSoup(response.content, "html.parser")

seasons_names = [name["title"] for name in soup.find_all('div', {"class": "tabbertab"})[0: 5]]
seasons = soup.find_all("div", {"class": "diamond2"})


for season in seasons[0:5]:
    characters = season.find_all("div", {"class": "charbox diamond resizeImg"})
    for character in characters:
        character_stand = character.find("div", {"class": "charname"})
        character_name = character.find("div", {"class": "charstand"})

        for stand_link in character_stand:
            print(stand_link["href"])
            try:
                soup = BeautifulSoup(requests.get("https://jojowiki.com" + stand_link["href"]).content, "html.parser")

                type_div = soup.find('div', attrs={'data-source': "type"})
                name_div = soup.find('h2', attrs={'data-source': "title"})

                if not type_div:
                    continue

                # This is goes in the final dictionary

                type_names = type_div.contents[3].find_all("a")
                stand_name = name_div.contents[0]

            except KeyError:
                i_element = stand_link.find("a")
                soup = BeautifulSoup(requests.get("https://jojowiki.com/" + i_element["href"]).content, "html.parser")
                type_div = soup.find('div', attrs={'data-source': "type"})
                type_names = type_div.contents[3].find_all("a")

        # for name_link in character_name:
        #     try:
        #         print(stand_link["href"])
        #     except KeyError:
        #         print(f"{stand_link} inside keyerror stand")
