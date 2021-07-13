import re
from django.core.checks import messages
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from countries.models import Countries
from countries.serializers import CountriesSerializer
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET','POST'])
def countries_list(request):
    if request.method=='GET':
        countires= Countries.objects.all()

        name=request.GET.get('name',None)
        if name is not None:
            countires=countires.filter(name__icontains=name)

        countires_serializer= CountriesSerializer(countires,many=True)
        return JSONParser(countires_serializer.data,safe=True)

    elif request.method == 'POST':
        countires_data=JSONParser().parse(request)
        countires_serializer=CountriesSerializer(data=countires_data)
        if countires_serializer.is_valid():
            countires_serializer.save()
            return JsonResponse(countires_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(countires_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def countries_detail(request,pk):
    try:
        countries=Countries.objects.get(pk=pk)
    except Countries.DoesNotExist:
        return JsonResponse({'message':'The country does not exist'},status=status.HTTP_404_NOT_FOUND)
    if request.method =="GET":
        countries_serializer=CountriesSerializer(countries)
        return JsonResponse(countries_serializer.data,status=status.HTTP_200_OK)
    elif request.method=="PUT":
        countries_data=JSONParser.parse(request)
        countries_serializer=CountriesSerializer(countries,data=countries_data)
        if countries_serializer.is_valid():
            countries_serializer.save()
            return JsonResponse(countries_serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(countries_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        countries.delete()
        return JSONParser({"message":"Country was deleted succesfully"},status=status.HTTP_204_NO_CONTENT)
