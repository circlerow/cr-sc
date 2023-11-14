from pymongo import MongoClient
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
for j in range(20):
    driver.get("https://research.com/scientists-rankings/computer-science?page=".format(j))
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    allNameLink = soup.find_all('h4')
    print(allNameLink)
    for i in range(100):
        endPoint = allNameLink[i].find('a')['href']
        fullName = allNameLink[i].text.strip()

        client = MongoClient('mongodb://localhost:27017/')
        db = client['crawl-data']
        collection = db['list-scientist']

        data = {'endPoint': 'https://research.com'+endPoint, 'name': fullName}
        result = collection.insert_one(data)
        print(f"Inserted record ID: {result.inserted_id}")

