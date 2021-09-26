from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.shortcuts import render, redirect
from django.http import JsonResponse, response
from django.http import HttpResponse
from .models import *
from administrator.models import Administrator
import hashlib
# Create your views here.

class UserWelcomeView(View):

    def get(self, request):
        return render(request, 'user/index.html')
    def post(self, request):
        response_data = {}
        user_id = -1
        if request.POST.get('action') == 'registerUser':
            firstname = request.POST.get("firstname")
            lastname = request.POST.get("lastname")
            age = request.POST.get("age")
            username = request.POST.get("username")
            password = request.POST.get("password")
            md5pass = hashlib.md5(password.encode())
            password = md5pass.hexdigest()
            response_data['result'] = 'Create post successful!'
            response_data['firstname'] = firstname
            response_data['lastname'] = lastname
            response_data['age'] = age
            response_data['username'] = username
            response_data['password'] = password
            user = User.objects.create(firstname = firstname,lastname = lastname, age = age, username = username, password = password )
            # user.save()
            return JsonResponse(response_data)
        elif request.POST.get('action') == 'loginUser':
            username = request.POST.get('username')
            password = request.POST.get("password")
            md5pass = hashlib.md5(password.encode())
            password = md5pass.hexdigest()     
            response_data['username'] = username
            response_data['password'] = password
            response_data['status'] = -1
            users = User.objects.filter(username = username)
            for user in users:
                if password == user.password:
                    response_data['status'] = 0
                    user_id = user.user_id
            if Administrator.objects.filter(user_ptr_id=user_id).exists():
                response_data['status'] = 1
            request.session['user_id'] = user_id
            request.session['access_type'] = response_data['status'] 
            return JsonResponse(response_data)       
        else:
            return render(request, 'user/index.html')
class UserView(View):
    
    def get(self, request):
        user_id = -1
        access_type = -1
        if 'user_id' in request.session:
            user_id = request.session['user_id']
        if 'access_type' in request.session:
            access_type = request.session['access_type']
        if access_type == 0:
            return render(request, 'user/user.html')
        else:
            return HttpResponse('<br><h1 style="text-align:center;">Invalid Access Code</h1>')
    def post(self, request):
        response_data = {}
        if request.POST.get('action') == 'logout':
            del request.session['user_id']
            del request.session['access_type']
            response_data['status'] = 1
            return JsonResponse(response_data) 
        else:
            return HttpResponse('<br><h1 style="text-align:center;">Error Request</h1>')
