from django.core.management.base import BaseCommand
from scraper.models import Product

import requests
from bs4 import BeautifulSoup
import re
from time import sleep


class Command(BaseCommand):
    help = "Scrap and save in DB"

    def handle(self, *args, **kwargs):
        headers = {"User-Agent": "Mozilla/5.0"}

        for page_count in range(1, 270):
            sleep(1)
            url = f"https://linella.md/ru/catalog?page={page_count}"
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "lxml")
            products = soup.find_all("div", class_="products-catalog-content__item")

            for product in products:
                name_tag = product.find("a", class_="products-catalog-content__name")
                if not name_tag:
                    continue

                name = name_tag.text.strip()
                link = "https://linella.md" + name_tag.get("href")

                text = product.get_text()
                price_match = re.search(r"\d+\.\d{2}", text)
                price = price_match.group() if price_match else None

                if not price:
                    continue

                #save or update
                Product.objects.update_or_create(
                    link=link,
                    defaults={
                        "name": name,
                        "price": price
                    }
                )

        self.stdout.write(self.style.SUCCESS("End Scrapping"))