from django.shortcuts import render
from dajngo.http.reponse import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from countries.models import Countries
from countries.serializers import CountriesSerializer
from rest_framework.decorators import api_view

# Create your views here.

#setting the decorator
@api_view(['GET','PUT','DELETE'])
def countries_detail(request,pk):
    try:
        countries = Countries.objects.get(pk=pk)
    except Countries.DoesNotExist:
        return JsonResponse({'message':'The Country does not exist'},status=status.HTTP_404_NOT_FOUND)

    if request.method == ' GET':
        countries_serializer = CountriesSerializer(countries)
        return JsonResponse(countries_serializer.data)

    elif request.method =='PUT':
        countries_data= JSONParser().parse(request)
        countries_serializer= CountriesSerializer(countries, data=countries_data)
        if countries_serializer.is_valid():
            countries_serializer.save()
            return JsonResponse(countries_serializer.data)
        return JsonResponse(countries_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        countries.delete()
        return JsonResponse({'message':'Country was deleted sucessfully!'},status=status.HTTP_204_NO_CONTENT)
        






    