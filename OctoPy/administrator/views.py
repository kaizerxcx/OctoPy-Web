from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.shortcuts import render, redirect
from django.http import JsonResponse, response
from django.http import HttpResponse
from .models import *
from user.models import *
from administrator.models import Administrator
import pandas as pd
import numpy as np
import hashlib
from datetime import datetime
from dateutil import parser

# Create your views here.

class AdministratorView(View):
    def get(self, request):
        user_id = -1
        access_type = -1
#        feedbacks = Feedback.objects.all()
#       users = User.objects.all()
#        context = {
#            'feedbacks' : feedbacks
#        }
        if 'user_id' in request.session:
            user_id = request.session['user_id']
        if 'access_type' in request.session:
            access_type = request.session['access_type']
        if access_type == 1:
            users = User.objects.raw("SELECT * FROM user JOIN child ON user.user_id = %s", [user_id])
            notifications = Notification.objects.raw("SELECT * FROM notification WHERE receiver = -1 AND isRead = 0 AND sender_id != %s", [user_id])
            requests = Request.objects.raw("SELECT * FROM request JOIN user ON request.child_id_id = user.user_id AND request.status != 'Approved' AND request.status != 'Rejected' ")
            item = Login.objects.all().values()
            df = pd.DataFrame(item)
            peak = df['lastLogin'].value_counts()
            dates = df['datetime'].values
            DATE = [ parser.parse(str(x)) for x in dates]
            months = [x.strftime("%B") for x in DATE]
            df['months'] = months
            months = df['months'].value_counts()
            userss = User.objects.all()
            user_values = User.objects.all().values()
            df2 = pd.DataFrame(user_values)
            age = df2['age'].value_counts()
            points_value = Points.objects.all().values()
            df3 = pd.DataFrame(points_value)
            df4 = pd.DataFrame([[df3["crazeOnPhonicPoints"].sum(),df3["wordKitPoints"].sum(),df3["alphaHopperPoints"].sum(), df3["mazeCrazePoints"].sum(), df3["readingSpreePoints"].sum() ]], columns = ["Craze on Phonics", "WordKit", "Alpha Hopper", "Maze Craze", "Reading Spree"])
            feedbacks = Feedback.objects.all()
            user_point = User.objects.raw("SELECT * FROM user JOIN points on user.user_id = points.child_id_id")
            leaderboard = pd.DataFrame([item.__dict__ for item in user_point])
            leaderboard['Total'] = leaderboard['crazeOnPhonicPoints'] + leaderboard['wordKitPoints'] + leaderboard['alphaHopperPoints'] + leaderboard['mazeCrazePoints'] + leaderboard['readingSpreePoints']
            leaderboard.drop(['_state', 'password'], axis=1, inplace=True)
            leaderboard['Rank'] = leaderboard['Total'].rank(ascending=False)
            leaderboard = leaderboard.sort_values('Rank')
            leaderboard = leaderboard[:5]
            context = {
                'user_id': user_id,
                'users' : users,
                'notifications': notifications,
                'requests': requests,
                'labels': df['lastLogin'].values,
                'peak': peak.to_json(),
                'months': months.to_json(),
                'age': age.to_json(),
                'points':df4.to_json(orient='records'),
                'userss' : userss,
                'feedbacks' : feedbacks,
                'df5': leaderboard.to_json(orient='records'),
            }
            return render(request,"admin/admin.html", context)
        else:
            return HttpResponse('<br><h1 style="text-align:center;">Invalid Access Code</h1>')
    def post(self, request):
        response_data = {}
        if request.POST.get('action') == 'logout':
            del request.session['user_id']
            del request.session['access_type']
            response_data['status'] = 1
            return JsonResponse(response_data)
        elif request.POST.get('action') == 'notificationRead':
            notification_id = request.POST.get("notification_id")
            Notification.objects.filter(notification_id = notification_id).delete()
            response_data['status'] = 1
            return JsonResponse(response_data)
        elif request.POST.get('action') == 'requestAccepted':
            admin_id = request.POST.get("admin_id")
            users = Child.objects.filter(user_ptr_id = admin_id)
            user_id = request.POST.get("user_id")
            request_id = request.POST.get("request_id")
            Request.objects.filter(request_id = request_id).update(status = 'Approved')
            Administrator.objects.create(child_id_id = user_id)
            for user in users:
                notif_content = user.firstname+" approved your request"
                admin_id = user.user_ptr_id
            Notification.objects.create(sender_id = admin_id, receiver = user_id, content = notif_content)
            return redirect('administrator:administrator_view')  
        elif request.POST.get('action') == 'requestRejected':
            admin_id = request.POST.get("admin_id")
            users = Child.objects.filter(user_ptr_id = admin_id)
            user_id = request.POST.get("user_id")
            request_id = request.POST.get("request_id")
            Request.objects.filter(request_id = request_id).update(status = 'Rejected')
            for user in users:
                notif_content = user.firstname+" declined your request"
                admin_id = user.user_ptr_id
                Notification.objects.create(sender_id = admin_id, receiver = user_id, content = notif_content)
                response_data['status'] = 1
            return redirect('administrator:administrator_view')        
        elif 'user-update' in request.POST:
            updateId = request.POST.get("user-id")
            updateFirstname = request.POST.get("user-firstname")
            updateLastname = request.POST.get("user-lastname")
            updateAge = request.POST.get("user-age")
            updateUsername = request.POST.get("user-username")
            password = request.POST.get("user-password")
            md5pass = hashlib.md5(password.encode())
            updatePassword = md5pass.hexdigest()                     
            updateUser = User.objects.filter(user_id = updateId).update(firstname = updateFirstname, lastname = updateLastname, age = updateAge, username = updateUsername, password = updatePassword)
            print(updateUser)
            return redirect('administrator:administrator_view')     
        elif 'user-delete' in request.POST:
            deleteId = request.POST.get("user-idDelete")
            deleteUser = User.objects.filter(user_id= deleteId).delete()            
            return redirect('administrator:administrator_view')  
        elif 'feedback-delete' in request.POST:
            feedbackId = request.POST.get("feedback-idDelete")
            feedbackUSer = Feedback.objects.filter(feedback_id = feedbackId).delete()
            return redirect('administrator:administrator_view') 
        elif 'admin-delete' in request.POST:
            deleteId = request.POST.get("user-idDelete")
            deleteUser = User.objects.filter(user_id= deleteId).delete()            
            return redirect('user:user_welcome_view')
         
        else:
            return HttpResponse('<br><h1 style="text-align:center;">Error Request</h1>')