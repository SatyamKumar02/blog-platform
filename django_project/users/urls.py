# urls.py inside each app

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # For login/logout

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.user_profile, name='user_profile'),
    path('signup/', views.signup, name='signup'),  # Add this
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
