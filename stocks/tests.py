from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import (
    APIRequestFactory,
    force_authenticate,
)

from .models import Product
from .views import BulkInsertProductView


class ViewsTests(TestCase):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user_required = User.objects.create_superuser(
            username='default',
            email='def@def.def',
            password='default',
        )
        cls.factory = APIRequestFactory()
        cls.bulk_insert_path = reverse('products:bulk-insert')
        

    def test_bulk_create_all_right(self):
        json_products_for_insert = {
            'products': [
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
        force_authenticate(request, user=self.user_required)
        response = BulkInsertProductView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'status': 'OK'})
        self.assertEqual(
            len(Product.objects.all()),
            len(json_products_for_insert.get('products'))
        )

    def test_bulk_create_fail_all_validations(self):
        json_products_for_insert = {
            'products': [
                {
                    'id': 'abcd',
                    'name': 'a'*2,
                    'value': 0,
                    'discount_value': 1,
                    'stock': -1
                },
                {
                    'id': 'abce',
                    'name': 'a'*56,
                    'value': 99999.91,
                    'discount_value': 100000,
                    'stock': -1
                },
            ]
        }
        error_response = {
            'status': 'ERROR',
            'products_report': [
                {
                    'id': 'abcd',
                    'errors': [
                        'Invalid product name',
                        'Invalid stock value',
                        'Invalid value',
                        'Invalid discount value'
                    ]
                },
                {
                    'id': 'abce',
                    'errors': [
                        'Invalid product name',
                        'Invalid stock value',
                        'Invalid value',
                        'Invalid discount value'
                    ]
                },
            ],
            'number_of_products_unable_to_parse': 2
        }
        request = self.factory.post(
            self.bulk_insert_path,
            json_products_for_insert,
            format='json'
        )
        force_authenticate(request, user=self.user_required)
        response = BulkInsertProductView.as_view()(request)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.data, error_response)
