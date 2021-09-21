from datetime import datetime

from bson import DBRef, ObjectId
from mongoengine import (
    connect, DynamicDocument, signals, Document, EmbeddedDocument,
    IntField, StringField, URLField, BooleanField, DateTimeField, ListField,
    ReferenceField, DateField, EmbeddedDocumentListField, FloatField, DictField
)
from mongoengine.base import LazyReference

from .constants import ENV
from .helpers import datetime2json

db = connect(ENV.SOLUTION, host=f"{ENV.MONGO_URL}")


# ~=~=~= Custom fields and stuff related only to models
class CustomReferenceField(ReferenceField):
    """
    custom field type to pass a model directly as a reference
    """

    def validate(self, value):
        if not isinstance(value, (self.document_type, LazyReference, DBRef, ObjectId)):
            self.error('A ReferenceField only accepts DBRef, LazyReference, ObjectId or documents')

        if isinstance(value, Document) and value.pk is None:
            self.error('You can only reference documents once they have been saved to the database')

        if self.document_type._meta.get('abstract') and not isinstance(value, self.document_type):
            klass = self.document_type._class_name
            self.error(f'{klass} is not an instance of abstract reference type {klass}')


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
    document.updated_at = datetime.utcnow()


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
