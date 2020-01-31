import requests 
from bs4 import BeautifulSoup 
import csv 
URL = "https://www.passiton.com/inspirational-quotes"
r = requests.get(URL) 
soup = BeautifulSoup(r.content, 'html5lib') 
quotes=[]

table = soup.find('div', attrs = {'id':'all_quotes'}) 
  
for row in table.findAll('div', attrs = {'class':'col-6'}): 
    quote = {} 
    quote['theme'] = row.h5.text 
    quote['url'] = row.a['href'] 
    quote['img'] = row.a.img['src']  
    quotes.append(quote)  
 
filename = 'inspirational_quotes.csv'

f = open(filename, "a")

for quote in quotes:
	f.write(str(quote))

f.close()

