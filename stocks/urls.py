from django.urls import path

from .views import (
    BulkInsertProductView,
    ListProductsView,
)

app_name = 'products'

urlpatterns = [
    path('products/bulk_insert/', BulkInsertProductView.as_view(), name='bulk-insert'),
    path('products/', ListProductsView.as_view(), name='list'),
]
