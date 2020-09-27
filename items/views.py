from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from items.models import Item,User
from items.serializers import ItemSerializer,UserSerializer,LoginSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


test_param = openapi.Parameter('pk2', openapi.IN_QUERY, description="enter item id as pk2", type=openapi.TYPE_BOOLEAN)
user_response = openapi.Response('Response', ItemSerializer)

@swagger_auto_schema(method='get',responses={200: user_response})
# 'methods' can be used to apply the same modification to multiple methods
# @swagger_auto_schema(method='delete',request_body=None,)
@swagger_auto_schema(method='post', request_body=ItemSerializer)
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
    


# 'method' can be used to customize a single HTTP method of a view

@swagger_auto_schema(method='get',responses={200: user_response})
# 'methods' can be used to apply the same modification to multiple methods
@swagger_auto_schema(method='delete',request_body=None,)
@swagger_auto_schema(method='put', request_body=ItemSerializer)
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
    

user_response = openapi.Response('Response', UserSerializer)
@swagger_auto_schema(method='post', request_body=LoginSerializer,responses={200: user_response})
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

@swagger_auto_schema(method='post', request_body=UserSerializer)
@api_view(['POST'])
def signup(request, format=None):
      if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
