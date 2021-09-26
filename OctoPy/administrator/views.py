from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse
from .models import *
from administrator.models import Administrator
import hashlib
# Create your views here.

class AdministratorView(View):
    def get(self, request):
        user_id = -1
        access_type = -1
        if 'user_id' in request.session:
            user_id = request.session['user_id']
        if 'access_type' in request.session:
            access_type = request.session['access_type']
        if access_type == 1:
            return render(request,"admin/admin.html")
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