from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user/register', views.create_user),
    path('user/login', views.login_user),
    path('success', views.success),
    path('user/logout', views.logout)
]