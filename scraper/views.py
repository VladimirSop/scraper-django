import re
import requests
from bs4 import BeautifulSoup
from time import sleep
from django.shortcuts import render

def linella_scraper(request):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0"
    }

    products_list = []  # сюда будем складывать данные

    for page_count in range(1, 5):
        sleep(3)  # пауза между запросами
        url = f"https://linella.md/ru/catalog?page={page_count}"  # исправил url, чтобы page_count вставлялся правильно
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        products = soup.find_all("div", class_="products-catalog-content__item")

        for product in products:
            name_tag = product.find("a", class_="products-catalog-content__name")
            price_tag = product.find("span", class_="price-products-catalog-content__static")

            if name_tag:
                name = name_tag.text.strip()
                link = "https://linella.md" + name_tag.get("href")
            else:
                continue

            textLinella = product.get_text()
            price_match = re.search(r"\d+\.\d{2}", textLinella)
            price = price_match.group() if price_match else "нет цены"

            # Сохраняем данные в список словарей
            products_list.append({
                "name": name,
                "link": link,
                "price": price
            })

    # Передаём список продуктов в HTML через context
    return render(request, "scraper/index.html", {"products": products_list})