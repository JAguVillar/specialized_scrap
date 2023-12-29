from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.specialized.com/ar/es/c/bikes")
web_page= response.text

soup = BeautifulSoup(web_page, 'html.parser')
article_tag = soup.findAll('article', {'data-component': 'product-tile'})


for i in article_tag:
    print(i.find('h3').text)
    children = i.find_all(recursive=False)
    last = children[0]
    last_child = last.find_all(recursive=False)
    price = last_child[-1].find('span').text
    print(price, '\n')

#
# h3_text = anchor_tag.find(name='h3').text
#
# print(h3_text)

