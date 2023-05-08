from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('applications/', views.application_list, name='application-list'),
    path('application/create', views.application_create, name='application-create'),
]
