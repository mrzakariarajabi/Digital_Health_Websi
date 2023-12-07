"""
URL configuration for digweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views
##import views
app_name = "digital"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('zakaria/', views.zakaria, name="zakaria"),
    path('', views.mainpage, name="main"),
    path('about/', views.about_page, name="about_page"),
    path('appointment/', views.appointment_page, name="appointment_page"),
    path('service/', views.service_page, name="service_page"),
    path('diabetes/', views.diabetes_page, name="diabetes_page")
]
