from django.urls import path
from . import views

urlpatterns = [
    path('', views.fests, name='fests'),
]

