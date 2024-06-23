from django.urls import path
from . import views

app_name = 'ideas'

urlpatterns = [
    path('', views.ideas, name='ideas'),
    path('add', views.add_idea, name="add_idea")
    # path('<pk>', views.idea, name='collab'),
    # path('<pk>/przeslij', views.przeslij, name='sub_collab'),
    # path('glosowania/', views.votings, name='votings'),
    # path('glosowanie/<pk>', views.voting, name='voting'),
    # path('glosowanie/<pk>/check', views.vote, name='vote'),
    # path('download/<int:pk>/', views.collab_pack_download, name='download_pack'),
    
]