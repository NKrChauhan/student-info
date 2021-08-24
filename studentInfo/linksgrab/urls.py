from .views import linkListView
from django.urls import path
app_name='linksgrab'
urlpatterns = [
    path('grabber/', linkListView, name="links")
]
