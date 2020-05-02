import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input ('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
suma = 0
count =0
# sve linkove
tags = soup ('span')
for tag in tags :
    #print(tag.contents[0])
    suma = suma + int(tag.contents[0])
    count = count + 1
print('Count ', count)
print('Sum', suma)
