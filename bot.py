import requests
import bs4
import csv
j = 1
csvRow = []
while j < 29:
    print(j)
    url = 'https://www.drugs.com/otc-a%d.html' % (j)
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.text, 'lxml')
    var = soup.select('.column-list-2.sitemap-list')
    CsvFile = open('Otc.csv', 'wt', newline='')
    writer = csv.writer(CsvFile)
    try:
        for cell in var:
            csvRow.append(cell.text)
        writer.writerow(csvRow)
    finally:
            CsvFile.close()
    j = j + 1

print("done")









