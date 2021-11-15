from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.shortcuts import render, redirect
from django.http import JsonResponse, response
from django.http import HttpResponse
from administrator.models import Administrator
import hashlib
from .forms import FeedbackForm
from .models import *
# Create your views here.

class UserWelcomeView(View):

    def get(self, request):
        return render(request, 'user/index.html')
    def post(self, request):
        response_data = {}
        user_id = -1
        form = FeedbackForm(request.POST)
        if request.POST.get('action') == 'registerUser':
            firstname = request.POST.get("firstname")
            lastname = request.POST.get("lastname")
            age = request.POST.get("age")
            username = request.POST.get("username")
            password = request.POST.get("password")
            email = request.POST.get("email")
            md5pass = hashlib.md5(password.encode())
            password = md5pass.hexdigest()
            response_data['result'] = 'Create post successful!'
            response_data['firstname'] = firstname
            response_data['lastname'] = lastname
            response_data['age'] = age
            response_data['username'] = username
            response_data['password'] = password
            now = datetime.now()
            user = Child.objects.create(firstname = firstname,lastname = lastname, age = age, username = username, email = email, password = password)
            Points.objects.create(child_id_id = user.child_id)
            # user.save()
            return JsonResponse(response_data)
        elif request.POST.get('action') == 'checkUsername':
            user = request.POST.get("username")
            response_data['status'] = 1
            try:
                test = User.objects.get(username=user)
            except User.DoesNotExist:
                response_data['status'] = 0
            return JsonResponse(response_data)

        elif request.POST.get('action') == 'checkEmail':
            email = request.POST.get("email")
            response_data['status'] = 1
            try:
                test = User.objects.get(email=email)
            except User.DoesNotExist:
                response_data['status'] = 0
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
            if Administrator.objects.filter(child_id_id = user_id).exists():
                response_data['status'] = 1
            now = datetime.now()
            if User.objects.filter(user_id = user_id).exists():
                login = Login.objects.create(child_id_id = user_id, lastLogin= now.strftime('%I:%M %p'))
            request.session['user_id'] = user_id
            request.session['access_type'] = response_data['status'] 
            return JsonResponse(response_data) 
        elif form.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            subject = request.POST.get("subject")
            feedback = request.POST.get("feedback")
            
            form = Feedback.objects.create(name = name, email = email, subject = subject, feedback = feedback)
            form.save()
            return redirect('user:user_welcome_view')

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
            users = User.objects.raw("SELECT * FROM user JOIN child ON user.user_id = %s", [user_id])
            requests = Request.objects.raw("SELECT * FROM request WHERE child_id_id = %s", [user_id])
            notifications = Notification.objects.raw("SELECT * FROM notification WHERE receiver = %s", [user_id])
            isRequested = True
            if not requests:
                isRequested = False
            context={
                'user_id': user_id,
                'users': users,
                'requests': requests,
                'isRequested': isRequested,
                'notifications': notifications,
            }
            return render(request, 'user/user.html', context)
        else:
            return HttpResponse('<br><h1 style="text-align:center;">Invalid Access Code</h1>')
    def post(self, request):
        response_data = {}
        if request.POST.get('action') == 'logout':
            del request.session['user_id']
            del request.session['access_type']
            response_data['status'] = 1
            return JsonResponse(response_data) 
        elif request.POST.get('action') == 'requestAdmin':
            user_id = request.POST.get("user_id")
            users = Child.objects.filter(user_ptr_id = user_id)
            content = "Request for Administrator Account"
            for user in users:
                notif_content = user.firstname+" sent you a request"
            Request.objects.create(child_id_id = user_id, content = content)
            admin_receive = -1
            Notification.objects.create(sender_id = user_id, content = notif_content, receiver = admin_receive)
            response_data['status'] = 1
            return JsonResponse(response_data) 
        elif request.POST.get('action') == 'notificationRead':
            notification_id = request.POST.get("notification_id")
            Notification.objects.filter(notification_id = notification_id).delete()
            response_data['status'] = 1
            return JsonResponse(response_data)
        elif 'user-update' in request.POST:
            updateId = request.POST.get("user-id")
            updateFirstname = request.POST.get("user-firstname")
            updateLastname = request.POST.get("user-lastname")
            updateAge = request.POST.get("user-age")
            password = request.POST.get("user-password")
            md5pass = hashlib.md5(password.encode())
            updatePassword = md5pass.hexdigest()                    
            # updateUsername = request.POST.get("user-username")       
            updateUser = User.objects.filter(user_id = updateId).update(firstname = updateFirstname, lastname = updateLastname, age = updateAge, password = updatePassword)
            print(updateUser)
            return redirect('user:user_view')
        elif 'user-delete' in request.POST:
            deleteId = request.POST.get("user-idDelete")
            deleteUser = User.objects.filter(user_id= deleteId).delete()            
            return redirect('user:user_welcome_view')
        else:
            return HttpResponse('<br><h1 style="text-align:center;">Error Request</h1>')
		
class YoutubeView(View):
	def get(self, request):
		return render(request,'user/youtube.html')
	def post(self, request):
		response_data = {}
		if request.POST.get('action') == 'logout':
			del request.session['user_id']
			del request.session['access_type']
			response_data['status'] = 1
			return JsonResponse(response_data)

