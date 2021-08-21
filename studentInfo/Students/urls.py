from django.contrib import admin
from django.urls import path
from .views import home,detail,delete,edit,create,detail, search

app_name = 'Students'
urlpatterns = [
    path('',home.as_view(),name="home"),
    path('search/',search.as_view(),name="search"),
    path('create/',create,name="create"),
    path('delete/<roll>/',delete,name="delete"),
    path('edit/<roll>/',edit,name="edit"),
    path('detail/<roll>/',detail,name="detail"),
] 
