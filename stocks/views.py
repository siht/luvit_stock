from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class BulkInsertProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data.pop('products'),
            many=True
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'status': 'OK'}, headers=headers)
