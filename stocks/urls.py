from django.urls import path

from .views import BulkInsertProductView

urlpatterns = [
    path('products/bulk_insert/', BulkInsertProductView.as_view()),
]
