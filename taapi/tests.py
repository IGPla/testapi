# -*- coding: utf-8 -*-
from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient
from tacore import mongomodels
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import time

class APITestCase(TestCase):
    def setUp(self):
        mongomodels.Product.objects().delete()
        self.client = APIClient()
        self.username = "test1"
        self.password = "Qwerty12345"
        self.email = "test1@test1.com"
        self.user = User.objects.create_user(username = self.username, password = self.password, email = self.email)
        self.token = Token.objects.create(user=self.user)
        self.product_reference = "abcd"
        self.product_brand_identifier = "bcde"
        self.product = mongomodels.Product(reference = self.product_reference,
                                           brand_identifier = self.product_brand_identifier).save()
        
    def tearDown(self):
        mongomodels.Product.objects().delete()

    def test_api_create_product(self):
        """
        Test CreateProduct api call
        """
        prev_products = mongomodels.Product.objects().count()
        response = self.client.post(reverse("taapi.create_product"),
                                     {'reference': 'test1',
                                      'brand_identifier': 'test1'})
        self.assertEqual(response.status_code, 401)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(reverse("taapi.create_product"),
                                     {'reference': 'test1',
                                      'brand_identifier': 'test1'},
        )
        self.assertEqual(response.status_code, 201)
        time.sleep(1)
        self.assertEqual(prev_products+1, mongomodels.Product.objects().count())

    def test_api_list_products(self):
        """
        Test ListProducts api call
        """
        prev_products = mongomodels.Product.objects().count()
        response = self.client.get(reverse("taapi.list_products", kwargs = {'brand': self.product_brand_identifier}))
        self.assertEqual(response.status_code, 401)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(reverse("taapi.list_products", kwargs = {'brand': self.product_brand_identifier}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("count"), 1)
        self.assertEqual(response.json().get("results")[0].get("reference"), self.product_reference)
        
    def test_api_retrieve_product(self):
        """
        Test RetrieveProduct api call
        """
        prev_products = mongomodels.Product.objects().count()
        response = self.client.get(reverse("taapi.retrieve_product", kwargs = {'pk': self.product_reference}))
        self.assertEqual(response.status_code, 401)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(reverse("taapi.retrieve_product", kwargs = {'pk': self.product_reference}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("reference"), self.product_reference)
