from django.urls import path
from . views import pfView
urlpatterns = [
    path("", pfView, name="store"),
]

