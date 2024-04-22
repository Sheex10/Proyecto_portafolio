from django.urls import path

from web_final.happy_footprints.views import home



urlpatterns = [
    path('', home, name="home")
]