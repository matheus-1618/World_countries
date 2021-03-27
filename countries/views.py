from django.shortcuts import render
from dajngo.http.reponse import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from countries.models import Countries
from countries.serializers import CountriesSerializer
from rest_framework.decorators import api_view

# Create your views here.
