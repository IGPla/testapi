# -*- coding: utf-8 -*-
import mongoengine
from django.urls import reverse

class Product(mongoengine.Document):
    reference = mongoengine.StringField(required = True,
                                        unique = True)
    brand_identifier = mongoengine.StringField(required = True)

    def api_retrieve_url(self):
        return reverse("taapi.retrieve_product", kwargs = {'pk': self.reference})
