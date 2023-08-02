from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


# from .forms import LoginForm

app_name = 'ankiety'

urlpatterns = [
    path('', views.ankiety, name='ankiety'),
    path('<int:pk>/', views.ankietaotw, name='ankietaotw'), 
    
]
