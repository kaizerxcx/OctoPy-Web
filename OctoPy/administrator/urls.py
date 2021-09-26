from django.contrib import admin
from django.urls import include, path
from . import views
app_name = 'administrator'
urlpatterns = [
  path("administrator", views.AdministratorView.as_view(), name="administrator_view"),
]