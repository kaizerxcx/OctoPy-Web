from django.shortcuts import render
from user.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
import hashlib

# Create your views here.

@api_view(['GET'])
def getAllUser(request):
	user = User.objects.all()
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