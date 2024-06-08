from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.i18n import set_language


from .forms import LoginForm


app_name = 'core'


urlpatterns = [
    path('', views.index, name='index'),
    # path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('profil/', views.profil, name='profil'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('editmail/', views.editEmail, name="editMail"),
    path('zmienhaslo', views.ChangePasswordView.as_view(), name='changePassword'),
    path('avatar/', views.profilePic, name="profilePic"),
    path('set_language/', views.SetLang.as_view(), name='set_language'),
]
