from django.contrib import admin
from django.urls import include, path
from . import views
app_name = 'user'
urlpatterns = [

  path("", views.UserWelcomeView.as_view(), name="user_welcome_view"),
  path("user", views.UserView.as_view(), name="user_view"),
  path("logout", views.UserWelcomeView.as_view(), name="user_welcome_view"),
]
