from bs4 import BeautifulSoup
import requests
import urllib.parse


# Spanish path
def spanish(query):
    # will webscrape from spanishdict
    r = requests.get(
        'https://www.spanishdict.com/translate/' + query)
    soup = BeautifulSoup(r.text, 'lxml')
    definition = soup.find_all('div', class_='CMxOwuaP _1v-p9pvd')
    pronounciation = soup.find('span', class_='_3xGlaCmF').text

    print(query)
    print(pronounciation)
    for item in definition:
        print(item.text)


# Chinese path
def mandarin(query):
    # will webscrape from mdbg
    r = requests.get(
        'https://www.mdbg.net/chinese/dictionary?page=worddict&wdrst=1&wdqb=' + urlencoded)
    soup = BeautifulSoup(r.text, 'lxml')
    chinese = soup.find_all('div', class_='hanzi')
    pinyin = soup.find_all('div', class_='pinyin')
    english = soup.find_all('div', class_='defs')

    new_chinese_list = []
    for item in chinese:
        if query in item.text:
            new_chinese_list.append(item.text)
    for i in range(len(new_chinese_list)):
        print(new_chinese_list[i])
        print(pinyin[i].text)
        print(' '.join(english[i].text.split()))


# Python command argument - will keep running until you quit the script
while True:
    query = input('Type in the word: ')
    if ord(query[0]) > 255:
        urlencoded = urllib.parse.quote(query)
        mandarin(query)
    else:
        spanish(query)
