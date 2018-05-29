import requests
import bs4


def Purpose():
    print("Purpose And Ingredients:-")
    print("---------------------------------------------------------------------------------------")
    url = 'https://www.drugs.com/otc/111768/azolen.html'
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.text, 'lxml')
    for a in soup.findAll('div', attrs={'class': 'Section'}):
        for c in a.findAll('b'):
            for b in a.select('.First'):
                print(c.text)
                print(b.text)
        print("---------------------------------------------------------------------------------------")


print("")
print("")


def uses():
    print("---------------------------------------------------------------------------------------")
    url = 'https://www.drugs.com/otc/111768/azolen.html'
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.text, 'lxml')
    for a in soup.findAll('div', attrs={'class': 'Section'}):
        for c in a.findAll('ul', attrs={'class': 'Disc'}):
            for b in a.findAll('b'):
                print(b.text+":-")
                for d in c.select('li'):
                    print(d.text)
            print("---------------------------------------------------------------------------------------")


Purpose()
uses()
