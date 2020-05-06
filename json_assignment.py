import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_468304.json'

fhand = urllib.request.urlopen(url, context=ctx)
data = fhand.read()

info = json.loads(data)
#print('User count:', len(info))

br = 0
suma = 0

for item in info["comments"]:
    br = br + 1
    suma = suma + item["count"]

print('Count:', br)
print('Sum' , suma)