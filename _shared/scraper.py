import traceback

import requests
from requests import Response

from .models import Product


class Scraper:
    def __init__(self, product: Product, parser):
        self.product = product
        self.parser = parser

    def get_html(self) -> Response:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
                "Upgrade-Insecure-Requests": "1", "DNT": "1",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate"}

            response = requests.get(self.product.url, headers=headers)
            return response.text
        except Exception as e:
            traceback.print_exc()
            return None

    def parse(self, response_html) -> Product:
        return self.parser.handle(response_html, self.product)

    def to_json(self):
        return self.product.to_json()

    def handle(self):
        try:
            response_html = self.get_html()
            self.product = self.parse(response_html)
            return self.product.to_dict()
        except Exception as e:
            traceback.print_exc()
