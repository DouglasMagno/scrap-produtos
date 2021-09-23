import traceback
from datetime import timedelta, datetime

from src.parsers.americanas import Americanas
from src.parsers.magalu import Magalu
from .models import Product
from .scraper import Scraper


class Service:

    def find_product_by_url(self, url) -> Product:
        try:
            # TODO: filtrar por 24 horas
            return Product.objects(url=url).first()
        except:
            return None

    def get_product_data(self, url: str):
        product = self.find_product_by_url(url)
        if product:
            next_update = product.updated_at + timedelta(minutes=60)
            if next_update >= datetime.now():
                return product.to_dict()
        else:
            product = Product(url=url)
        parser = self.choose_parser(url)
        scraper = Scraper(product, parser)
        product = scraper.handle()
        try:
            product.save()
        except:
            traceback.print_exc()
        return product.to_dict()

    def choose_parser(self, url):
        parsers = {
            'americanas': Americanas(),
            'magazineluiza': Magalu()
        }

        for parser in parsers:
            if parser in url:
                return parsers[parser]

        raise Exception('no parser')
