import unittest

from src._shared.models import Product


class ProductTest(unittest.TestCase):

    def build_product(self) -> Product:
        p = Product(
            title='product test',
            price=123.12,
            description='product test',
            url='https://google.com',
            image_url='https://google.com/image.jpg'
        ).save()

        # self.assertIsInstance()
        try:
            return Product.objects(id=p.id).first()
        except:
            return p

    def test_build_product(self):
        product = self.build_product()
        product.save()
        self.assertTrue(product.pk)

if __name__ == '__main__':
    unittest.main()