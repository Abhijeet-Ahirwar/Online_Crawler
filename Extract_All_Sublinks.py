#Find Sublinks For A Given Link
import bs4
import requests
import csv


def link(x):                                                #Find Link And Store In A Csv File.
    url = 'https://www.drugs.com' + x
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.text, 'lxml')
    with open('link.csv', 'a', newline='') as CsvFile:
        writer = csv.writer(CsvFile)
        for links in soup.find_all('a', attrs={'class': 'ddc-btn ddc-btn-sm'}):
            # print(links.get('href'))
            csvRow = [links.get('href')]                   #Just Extract The Links.
            writer.writerow(csvRow)


def fetch():
    file_obj = open('OTC_FOR_A.csv', 'r')                  # opening a file which contain the list of links.
    for r in csv.reader(file_obj):
        r = list(csv.reader(file_obj))                     # Convert A Given Csv File To A 2D List.
        for a in range(1, 2264):
            print(a)
            link(r[a][1])                                  # here r[m][n] we have [m] as row and [n] as column.


fetch()
