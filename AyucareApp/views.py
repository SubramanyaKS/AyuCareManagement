from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from AyucareApp.models import Ayucare
from AyucareApp.serializers import AyucareSerializer
from rest_framework.decorators import api_view


# Create your views here.
def nhome(request):
    return render(request,"home.html")

@api_view(['GET','POST','DELETE'])
def ayucare_list(request):
# GET list of Ayucares, POST a new Ayucare, DELETE all Ayucares
    if request.method=='GET':
        ayucare = Ayucare.objects.all()
        title =request.GET.get('productname',None)
        if title is not None:
            ayucare =ayucare.filter(productname__icontains=title)
            ayucare_serializer=AyucareSerializer(ayucare, many=True)
            return JsonResponse(ayucare_serializer.data, safe=False)
    elif request.method=='POST':
        Ayucare_data=JSONParser().parse(request)
        ayucare_serializer=AyucareSerializer(data=Ayucare_data)
        if ayucare_serializer.is_valid():
            ayucare_serializer.save()
            return JsonResponse(ayucare_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(ayucare_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        count =Ayucare.objects.all().delete()
        return JsonResponse({'message':'{} Product were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','PUT','DELETE'])
def ayucare_detail(request, pk):
    # find Ayucare by pk (id)
    try:
        ayucare = Ayucare.objects.get(pk=pk)
        if request.method=='GET':
            Ayucare_serializer=AyucareSerializer(ayucare)
            return JsonResponse(Ayucare_serializer.data)

        elif request.method == "PUT":
            ayucare_data=JSONParser().parse(request)
            Ayucare_serializer=AyucareSerializer(Ayucare, data=ayucare_data)
            if Ayucare_serializer.is_valid():
                Ayucare_serializer.save()
                return JsonResponse(Ayucare_serializer.data)
            return JsonResponse(Ayucare_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        elif request.method=='DELETE':
            Ayucare.delete()
        return JsonResponse({'message':'Ayucare was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    except Ayucare.DoesNotExist:
        return JsonResponse({'message':'The Ayucare does not exist'}, status=status.HTTP_404_NOT_FOUND)



