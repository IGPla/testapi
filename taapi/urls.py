# -*- coding: utf-8 -*-
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from taapi import views

urlpatterns = [
    url(r'^products/list/(?P<brand>[a-zA-Z0-9]+)/$',
        views.ListProducts.as_view(),
        name = "taapi.list_products"),
    url(r'^products/create/$',
        views.CreateProduct.as_view(),
        name = "taapi.create_product"),
    url(r'^products/detail/(?P<pk>[a-zA-Z0-9]+)/$',
        views.RetrieveProduct.as_view(),
        name = "taapi.retrieve_product"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
