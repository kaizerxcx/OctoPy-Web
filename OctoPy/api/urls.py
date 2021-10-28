from django.urls import path
from . import views

urlpatterns = [
	path('getUsers/', views.getAllUser, name="user-list"),
	path('verifyUser/<str:username>/<str:password>/', views.verifyUser, name="verify-user"),
	path('registerUser/<str:firstname>/<str:lastname>/<str:age>/<str:username>/<str:password>/', views.registerUser, name="register-user"),
]

