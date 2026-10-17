from bs4 import BeautifulSoup
import requests
url = "https://books.toscrape.com/"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("div", {"class": "col-sm-8 h1"}).text
    print("Заголовок: ", title )
    books = soup.find_all("article", {"class": "product_pod"})[:5]
    print("Перші 5 книг:")
    for book in books:
        title = book.find("h3").text
        price = book.find("p", {"class": "price_color"}).text
        print("Назва:", title,  "Ціна:", price)
else:
    print("Сторінку не вдалося завантажити")