# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
import json
import logging
from . import serializers
from .models import User,Brand,ProductColor,ProductTag,ProductType,Product,ProductCategory

logger = logging.getLogger(__name__)


#TODO only allow admin access
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetail(APIView):
    serializer_class = serializers.UserSerializer
    def get_queryset(self):
        #get stuff from body
        return User.objects.filter()

    def get(self,request,format=None):
        serializer = serializers.BrandSerializer(self.get_queryset())
        return Response(serializer.data)


class BrandList(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandSerializer


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def brandDetail(request,slug):
    if request.method == 'GET':
        try:
            brand = Brand.objects.get(pk=1)
        except ObjectDoesNotExist:
            return Response({'status':'failed','message':'Could not find Brand'})
        serializer = serializers.BrandSerializer(brand)
        return Response(serializer.data)

#TODO: allow pages - each page has 30 products
class ClothingList(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(productTypes__name='Clothing')
        return queryset
        # page = self.request.query_params.get('page')
        # if page is not None:
        #     queryset = queryset.
    def get(self,request):
        ret = {'status':'success'}
        ret['results'] = serializers.ProductSerializer(self.get_queryset(),many=True).data
        return Response(ret)


class ClothingListWithCategory(APIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Product.objects.filter(productTypes__name = 'Clothing')
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        pass




