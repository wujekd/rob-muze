from django.urls import path
from . import views

app_name = 'collabs'

urlpatterns = [
    path('', views.collabs, name='collabs'),
    path('<pk>', views.collab, name='collab'),
    path('<pk>/przeslij', views.przeslij, name='sub_collab'),
    path('<pk>/moderate', views.collab_moderate, name="collab_moderate"),
    path('<pk>/add-stage', views.add_stage, name='add_stage'),
    path('glosowanie/<pk>/check', views.vote, name='vote'),

    
    path('download/<int:pk>/', views.collab_pack_download, name='download_pack'),
]