from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('fests', views.fests, name='fests'),
    path('addfest', views.addfest, name='addfest'),
    path('events/<uuid:id>', views.events, name='events'),
    path('regevent/<uuid:id>', views.regevent, name='regevents'),
    path('getregevent', views.getregevent, name='getregevents'),
]

