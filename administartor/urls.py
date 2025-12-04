from django.urls import path, include
from django.contrib import admin
from . import views
from project import views  


urlpatterns = [
    path('',admin.site.urls),
    path('admin/logout/', views.logout, name='user_logout')
]