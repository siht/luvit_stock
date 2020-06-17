from rest_framework.generics import CreateAPIView

from .models import Product
from .serializers import ProductSerializer


class BulkInsertProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
