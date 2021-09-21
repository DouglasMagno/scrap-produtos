import traceback

import requests

from parsers.americanas import Americanas
from parsers.magalu import Magalu
from .product import Product
from .scraper import Scraper


class Service:

    def get_product_data(self, url: str):
        product = Product(url=url)
        parser = self.choose_parser(url)
        scraper = Scraper(product, parser)
        return scraper.handle()

    def choose_parser(self, url):
        parsers = {
            'americanas': Americanas(),
            'magazineluiza': Magalu()
        }

        for parser in parsers:
            if parser in url:
                return parsers[parser]

        raise Exception('no parser')
