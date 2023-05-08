"""coverletter_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy, reverse
from coverletter.views import register
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('coverletter.urls')),
    path('register/', register, name='register'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='registration/password-change.html', success_url='password-change-done'), name='password-change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password-change-done.html'), name='password-change-done'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/password-reset.html', success_url='done'), name='password-reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password-reset-done.html'), name='password-reset-done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password-reset-confirm.html'), name='password-reset-confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password-reset-complete.html'), name='password-reset-complete'),
    path('', include('django.contrib.auth.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)