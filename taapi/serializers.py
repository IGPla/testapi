# -*- coding: utf-8 -*-
from rest_framework_mongoengine import serializers
from rest_framework.serializers import CharField

from tacore import mongomodels

class ProductsSerializer(serializers.DocumentSerializer):
    url = CharField(source = "api_retrieve_url")
    class Meta:
        model = mongomodels.Product
        fields = ("url", "reference")

class ProductSerializer(serializers.DocumentSerializer):
    class Meta:
        model = mongomodels.Product
        fields = ("reference", "brand_identifier")
