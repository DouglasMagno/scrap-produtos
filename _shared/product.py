import json


class Product:
    def __init__(self, **args):
        self.title = args.get('title', None)
        self.image_url = args.get('image_url', None)
        self.price = args.get('price', None)
        self.description = args.get('description', None)
        self.url = args.get('url', None)

    def to_json(self):
        return json.dumps({
            'title': self.title,
            'image_url': self.image_url,
            'price': self.price,
            'description': self.description,
            'url': self.url
        })
