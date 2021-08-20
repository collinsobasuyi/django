from django.urls import path
from . import views
urlpatterns = [
    path('playgroug/hello', views.say_hello) 
]