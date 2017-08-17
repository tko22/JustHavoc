from django.contrib.auth.models import User
from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    """UserSerializer"""
    password = serializers.CharField(
        write_only=True, style={'input_type': 'password'})

    class Meta:
        model = models.User
        fields = ('id', 'username', 'email',
                  'first_name', 'last_name', 'password')
        write_only_fields = ('password',)

class BrandSerializer(serializers.ModelSerializer):
    """BrandSerializer"""

    class Meta:
        model = models.Brand
        fields = ['id','name','store_url','logo_url','description','slug']

class ProductTypeSerializer(serializers.ModelSerializer):
    """ProductTypeSerializer"""

    class Meta:
        model = models.ProductType
        fields = ['id','name','description']

class ProductCategorySerializer(serializers.ModelSerializer):
    """ProductCategorySerializer"""
    class Meta:
        model = models.ProductCategory
        fields = ['id','name','description','productType']

class ProductTagSerializer(serializers.ModelSerializer):
    """ProductTagSerializer"""

    class Meta:
        model = models.ProductTag
        fields = ['id','name','productType','description']

class ProductColorSerializer(serializers.ModelSerializer):
    """ProductColorSerializer"""

    class Meta:
        model = models.ProductColor
        fields = ['id','name','image_url','brand']

class ProductSerializer(serializers.ModelSerializer):
    """ProductSerializer"""

    productColor = ProductColorSerializer
    brand = serializers.StringRelatedField()
    class Meta:
        model = models.Product
        fields = ['id','name','brand','price','size','description','images_path','productCategories',
                  'productTypes','productTags','productColors','slug']
