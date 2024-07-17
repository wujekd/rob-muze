from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.groups, name='groups'),
    path('<pk>', views.group, name="group"),
    
]