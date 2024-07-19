from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.groups, name='groups'),
    path('<pk>', views.group, name="group"),
    path('verify/<pk>', views.verify_member, name="verify_member"),
    path('request/<pk>/', views.join_group, name='join_group'),
    path('<int:pk>/invite/', views.create_invitation, name='create_invitation'),
    path('join/<str:token>/', views.join_group_with_token, name='join_group_with_token'),
    
    
]