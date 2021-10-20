from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/<int:id>', views.show_details),
    path('shows/<int:id>/edit', views.edit),
    path('shows/<int:id>/destroy', views.destroy),
    path('shows/<int:id>/update', views.update),
    path('shows/new', views.new),
    path('shows/create', views.create),
    path('title_valid/', views.title_valid_null),
    path('title_valid/<str:title>', views.title_valid),
]