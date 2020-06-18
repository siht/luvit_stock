from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
)
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
        if(serializer.is_valid()):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({'status': 'OK'}, headers=headers)
        list_errors = list(
            map(lambda obj: {
                'id': str(obj['id'][0]),
                'errors': list(map(
                    lambda e: str(e),
                    obj['errors']
                ))
            }, serializer.errors)
        )
        error_response = {
            'status': 'ERROR',
            'products_report': list_errors,
            'number_of_products_unable_to_parse': len(list_errors)
        }
        return Response(
            error_response,
            status=status.HTTP_422_UNPROCESSABLE_ENTITY
        )


class ListProductsView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        data_response = {
            'Products': serializer.data
        }
        return Response(data_response)
