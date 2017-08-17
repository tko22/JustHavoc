# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from decimal import Decimal


class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    date_created = models.DateField(blank=True)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('username',)


class Brand(models.Model):
    name = models.CharField(max_length=30, unique=True)
    store_url = models.URLField(blank=True)
    logo_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.name


class ProductType(models.Model):
    """The Type of Product - ex: food,clothing,shoes"""
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    """Product Categories - ex: Basics, Jeans, Shorts, Coats & Jackets """
    name = models.CharField(max_length=30)
    productType = models.ForeignKey(ProductType, related_name='productCategories', on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class ProductTag(models.Model):
    name = models.CharField(max_length=100)
    productType = models.ForeignKey(ProductType, related_name='productTags', on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class ProductColor(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.URLField(blank=True)
    brand = models.ForeignKey(Brand, related_name='productColors', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, related_name='items', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('0.00'))
    size = models.CharField(max_length=10, blank=True, help_text='please')
    description = models.TextField(blank=True)
    images_path = models.CharField(max_length=100, blank=True)
    productTypes = models.ManyToManyField(ProductType, related_name='products', blank=True)
    productCategories = models.ManyToManyField(ProductCategory, related_name='products', blank=True)
    productTags = models.ManyToManyField(ProductTag, related_name='products', blank=True)
    productColors = models.ManyToManyField(ProductColor, related_name='products', blank=True)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('brand',)
