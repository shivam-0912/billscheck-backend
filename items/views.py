from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from items.models import Item,User
from items.serializers import ItemSerializer,UserSerializer


@api_view(['GET', 'POST'])
def item_list(request,id, format=None):
    """
    List all code items, or create a new item.
    """
    if request.method == 'GET':
        user=User.objects.get(id=id)
        items = Item.objects.filter(user_id=user)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def item_detail(request,pk2, format=None):
    """
    Retrieve, update or delete a code item.
    """
    try:
        item = Item.objects.get(id=pk2)
    except item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


    
@api_view(['POST'])
def login(request, format=None):
    """
    List all code items, or create a new item.
    """
   
    try:
        user= User.objects.get(username=request.data['username'],password=request.data['password'])
    except user.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

      
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
def signup(request, format=None):
      if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
