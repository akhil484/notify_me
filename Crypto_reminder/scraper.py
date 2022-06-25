import requests
from bs4 import BeautifulSoup


def get_crypto_price(name):
  url1="https://coinmarketcap.com/currencies/"+name+"/"
  source=requests.get(url1)
  soup=BeautifulSoup(source.content,"html.parser")
  div_tag=soup.find('div',class_='priceValue')
  return div_tag.span.text



if __name__ == '__main__':
	print(get_crypto_price("dogecoin"))

