import os
import unittest

from src._shared.models import Product
from src.parsers.magalu import Magalu


class MagaluTest(unittest.TestCase):

    def build_magalu_sample_html(self):
        try:
            dir_path = os.path.dirname(os.path.realpath(__file__))
            file = open(f"{dir_path}/../samples/magalu-sample.html", "r", encoding='UTF-8')
            content = file.read().replace('\n', '')
            file.close()
            return content
        except:
            return ''

    def test_build_product(self):
        magalu_sample_html = self.build_magalu_sample_html()
        parser = Magalu()
        product = parser.handle(magalu_sample_html, Product(url='https://google.com.br'))
        product.save()
        self.assertTrue(product.id)

if __name__ == '__main__':
    unittest.main()