import urllib
import urllib2
from bs4 import BeautifulSoup
#open search result for viewing
#import webbrowser


search = urllib.urlencode({'item':'Python'})

url = 'http://139.59.1.147/search-courses/'
full_url = url + '?' + search
response = urllib2.urlopen(full_url)


with open("search-page.html","w") as f:
    data = response.read()
    f.write(data)

soup = BeautifulSoup(data, "html.parser")
print soup.title
#webbrowser.open("search-page.html")

