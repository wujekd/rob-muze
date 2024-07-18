from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.groups, name='groups'),
    path('<pk>', views.group, name="group"),
    path('verify/<pk>', views.verify_member, name="verify_member"),
    path('join_group/<pk>/', views.join_group, name='join_group'),
    
    
]