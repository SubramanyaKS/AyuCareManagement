"""Ayucare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from AyucareApp.views import nhome, user_list
from django.contrib import admin
from django.urls import path,re_path
from AyucareApp.views import ayucare_detail,ayucare_list,ayucare_list_compound,purchased_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',nhome),
    re_path('^api/ayucare$', ayucare_list),
    re_path('^api/ayucare/(?P<pk>[0-9]+)$', ayucare_detail),
    re_path('^api/ayucare/compound$', ayucare_list_compound),
    re_path('^api/user$', user_list),
    re_path('^api/purchased/(?P<pk>[0-9]+)$', purchased_detail),
]