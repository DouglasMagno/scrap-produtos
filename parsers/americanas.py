from bs4 import BeautifulSoup
from requests import Response

from _shared.product import Product


class Americanas:

    def handle(self, response_html: Response, product: Product) -> Product:
        soup = BeautifulSoup(response_html, 'html.parser')
        product.title = soup.find("meta", property="og:title")['content']
        product.price = float(soup.find(class_='priceSales').text.replace('.', '').replace('R$ ', '').replace(',', '.'))
        product.image_url = soup.find("meta", property="og:image")['content']
        product.description = soup.find("meta", property="og:description")['content']
        return product
