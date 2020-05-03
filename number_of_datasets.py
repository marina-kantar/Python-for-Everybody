#Write a Python program to get the number of datasets currently listed on data.gov.

from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.data.gov/').text
soup = BeautifulSoup(source, 'html.parser')

#print(soup.prettify)

x = soup.small.a.text
#print(x)
l =x.split()
print('Number of datasets currently listed on data.gov is: ', l[0])



   
    

