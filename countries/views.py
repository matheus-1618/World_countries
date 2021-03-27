from django.shortcuts import render
from dajngo.http.reponse import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from countries.models import Countries
from countries.serializers import CountriesSerializer
from rest_framework.decorators import api_view

# Create your views here.

#setting the decorator
@api_view('GET','POST')
def countries_list(request):
    if request.method=='GET':
        countries= Countries.objects.all()

        name = request.GET('name',None)
        if name is not None:
            countries = countries.folter(name_icontains=name)

        countries_serializer= CountriesSerializer(countries,many=True)
        return JsonResponse(countries_serializer.data,safe=False)

    elif request.method =='POST':
        countries_data=JSONParser().parse(request)
        countries_serializer= CountriesSerializer(data=countries_data)
        if countries_serializer.is_valid():
            countries_serializer.save()
            return JsonResponse(countries_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(countries_serializer.erros, status=status.HTTP_400_BAD_REQUEST)