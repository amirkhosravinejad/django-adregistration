from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from regist.models import advertise
from regist.serializers import adSerializer
# Create your views here.

@api_view(['GET'])
def ad_list(request):
    advertises = advertise.objects.all()
    """advertise_dict = list(advertises.values())
    return JsonResponse({
        'advertises' : advertise_dict
    })"""
    ad_se = adSerializer(advertises, many=True)
    return Response(ad_se.data)

@api_view(['POST'])
def ad_create(request):
    ad_se = adSerializer(data = request.data)
    if ad_se.is_valid():
        ad_se.save()
        return Response(ad_se.data)
    else:
        return Response(ad_se.errors)

@api_view(['PUT', 'GET', 'DELETE'])
def advert(request, pk):
    advert = advertise.objects.get(pk = pk)
    if request.method == 'GET':
        ad_se = adSerializer(advert)
        return Response(ad_se.data)

    if request.method == 'PUT':
        ad_se = adSerializer(advert, data = request.data)
        if ad_se.is_valid():
            ad_se.save()
            return Response(ad_se.data)
        return Response(ad_se.errors)

    if request.method == 'DELETE':
        advert.delete()
        return Response({
            'delete' : True
        })