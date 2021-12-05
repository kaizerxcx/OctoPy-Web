from django.urls import path
from . import views

urlpatterns = [
	path('getAllUser/', views.getAllUser, name="users-list"),
	path('getUser/<str:pk>/', views.getUser, name="user-info"),
	# path('verifyUser/<str:username>/<str:password>/', views.verifyUser, name="verify-user"),
	path('verifyUser/', views.verifyUser, name="verify-user"),
	# path('registerUser/<str:firstname>/<str:lastname>/<str:age>/<str:username>/<str:email>/<str:password>/', views.registerUser, name="register-user"),
	# path('updateUser/<str:user_id>/<str:firstname>/<str:lastname>/<str:age>/<str:username>/<str:email>/<str:password>/', views.updateUser, name="update-user"),
	path('updateUser/', views.updateUser, name="updateUser-user"),
	path('deleteUser/<str:user_id>/', views.deleteUser, name="delete-user"),
	path('getLeaderboard/', views.getLeaderboard, name="users-leaderboard"),
	path('getReward/<str:pk>/', views.getReward, name="users-reward"),
	path('checkUsername/<str:username>/', views.checkUsername, name="users-checkUsername"),
	path('checkEmail/<str:email>/', views.checkEmail, name="users-checkEmail"),
	path('getPercentile/<str:pk>/', views.getPercentile, name="users-getPercentile"),
	path('registerUser/', views.registerUser, name="register-user"),
	path('updatecrazeOnPhonicPoints/', views.updatecrazeOnPhonicPoints, name="user-updatecrazeOnPhonicPoints"),
	path('updatewordKitPoints/', views.updatewordKitPoints, name="user-updatewordKitPoints"),
	path('updatealphaHopperPoints/', views.updatealphaHopperPoints, name="user-updatealphaHopperPoints"),
	path('updatemazeCrazePoints/', views.updatemazeCrazePoints, name="user-updatemazeCrazePoints"),
	path('updatereadingSpreePoints/', views.updatereadingSpreePoints, name="user-updatereadingSpreePoints"),
]