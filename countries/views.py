import re
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
