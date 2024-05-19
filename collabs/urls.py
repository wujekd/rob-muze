from django.urls import path
from . import views

app_name = 'collabs'

urlpatterns = [
    path('', views.collabs, name='collabs'),
    path('<pk>', views.collab, name='collab'),
    path('<pk>/przeslij', views.przeslij, name='sub_collab'),
    path('glosowania/', views.votings, name='votings'),
    path('glosowanie/<pk>', views.voting, name='voting'),
    path('glosowanie/<pk>/check', views.vote, name='vote'),
    
    path('download/<int:pk>/', views.collab_pack_download, name='download_pack'),
]