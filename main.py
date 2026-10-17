#import urllib.request
#opener = urllib.request.build_opener()
#response = opener.open("http://httpbin.org/get")
#print(response.read())

#import requests
#response = requests.get("https://httpbin.org/get")
#print(response.text)
#print(type(response.text))

#import requests
#response = requests.post(
   # "https://httpbin.org/post",
  #  data="Test data",
 #   headers ={"h1": "Test title"}
#)
#print(response.status_code)
#print(response.text)

#import requests
#url="http://quotes.toscrape.com/"
#response = requests.get(url)
#print(response.status_code)
#print(response.text)

#import requests
#from bs4 import BeautifulSoup
#url="http://quotes.toscrape.com/"
#response = requests.get(url)
#if response.status_code == 200:
    #soup = BeautifulSoup(response.text, "html.parser")
   # quotes = soup.find_all("span",{"class":"text"})
  #  for quote in quotes:
 #       print(quote.text)
#else:
   # print("Сторінку невдалося завантажити")



import requests
from bs4 import BeautifulSoup
url="http://quotes.toscrape.com/"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    authors = soup.find_all("small",{"class":"author"})
    for author in authors:
        print(author.text)
else:
    print("Сторінку невдалося завантажити")