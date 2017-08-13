# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
import logging
from . import serializers
# Create your views here.


logger = logging.getLogger(__name__)