from django.test import TestCase
from rest_framework.test import APIRequestFactory

from .views import BulkInsertProductView


class ViewsTests(TestCase):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.factory = APIRequestFactory()
        cls.bulk_insert_path = 'api/products/bulk_insert'

    def test_bulk_create_all_right(self):
        json_products_for_insert = {
            "products": [
                {
                    'id': 'abcd',
                    'name': 'galleta',
                    'value': 99,
                    'discount_value': 10,
                    'stock': 100
                },
                {
                    'id': 'abce',
                    'name': 'jugo',
                    'value': 9,
                    'stock': 100
                }
            ]
        }
        request = self.factory.post(
            self.bulk_insert_path,
            json_products_for_insert,
            format='json'
        )
        response = BulkInsertProductView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'status': 'OK'})
