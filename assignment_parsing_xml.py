import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_468303.xml'

fhand = urllib.request.urlopen(url, context=ctx)
data = fhand.read()

tree = ET.fromstring(data)

br = 0
suma = 0

counts = tree.findall('.//count')
for item in counts :
    br = br + 1
    suma = suma + int(item.text)

print('Count:', br)
print('Sum' , suma)
