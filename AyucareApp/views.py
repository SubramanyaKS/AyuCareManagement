from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from AyucareApp.models import Ayucare, Purchased, User
from AyucareApp.serializers import AyucareSerializer, UserSerializer
from AyucareApp.serializers import PurchasedSerializer
from rest_framework.decorators import api_view
from django.db.models import Q


# Create your views here.
def nhome(request):
    return render(request,"home.html")

#Views for Ayucare Product

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

@api_view(['GET'])
def ayucare_list_compound(request):
    ayucare = Ayucare.objects.all()
    productname=request.GET.get('productname',None)
    cure=request.GET.get('cure',None)
    ayucare = ayucare.filter(Q(productname_icontains=productname)&Q(cure_icontains=cure))
    if ayucare is not None:
        print(ayucare)
        if request.method=='GET':
            ayucare_serializer=AyucareSerializer(ayucare, many=True)
            return JsonResponse(ayucare_serializer.data,safe=False)

#User Views
@api_view(['GET','POST','DELETE'])
def user_list(request):
# GET list of User, POST a new User, DELETE all Users
    if request.method=='GET':
        user = User.objects.all()
        title =request.GET.get('username',None)
        if title is not None:
            user =user.filter(username__icontains=title)
            user_serializer=UserSerializer(user, many=True)
            return JsonResponse(user_serializer.data, safe=False)
    elif request.method=='POST':
        user_data=JSONParser().parse(request)
        user_serializer=UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        count =User.objects.all().delete()
        return JsonResponse({'message':'{} Product were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','PUT','DELETE'])
def user_detail(request, pk):
    # find User by pk (id)
    try:
        user = Purchased.objects.get(pk=pk)
        if request.method=='GET':
            user_serializer=UserSerializer(user)
            return JsonResponse(user_serializer.data)

        elif request.method == "PUT":
            user_data=JSONParser().parse(request)
            user_serializer=UserSerializer(User, data=user_data)
            if user_serializer.is_valid():
                user_serializer.save()
                return JsonResponse(user_serializer.data)
            return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method=='DELETE':
            User.delete()
            return JsonResponse({'message':'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    except User.DoesNotExist:
        return JsonResponse({'message':'The User does not exist'}, status=status.HTTP_404_NOT_FOUND)


#Purchased Views

@api_view(['GET','PUT','DELETE'])
def purchased_detail(request, pk):
    # find Ayucare by pk (id)
    try:
        purchased = Purchased.objects.get(pk=pk)
        if request.method=='GET':
            purchased_serializer=PurchasedSerializer(purchased)
            return JsonResponse(purchased_serializer.data)

        elif request.method == "PUT":
            purchased_data=JSONParser().parse(request)
            purchased_serializer=PurchasedSerializer(Purchased, data=purchased_data)
            if purchased_serializer.is_valid():
                purchased_serializer.save()
                return JsonResponse(purchased_serializer.data)
            return JsonResponse(purchased_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method=='DELETE':
            Purchased.delete()
            return JsonResponse({'message':'Purchased was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    except Purchased.DoesNotExist:
        return JsonResponse({'message':'The Purchased does not exist'}, status=status.HTTP_404_NOT_FOUND)