from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('fests', views.fests, name='fests'),
    path('addfest', views.addfest, name='addfest'),
    path('login', views.login, name='login'),
]

