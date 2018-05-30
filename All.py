import requests
import bs4
import csv


def otc(alp):
    j = 1
    while j < 29:
        print(j)
        url = 'https://www.drugs.com/otc-%s%d.html' % (chr(alp), j)
        req = requests.get(url)
        soup = bs4.BeautifulSoup(req.text, 'lxml')
        var = soup.select('.column-list-2.sitemap-list')
        CsvFile = open('OtcAll.csv', 'wt', newline='')  # Open the file
        writer = csv.writer(CsvFile)
        try:
            for cell in var:
                csvRow.append(cell.text)  # insert value into Cell
            writer.writerow(csvRow)
        finally:
            CsvFile.close()
        j = j + 1
        print("Done {}".format(alp))


csvRow = []
j = 97
while j < 123:
    otc(j)
    j = j + 1
    print("Done All")
