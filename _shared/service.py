import traceback

import requests

from parsers.americanas import Americanas
from parsers.magalu import Magalu
from .models import Product
from .scraper import Scraper


class Service:

    def find_product_by_url(self, url) -> Product:
        try:
            return Product.objects(url=url).first()
        except:
            return None

    def get_product_data(self, url: str):
        product_in_data_base = self.find_product_by_url(url)
        if product_in_data_base:
            return product_in_data_base.to_dict()
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
