import traceback

from bs4 import BeautifulSoup
from requests import Response

from src._shared.models import Product


class Magalu:

    def handle(self, response_html, product: Product) -> Product:
        soup = BeautifulSoup(response_html, 'html.parser')
        product.title = soup.find("meta", property="og:title")['content']
        product.price = float(soup.find(class_='price-template__text').text.replace('.', '').replace('R$ ', '').replace(',', '.'))
        product.image_url = soup.find("meta", property="og:image")['content']
        product.description = soup.find("meta", property="og:description")['content']
        return product
