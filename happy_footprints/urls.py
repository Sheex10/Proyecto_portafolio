from django.urls import path
from happy_footprints import views
from .views import home



urlpatterns = [
    path('', home, name="home"),

]