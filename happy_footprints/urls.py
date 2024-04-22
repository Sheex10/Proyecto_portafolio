from django.urls import path
from web_final import views
from .views import home



urlpatterns = [
    path('', home, name="home"),

]