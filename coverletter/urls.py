from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.application_create, name='application-create'),
    path('application/<int:pk>', views.application_single, name='application'),
    path('applications/', views.application_list, name='application-list'),

]
