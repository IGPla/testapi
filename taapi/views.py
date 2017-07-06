# -*- coding: utf-8 -*-
from rest_framework_mongoengine import generics
from rest_framework.generics import GenericAPIView
from tacore import mongomodels
from taapi import serializers
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

class APICacheView(GenericAPIView):
    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super(APICacheView, self).dispatch(*args, **kwargs)
        
class RetrieveProduct(generics.RetrieveAPIView, APICacheView):
    queryset = mongomodels.Product.objects()
    serializer_class = serializers.ProductSerializer
    lookup_field = "reference"
    lookup_url_kwarg = "pk"

class ListProducts(generics.ListAPIView, APICacheView):
    serializer_class = serializers.ProductsSerializer

    def get_queryset(self, *args, **kwargs):
        return mongomodels.Product.objects(brand_identifier = self.kwargs.get("brand"))

class CreateProduct(generics.CreateAPIView, APICacheView):
    queryset = mongomodels.Product.objects()
    serializer_class = serializers.ProductSerializer

    
