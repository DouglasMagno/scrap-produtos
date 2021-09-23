import os
import traceback
import unittest

from src._shared.models import Product
from src.parsers.americanas import Americanas


class AmericanasTest(unittest.TestCase):

    def build_americanas_sample_html(self):
        try:
            dir_path = os.path.dirname(os.path.realpath(__file__))
            file = open(f"{dir_path}/../samples/americanas-sample.html", "r", encoding='UTF-8')
            content = file.read().replace('\n', '')
            file.close()
            return content
        except:
            traceback.print_exc()
            return ''

    def test_build_product(self):
        americanas_sample_html = self.build_americanas_sample_html()
        parser = Americanas()
        product = parser.handle(americanas_sample_html, Product(url='https://google.com.br'))
        product.save()
        self.assertTrue(product.id)

if __name__ == '__main__':
    unittest.main()