
from django.urls import path

from . import views
from .views import HomePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login', views.signin),
    path('home', HomePageView.as_view()),
    path('login_page', views.signin),
    ]
