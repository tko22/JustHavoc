# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import User,Brand,ProductType,ProductCategory,ProductColor,ProductTag,Product

# Register your models here.
admin.site.register(User)
admin.site.register(Brand)
admin.site.register(ProductType)
admin.site.register(ProductColor)
admin.site.register(ProductTag)
admin.site.register(ProductCategory)
admin.site.register(Product)
