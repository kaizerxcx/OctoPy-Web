from django.urls import path
from . import views

urlpatterns = [
	path('getAllUser/', views.getAllUser, name="users-list"),
	path('getUser/<str:pk>/', views.getUser, name="user-info"),
	path('verifyUser/<str:username>/<str:password>/', views.verifyUser, name="verify-user"),
	path('registerUser/<str:firstname>/<str:lastname>/<str:age>/<str:username>/<str:password>/', views.registerUser, name="register-user"),
	path('updateUser/<str:user_id>/<str:firstname>/<str:lastname>/<str:age>/<str:username>/<str:password>/', views.updateUser, name="update-user"),
	path('deleteUser/<str:user_id>/', views.deleteUser, name="delete-user"),
]

