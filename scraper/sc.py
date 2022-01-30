from selenium import webdriver
import time
import pprint
import json

pp = pprint.PrettyPrinter(indent=4)
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


def get_links():
    """
    DIO, JOESTAR STAND(DIO), ANUBIS

    RATT, KING CRIMSON

    DA 2 MENOS PORQUE EL USUARIO ES EL MISMO PERO EL STAND ES DIFERENTE

    """
    all_links = []
    for x in range(3):
        driver.get("https://jojowiki.com/List_of_Stands")
        for i in range(35):
            both = []
            try:
                standLink = driver.find_elements_by_xpath(f'//*[@id="tabber-7b41f183054568e35f06bd9e4c65aa1d"]/div[{x+1}]/div[1]/div/div[2]/div[{i+1}]/div[2]/a')
                userLink = driver.find_elements_by_xpath(f'//*[@id="tabber-7b41f183054568e35f06bd9e4c65aa1d"]/div[{x+1}]/div[1]/div/div[2]/div[{i+1}]/div[2]/div/a')
                both.append(standLink[0].get_attribute('href'))
                both.append(userLink[0].get_attribute('href'))

                all_links.append(both)
            except Exception as e:
                both.append('fail')

    return all_links


def get_all_data(sub_list: list, final_list):

    information = {}

    for num, link in enumerate(sub_list):
        driver.get(link)
        time.sleep(1)
        if num == 1:
            try:
                search = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[2]/aside')
                result = list(search.text.split("\n"))
            except Exception as e:
                search = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/aside')
                result = list(search.text.split("\n"))
            finally:
                image = driver.find_element_by_xpath('//*[@class="tabber tabberlive"]/div[2]/p/a/img').get_attribute('src')
                information['user_image'] = image
                for n, data in enumerate(result):
                    if n == 0:
                        information['user'] = data

                    if data.lower() in ['stand', 'gender']:
                        information[data] = result[n + 1]

                    elif data.lower() in ['hair color', 'eye color']:
                        for i in range(3):
                            i = i + 1
                            if 'Anime' in result[n + i]:
                                information[data] = result[n + i]
                                break
                            else:
                                information[data] = result[n + 1]
        if num == 0:
            try:
                search = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/aside')
                result = list(search.text.split("\n"))
            except Exception as e:
                try:
                    search = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/aside[1]')
                    result = list(search.text.split("\n"))
                except Exception:
                    result = [None]
            finally:
                image = driver.find_element_by_xpath('//*[@class="tabber tabberlive"]/div[2]/p/a/img').get_attribute('src')
                information['stand_image'] = image
                for n, data in enumerate(result):
                    if isinstance(data, str):
                        if data.lower() == 'stand type':
                            stands = []
                            var = 1
                            while True:
                                if result[n + var].lower() == 'manga debut':
                                    break
                                else:
                                    stands.append(result[n + var])
                                    var = var + 1
                            information['stand_type'] = stands
                    if data is None:
                        information['stand_type'] = 'None'

    final_list.append(information)


def main():
    final_list = []
    lista = get_links()

    for sub_list in lista:
        time.sleep(0.5)
        get_all_data(sub_list, final_list)

    with open("test.json", "w") as file:
        json.dump(final_list, file, indent = 4)
        print('DONE')


main()
