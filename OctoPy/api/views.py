from django.core.serializers import serialize
from django.shortcuts import render
from user.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
import hashlib
from django.core import serializers
from django.http import HttpResponse

# Create your views here.

@api_view(['GET'])
def getAllUser(request):
	user = User.objects.all()
	serializer = UserSerializer(user, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def getUser(request, pk):
	user = User.objects.filter(user_id=pk)
	serializer = UserSerializer(user, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def verifyUser(request, username, password):
    user_id = -1
    md5pass = hashlib.md5(password.encode())
    password = md5pass.hexdigest()
    now = datetime.now()
    users = User.objects.filter(username = username)
    for user in users:
        if password == user.password:
            user_id = user.user_id
    # if User.objects.filter(user_id = user_id).exists():
    #     Login.objects.create(child_id_id = user_id, lastLogin= now.strftime('%I:%M %p'))
    return Response(user_id)

@api_view(['POST'])
def registerUser(request, firstname, lastname, age, username, password):
    md5pass = hashlib.md5(password.encode())
    password = md5pass.hexdigest()
    user = Child.objects.create(firstname = firstname,lastname = lastname, age = age, username = username, password = password)
    Points.objects.create(child_id_id = user.child_id)
    return Response("ok")

@api_view(['POST'])
def updateUser(request, user_id, firstname, lastname, age, username, password):
    str = password
    md5pass = hashlib.md5(password.encode())
    password = md5pass.hexdigest()
    if str:
        update = User.objects.filter(user_id = user_id).update(firstname = firstname, lastname = lastname, age = age, username = username, password = password)
    else:
        update = User.objects.filter(user_id = user_id).update(firstname = firstname, lastname = lastname, age = age, username = username)
    user = User.objects.filter(user_id= user_id)
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def deleteUser(request, user_id):
    update = User.objects.filter(user_id = user_id).delete()
    return Response("deleted")