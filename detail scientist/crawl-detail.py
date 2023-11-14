import time

import openpyxl
from bs4 import BeautifulSoup
from pymongo import MongoClient
from selenium import webdriver

listEndpoints = []
client = MongoClient('mongodb://localhost:27017/')
db = client['crawl-data']
collection = db['list-scientist']
detailInformation = db['detail-information']


def save_row_to_excel(file_path, data):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    sheet.append(data)
    wb.save(file_path)


for document in collection.find():
    listEndpoints.append(document.get('endPoint'))

for k in range(19, 100):

    # get information crawl full website
    driver = webdriver.Chrome()
    driver.get(listEndpoints[k])
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    nameScientist = soup.select_one(".profile-head__info__text > h1").text.strip()

    location = soup.find('p', class_="pl-ipad mb-0").find('a').text.strip()

    nation = soup.find('p', class_="pl-ipad mb-0").find_all('a')[1].text.strip()

    sidebar_div = soup.find('div', class_='sidebar bg-white shadow')
    externalLink = ''
    if sidebar_div:
        ul_tag = sidebar_div.find('ul')
        if ul_tag:
            externalLink = ul_tag.find_all('a')
    if len(externalLink) == 2:
        personalWebsite = externalLink[1].get('href')
    if len(externalLink) == 1:
        personalWebsite = externalLink[0].get('href')
    else:
        personalWebsite = ''

    bestPublication = []
    lenBestPublication = soup.find_all('div', class_='profile-publications__left')
    for i in range(10):
        lenBestPublication[i].find_all('p')
        bestPublication.append(
            lenBestPublication[i].find_all('p')[0].text.strip() + lenBestPublication[i].find_all('p')[1].text.strip())

    specialized = 'Computer Science'

    researchArea = []
    bestKnowFor = soup.find(
        'div', class_='tab bg-white shadow').find('div', class_='tab-slide').find('ul').find_all('li')
    for i in range(3):
        researchArea.append(bestKnowFor[i].text)

    data = {'nameScientist': nameScientist, 'location': location, 'nation': nation, 'personalWebsite': personalWebsite,
            'bestPublication': bestPublication, 'specialized': specialized, 'researchArea': researchArea}

    dataExcel = [k, nameScientist, '', '', location, nation, '', '', personalWebsite, '', '', ', '.join(map(str, bestPublication)), '', '',
                 specialized, '', ', '.join(map(str, researchArea))]
    save_row_to_excel("detail scientist/data.xlsx", dataExcel)
    result = detailInformation.insert_one(data)
    print(f"Inserted record ID: {result.inserted_id}")

    time.sleep(5)
