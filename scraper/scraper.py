from bs4 import BeautifulSoup
import requests
import json

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
        print(user)
        information = {}

        if name not in final_data.keys():
            final_data[name] = []

        soup = BeautifulSoup(requests.get("https://jojowiki.com" + stand).text, "lxml")
        user_soup = BeautifulSoup(requests.get("https://jojowiki.com" + user).text, "lxml")

        # User elements
        user_name_div = user_soup.find('h2', attrs={'data-source': "title"})
        gender_div = user_soup.find('div', attrs={'data-source': "gender"})
        hair_color_div = user_soup.find('div', attrs={'data-source': "hair"})
        eye_color_div = user_soup.find('div', attrs={'data-source': "eyes"})

        user_image_holder = user_soup.find("div", {"class": "pi-item pi-data pi-item-spacing pi-border-color"})

        if not user_image_holder:
            continue

        user_parts_div = user_image_holder.find_all('div', attrs={'title': "Anime", "class": "tabbertab"})

        # Stand elements
        type_div = soup.find('div', attrs={'data-source': "type"})
        stand_name_div = soup.find('h2', attrs={'data-source': "title"})
        
        if not type_div:
            continue

        stand_image_holder = soup.find("div", {"class": "pi-item pi-data pi-item-spacing pi-border-color"})
        stand_parts_div = stand_image_holder.find_all('div', attrs={'title': "Anime", "class": "tabbertab"})


        stand_images = []
        user_images = []

        for part_image in stand_parts_div:
            image_element = part_image.find('a', attrs={'class': "image"})

            if image_element:
                for image in image_element.children:
                    stand_images.append(image["src"])
            else:
                image_element = stand_parts_div[0].find('a', attrs={'class': "image"})
                for image in image_element.children:
                    stand_images.append(image["src"])

        for user_part_image in user_parts_div:
            user_image_element = user_part_image.find("a", attrs={"class": "image"})

            if user_image_element:
                for user_image in user_image_element.children:
                    user_images.append(user_image["src"])
            else:
                user_image_element = user_parts_div[0].find('a', attrs={'class': "image"})
                for user_image in user_image_element.children:
                    user_images.append(user_image["src"])

        type_element = type_div.contents[3].find_all("a")
        type_names = [type.contents[0] for type in type_element]
        stand_name = stand_name_div.text
        user_name = user_name_div.text if user_name_div else "Unknown"
        user_gender = gender_div.find("div").text.replace(" ", "") if gender_div else "Unknown"
        eye_color = eye_color_div.find("div").contents[0] if eye_color_div else "Unknown"
        hair_color = hair_color_div.find("div").contents[0] if hair_color_div else "Unknown"

        information["type"] = type_names
        information["stand"] = stand_name
        information["stand_images"] = stand_images
        information["user"] = user_name
        information["gender"] = user_gender
        information["hair_color"] = hair_color
        information["eye_color"] = eye_color
        information["user_images"] = user_images

        final_data[name].append(information)

    return final_data

