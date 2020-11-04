##Ensure that the module is installed in
##Your Python Directory Before You Import
## pip3 install beautifulsoup4

#Beautiful Soup for Python 3
from bs4 import BeautifulSoup
import urllib
import re

#For Python 3 include .request before .urlopen
#Replace Your URL XXX
html_page = urllib.request.urlopen("XXX")
soup = BeautifulSoup(html_page)
images = []
for img in soup.findAll('img'):
    images.append(img.get('src'))

print(images)
