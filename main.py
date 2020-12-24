from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

news_url='https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419'

root=urlopen(news_url)

xml_page=root.read()
root.close()

soup_page=soup(xml_page, "xml")
news_list=soup_page.findAll("item")

for news in news_list:
  print(news.title.text)
  print(news.link.text)
  print(news.pubDate.text)
  print("-"*120)
