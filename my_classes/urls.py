"""my_classes URL Configuration

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
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from classes.views import ClassViewSet
from students.views import StudentViewSet
from sports.views import SportViewSet
from plans.views import PlanViewSet

router = routers.DefaultRouter()
router.register(r"aulas", ClassViewSet, basename="Class")
router.register(r"estudantes", StudentViewSet, basename="Student")
router.register(r"esportes", SportViewSet, basename="Sport")
router.register(r"planos", PlanViewSet, basename="Plan")

urlpatterns = [path("admin/", admin.site.urls), path("", include(router.urls))]
