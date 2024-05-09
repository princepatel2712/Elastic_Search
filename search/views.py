from rest_framework import generics
from .documents import ProductDocument
from .serializers import ProductSerializer
from rest_framework import viewsets
from .models import Product


class ProductSearchAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        """
        Example-URL: http://127.0.0.1:8000/product-search/?q=Bottle
        """
        q = self.request.query_params.get('q', '')
        s = ProductDocument.search().query('match', name=q)
        response = s.execute()
        return [hit.to_dict() for hit in response]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
