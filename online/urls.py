from django.urls import path
from . views import storView
urlpatterns = [
    path("", storView,name="home")
]
