import requests
import bs4
import csv

csvRow = []
url = 'https://www.drugs.com/otc-a1.html'  # select url
req = requests.get(url)  # create a req object
soup = bs4.BeautifulSoup(req.text, 'lxml')  # call Beautiful soup
CsvFile = open('Href.csv', 'w', newline='')
writer = csv.writer(CsvFile)
try:
    for b in soup.select('.column-list-2.sitemap-list'):
        for a in b.findAll('a', href=True):
            csvRow = [a['href']]
            writer.writerow(csvRow)
finally:
    CsvFile.close()
