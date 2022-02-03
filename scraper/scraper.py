from bs4 import BeautifulSoup
import requests


def get_links():

    link = "https://jojowiki.com/List_of_Stands"
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "lxml")

    seasons = soup.find_all("div", {"class": "diamond2"})

    seasons_names = [name["title"] for name in soup.find_all('div', {"class": "tabbertab"})[0: 4]]
    list_of_links = []

    for index, season, in enumerate(seasons[0:4]):
        characters = season.find_all("div", {"class": "charbox diamond resizeImg"})
        for character in characters:

            list_of_links.append(seasons_names[index])

            character_stand = character.find("div", {"class": "charname"})
            character_name = character.find("div", {"class": "charstand"})

            for stand_link in character_stand:
                list_of_links.append(stand_link["href"])

            for user_link in character_name:
                try:
                    list_of_links.append(user_link["href"])
                except KeyError:
                    inside_element = user_link.find("a")
                    list_of_links.append(inside_element["href"])

    return list_of_links[:-1]


def get_attributes(links_list):
    final_data = {}

    for name, user, stand in zip(links_list[::3], links_list[2::3], links_list[1::3]):
        information = {}

        if name not in final_data.keys():
            final_data[name] = []

        soup = BeautifulSoup(requests.get("https://jojowiki.com" + stand).text, "lxml")
        user_soup = BeautifulSoup(requests.get("https://jojowiki.com" + "/Jotaro_Kujo").text, "lxml")

        # User elements

        user_name_div = user_soup.find('h2', attrs={'data-source': "title"})
        gender_div = user_soup.find('div', attrs={'data-source': "gender"})

        # TODO: this

        hair_color_div = user_soup.find('div', attrs={'data-source': "hair"})
        eye_color_div = user_soup.find('div', attrs={'data-source': "eyes"})

        eye_color_div.find("div").contents
        hair_color_div.find("div").text

        # Stand elements

        type_div = soup.find('div', attrs={'data-source': "type"})
        stand_name_div = soup.find('h2', attrs={'data-source': "title"})
        parts_div = soup.find_all('div', attrs={'title': "Anime", "class": "tabbertab"})

        if not type_div:
            continue

        stand_images = []

        for part_image in parts_div:
            image_element = part_image.find('a', attrs={'class': "image"})

            if image_element:
                for image in image_element:
                    stand_images.append(image["src"])
            else:
                image_element = parts_div[0].find('a', attrs={'class': "image"})
                for image in image_element:
                    stand_images.append(image["src"])

        type_element = type_div.contents[3].find_all("a")
        type_names = [type.contents[0] for type in type_element]
        stand_name = stand_name_div.text
        user_name = user_name_div.text
        user_gender = gender_div.find("div").text.replace(" ", "")

        information["type"] = type_names
        information["stand"] = stand_name
        information["stand_images"] = stand_images
        information["user"] = user_name
        information["gender"] = user_gender

        final_data[name].append(information)

    print(final_data)


get_attributes(get_links())
