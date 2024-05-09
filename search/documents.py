from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Product


@registry.register_document
class ProductDocument(Document):
    class Index:
        name = 'product'

        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Product
        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'name',
            'description',
            'stock',
            'price'
        ]
