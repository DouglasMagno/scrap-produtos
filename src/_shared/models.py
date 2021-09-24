from datetime import datetime
from mongoengine import (
    connect, DynamicDocument, signals, Document, EmbeddedDocument,
    IntField, StringField, URLField, BooleanField, DateTimeField, ListField,
    ReferenceField, DateField, EmbeddedDocumentListField, FloatField, DictField
)
from mongoengine.base import LazyReference

from .constants import ENV
from .helpers import datetime2json

db = connect(ENV.SOLUTION, host=f"{ENV.MONGO_URL}")


def handler(event):
    """
    Signal decorator to allow use of callback functions as class decorators.
    see: https://docs.mongoengine.org/guide/signals.html
    """

    def decorator(fn):
        def apply(cls):
            event.connect(fn, sender=cls)
            return cls

        fn.apply = apply
        return fn

    return decorator


@handler(signals.pre_save)
def pre_save_updated_at(sender, document):
    """
    update field "updated_at" in doc
    """
    document.updated_at = datetime.now()


# ~=~=~= Models
@pre_save_updated_at.apply
class Product(DynamicDocument):
    """
    registed products
    """

    meta = {
        'indexes': [
            'url'
        ]
    }

    title = StringField(required=True)
    price = FloatField(required=True)
    description = StringField(required=True)
    url = URLField(required=True)
    image_url = URLField(required=True)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField()

    def to_dict(self) -> dict:
        return {
            'title': self.title,
            'price': self.price,
            'description': self.description,
            'url': self.url,
            'created_at': datetime2json(self.created_at),
            'updated_at': datetime2json(self.updated_at)
        }
