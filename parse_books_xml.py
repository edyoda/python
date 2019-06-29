from bs4 import BeautifulSoup
infile = open("books.xml","r")
contents = infile.read()
soup = BeautifulSoup(contents,'xml')
titles = soup.find_all('title')
authors = soup.find_all('author')
prices = soup.find_all('price')
for i in range(0, len(titles)):
    print(titles[i].get_text(),"by",end=' ')
    print(authors[i].get_text(),end=' ')
    print("costs $" + prices[i].get_text())
