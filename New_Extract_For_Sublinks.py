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
    for a in soup.findAll('p', limit=3):
        if re.search(r'Dosage form:', a.text, re.M | re.I):
            replace = re.sub(r'Ingredients:', " Ingredients:", a.text)
            replace = re.sub(r'Labeler:', " Labeler:", replace)
            find = re.search(r'Dosage form: (.*) Ingredients: (.*?) Labeler', replace, re.M | re.I)
            return find.group(1)

        elif re.search(r'Name: ', a.text, re.M | re.I):
            replace = re.sub(r'Form:', " Form:", a.text)
            replace = re.sub(r'Ingredients:', " Ingredients:", a.text)
            replace = re.sub(r'Date:', " Date:", replace)
            find = re.search(r'Form: (.*) Ingredients: (.*?) Date', replace, re.M | re.I)
            return find.group(1)


def ingd(y):
    url = 'https://www.drugs.com' + y
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.text, 'lxml')
    for a in soup.findAll('p', limit=3):
        if re.search(r'Dosage form:', a.text, re.M | re.I):
            replace = re.sub(r'Ingredients:', " Ingredients:", a.text)
            replace = re.sub(r'Labeler:', " Labeler:", replace)
            find = re.search(r'Dosage form: (.*) Ingredients: (.*?) Labeler', replace, re.M | re.I)
            return find.group(2)

        elif re.search(r'Name: ', a.text, re.M | re.I):
            replace = re.sub(r'Form:', " Form:", a.text)
            replace = re.sub(r'Ingredients:', " Ingredients:", a.text)
            replace = re.sub(r'Date:', " Date:", replace)
            find = re.search(r'Form: (.*) Ingredients: (.*?) Date', replace, re.M | re.I)
            return find.group(2)


def purpose(y):
    t = "none"
    url = 'https://www.drugs.com' + y
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.text, 'lxml')
    if soup.findAll('tbody', attrs={'class': 'Headless'}) is False:
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

    else:
        t = soup.body.text
        s = t.replace('\n', '')
        replace = s.replace('USES', ' USES ').replace('WARNINGS', ' WARNINGS ').replace('PURPOSE', ' PURPOSE ').replace(
            'Uses', ' Uses ').replace('Purpose', ' Purpose ').replace('Warnings', ' Warnings ').replace('Uses:', ' Uses: ').replace(
            'Purpose:', ' Purpose: ').replace('Warnings:', ' Warnings: ').replace('WARNING', ' WARNINGS').replace('Warning', ' Warnings ')
        find = re.search(r'.* purpose (.*?) uses (.*?) warnings', replace, re.I | re.M)
        find1 = re.search(r'.* purpose (.*?) warnings', replace, re.I | re.M)
        if find:
            return find.group(1)  # PURPOSE
            print(find.group(1))
        elif find1:
            return find1.group(1)
        else:
            print('NONE')


def uses(z):
    # t = "none"
    url = 'https://www.drugs.com' + z
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.text, 'lxml')
    t = soup.body.text
    s = t.replace('\n', '')
    replace = s.replace('USES', ' USES ').replace('WARNINGS', ' WARNINGS ').replace('PURPOSE', ' PURPOSE ').replace(
        'Uses', ' Uses ').replace('Purpose', ' Purpose ').replace('Warnings', ' Warnings ').replace('Uses:',' Uses: ').replace(
        'Purpose:', ' Purpose: ').replace('Warnings:', ' Warnings: ').replace('WARNING', ' WARNINGS').replace('Warning', ' Warnings ')
    find = re.search(r'.* purpose (.*?) uses (.*?) warnings', replace, re.I | re.M)
    find1 = re.search(r'.* uses (.*?) indications', replace, re.I | re.M)
    find2 = re.search(r'.* uses (.*?) warnings', replace, re.I | re.M)
    if find:
        return find.group(2)  # USES
    elif find1:
        return find1.group(1)  # USES
    elif find2:
        return find2.group(1)
    else:
        print('NONE')


def flex():
    with open('Otc_Extract_Sub.csv', 'a', newline="")as csvfile:  # new line problem fixed ''-> ""
        file_obj = open('link.csv', 'r')
        writer = csv.writer(csvfile)
        # writer.writerow(['NAME', 'LINKS', 'DOSAGE', 'INGREDIENT', 'PURPOSE', 'USES'])
        for r in csv.reader(file_obj):
            r = list(csv.reader(file_obj))
            for a in range(1, 101):
                print(a)
                reduce = str(r[a]).replace('[', '').replace(']', '').replace("'", "")
                writer.writerow([name(reduce), 'www.drugs.com' + reduce, dosage(reduce), ingd(reduce), purpose(reduce),
                                 uses(reduce)])  # here r[m][n] we
                # have [m] as row and [n] as column


flex()
