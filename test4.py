from selenium import webdriver
from bs4 import BeautifulSoup
import json

driver = webdriver.Chrome()
driver.get("https://research.com/u/anil-k-jain")
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

name = soup.select_one(".profile-head__info__text > h1")
location = soup.find('p', class_="pl-ipad mb-0")
universityAndCountry = location.find_all('a')
dIndexAndMetrics = soup.find_all('div', class_='metrics-table__row')
parameter1 = dIndexAndMetrics[0].find_all('span')
parameter2 = dIndexAndMetrics[1].find_all('span')
award = soup.find_all('div', class_='profile-achievements shadow')
achievements = award[0].find_all('p')
overview = soup.find('div', class_='tab bg-white shadow')
overview1 = overview.find_all('h2')
overview2 = overview.find_all('h3')
overview3 = overview.find_all('p')
bestKnownFor = overview.find_all('ul')
bestKnownFors1 = bestKnownFor[0].find_all('li')
bestKnownFors2 = bestKnownFor[1].find_all('li')
bestKnownFors3 = bestKnownFor[2].find_all('li')
bestKnownFors4 = bestKnownFor[3].find_all('li')
bestKnownFors5 = bestKnownFor[4].find_all('li')
bestKnownFors6 = bestKnownFor[5].find_all('li')
bestPublications = soup.find('div', class_='profile-publications tab bg-white shadow')
leftBestPublications = bestPublications.find_all('div', class_='profile-publications__left')
rightBestPublications = bestPublications.find_all('div', class_='profile-publications__right')
bestScientist = soup.find('div', id='tab-3')
bestScientist_h2 = bestScientist.find('h2')
bestScientist_a = bestScientist.find_all('a')
bestScientist_p = bestScientist.find_all('p')
citation = soup.find('div', class_='sidebar bg-white shadow')
citation_h3 = citation.find('h3')
citation_div = citation.find('div')['data-citations']
citations_list = json.loads(citation_div)
frequent = citation.find_all('h3')[1]
author = soup.find_all('div', class_='sidebar-author')
external = citation.find_all('h3')[2]
print(external)
external_link = citation.find('ul')
print(external_link)
links = external_link.find_all('a')
for link in links:
    href = link.get('href')
    print(href)


print(name.text)
print(universityAndCountry[0].text.strip())
print(universityAndCountry[1].text.strip())

print("\n")

print(parameter1[1].find('span').next_sibling.strip())
print(parameter1[3].find('span').next_sibling.strip())
print(parameter1[5].text.strip())
print(parameter1[6].find('span').next_sibling.strip())
print(parameter1[8].find('span').next_sibling.strip())

print("\n")

print(parameter2[1].find('span').next_sibling.strip())
print(parameter2[3].find('span').next_sibling.strip())
print(parameter2[5].text.strip())
print(parameter2[6].find('span').next_sibling.strip())
print(parameter2[8].find('span').next_sibling.strip())

print("\n")

for i in list(range(len(achievements))):
    print(' '.join(achievements[i].text.split()))
print(overview1[0].text)
print(overview1[1].text)
print(overview2[0].text)
for i in range(len(bestKnownFors1)):
    print('*', bestKnownFors1[i].text)
print(overview3[0].text, '\n')
print(overview2[1].text)
for i in range(len(bestKnownFors2)):
    print('*', bestKnownFors2[i].text)
print(overview1[2].text, '\n')
print(overview3[1].text)
print(overview2[2].text)
for i in range(len(bestKnownFors3)):
    print('*', bestKnownFors3[i].text)
print(overview1[3].text, '\n')
for i in range(len(bestKnownFors4)):
    print('*', bestKnownFors4[i].text)
print(overview2[3].text)
print(overview3[2].text)
print(overview2[4].text)
for i in range(len(bestKnownFors5)):
    print('*', bestKnownFors5[i].text)
print(overview1[4].text, '\n')
for i in range(len(bestKnownFors6)):
    print('*', bestKnownFors6[i].text)
print(overview3[3].text)
leftBestPublications_p = []  # Khởi tạo list trống

for i in range(10):
    leftBestPublications_p.append(leftBestPublications[i].find_all('p'))
    print(leftBestPublications_p[i][0].text.strip())
    print(leftBestPublications_p[i][1].text.strip())
    print(rightBestPublications[0].text.strip(), '\n')
print(bestScientist_h2.text.strip())
for i in range(12):
    print(bestScientist_a[i].text.strip())
    print(bestScientist_p[i*2].text.strip())
    print(bestScientist_p[i * 2+1].text.strip(), '\n')

print(citation_h3.text.strip())
for i in range(4):
    print(2019+i, ':', citations_list[i]['y'])
print('\n')
print(frequent.text.strip())
for i in range(10):
    print(author[i].find('a').text.strip())
    print(author[i].find('p').text.strip(), '\n')
print(external.text.strip())
for link in links:
    title = link.get('title')
    print(title)
    href = link.get('href')
    print(href)
driver.quit()
