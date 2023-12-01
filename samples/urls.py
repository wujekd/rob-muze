from django.urls import path
from . import views



app_name = 'samples'

urlpatterns = [
    path('', views.samples, name='samples'),
    path('download/<int:pk>/', views.download_file, name='download'),
    path('<int:pk>/', views.sample_detail, name='sampel'),
    path('message/', views.message, name='message')
]