from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('ekstraklasa/', views.ekstraklasa, name='ekstraklasa'),
    path('liga1/', views.liga1, name='liga1'),
    path('liga2/', views.liga2, name='liga2'),
    path('liga3/', views.liga3, name='liga3'),
    path('liga4/', views.liga4, name='liga4'),
    path('liga5/', views.liga5, name='liga5'),
    path('liga6/', views.liga6, name='liga6'),
    path('liga7/', views.liga7, name='liga7'),
    ]
