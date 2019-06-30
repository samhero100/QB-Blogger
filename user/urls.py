from django.urls import path
from .views import register,login_user,logout_user,profile,profile_update
from django.contrib.auth.views import LoginView,LogoutView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path ('register/',register,name='register' ),
    path ('Login/',login_user,name='Login'),
    path ('Logout/',logout_user,name='Logout' ),
    path ('profile/',profile,name='profile' ),
    path ('profile_update/',profile_update,name='profile_update' ),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 