import re
import urllib.request as ur
from bs4 import BeautifulSoup as bs
import operator

url = 'https://quotes.toscrape.com/tag/love/'
html = ur.urlopen(url)
soup = bs(html.read(), 'html.parser')
quotes = soup.find_all('div',{"class":"quote"})
sentences = []
cnt = dict()
for quote in quotes:
    quote = quote.find_all('span',{"class":"text"})
    for i in quote:
        sentences.append(i.text)
for i in sentences:
    i = re.sub(r"[^\uAC00-\uD7A3\s0-9a-zA-Z]", "",i.lower())
    for j in i.split():
        if j in cnt:
            cnt[j]+=1
        else:    
            cnt[j]=1
sorted_cnt = sorted(cnt.items(),key=operator.itemgetter(1),reverse=True)
for i in range(5):
    print(f"{sorted_cnt[i][0]}, {sorted_cnt[i][1]}")