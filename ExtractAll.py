import requests
import bs4
import csv
import re


def name(x):
    url = 'https://www.drugs.com' + x
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.text, 'lxml')
    for a in soup.body.b:
        return a


def dosage(y):
    url = 'https://www.drugs.com' + y
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.text, 'lxml')
    for a in soup.findAll('p', limit=2):
        if re.search(r'Dosage form:', a.text, re.M | re.I):                   # using regular expression for obtain dosage
            replace = re.sub(r'Ingredients:', " Ingredients:", a.text)
            replace = re.sub(r'Labeler:', " Labeler:", replace)
            find = re.search(r'Dosage form: (.*) Ingredients: (.*?) Labeler', replace, re.M | re.I)
            return find.group(1)

        elif re.search(r'Name: ', a.text, re.M | re.I):
            replace = re.sub(r'Form:', " Form:", a.text)
            replace= re.sub(r'Ingredients:', " Ingredients:", a.text)
            replace = re.sub(r'Date:', " Date:", replace)
            find = re.search(r'Form: (.*) Ingredients: (.*?) Date', replace, re.M | re.I)
            return find.group(1)


def ingd(y):
    url = 'https://www.drugs.com' + y
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.text, 'lxml')
    for a in soup.findAll('p', limit=2):
        if re.search(r'Dosage form:', a.text, re.M | re.I):                   # using regular expression for obtain ingrediants
            replace = re.sub(r'Ingredients:', " Ingredients:", a.text)
            replace = re.sub(r'Labeler:', " Labeler:", replace)
            find = re.search(r'Dosage form: (.*) Ingredients: (.*?) Labeler', replace, re.M | re.I)
            return find.group(2)

        elif re.search(r'Name: ', a.text, re.M | re.I):
            replace = re.sub(r'Form:', " Form:", a.text)
            replace= re.sub(r'Ingredients:', " Ingredients:", a.text)
            replace = re.sub(r'Date:', " Date:", replace)
            find = re.search(r'Form: (.*) Ingredients: (.*?) Date', replace, re.M | re.I)
            return find.group(2)


def purpose(y):
    t = "none"
    url = 'https://www.drugs.com' + y
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.text, 'lxml')
    if soup.findAll('tr', attrs={'class': 'First Toprule'}):
        for a in soup.findAll('tr', attrs={'class': 'First Toprule'}):
            for p in a.select('td'):
                print('')
            return p.text

    elif soup.findAll('tr', attrs={'class': 'Botrule Last'}):
        for x in soup.findAll('tr', attrs={'class': 'First Toprule'}):
            for y in x.select('td'):
                print('')
            return y.text

    elif soup.findAll('div', attrs={'class': 'Section'}):
        for a in soup.findAll('div', attrs={'class': 'Section'}, limit=4):
            for b in a.select('.First'):
                t = [b.text]  # 78 page is not working
        return t


def uses(z):
    t = "none"
    url = 'https://www.drugs.com' + z
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.text, 'lxml')
    if soup.findAll('div', attrs={'class': 'Section'}):
        for a in soup.findAll('div', attrs={'class': 'Section'}, limit=5):

            if a.findAll('ul', attrs={'class': 'Disc'}):
                for c in a.findAll('ul', attrs={'class': 'Disc'}):
                    for d in c.select('li'):
                        t = [d.text]
                return t

            elif a.findAll('ul'):                    # Added this for the page who doesn't have '.First' class
                for c in a.findAll('ul'):
                    for d in c.select('li'):
                        t = [d.text]
                return t

            elif a.findAll('ul', attrs={'class': 'Square'}):
                for c in a.findAll('ul', attrs={'class': 'Square'}):
                    for d in c.select('li'):
                        t = [d.text]
                return t

    if soup.findAll('div', attrs={'class': 'Section'}):
        for a in soup.findAll('div', attrs={'class': 'Section'}, limit=4):
            for b in a.select('.First'):
                t = [b.text]
        return t


def flex():
    with open('Otc_Extract_1_10.csv', 'a', newline='')as csvfile:
        file_obj = open('OTC_FOR_A.csv', 'r')
        writer = csv.writer(csvfile)
        writer.writerow(['NAME', 'LINKS', 'DOSAGE', 'INGREDIENT', 'PURPOSE', 'USES'])
        for r in csv.reader(file_obj):
            r = list(csv.reader(file_obj))
            for a in range(1, 10):
                print(a)
                writer.writerow([name(r[a][1]), 'www.drugs.com' + r[a][1], dosage(r[a][1]), ingd(r[a][1]), purpose(r[a][1]), uses(r[a][1])])  # here r[m][n] we
                # have [m] as row and [n] as column


flex()
