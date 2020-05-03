# Write a Python program to display the content of robot.txt for en.wikipedia.org.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html= urllib.request.urlopen('http://en.wikipedia.org/robots.txt', context=ctx).read()
soup =BeautifulSoup(html, 'html.parser')

print(soup)

