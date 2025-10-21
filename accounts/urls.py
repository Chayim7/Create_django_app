from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('profile/', views.profile_view, name='profile'),
    path('u/<str:username>/', views.profile_other, name='profile_other'),
    path('u/<str:username>/follow/', views.follow_toggle, name='follow_toggle'),
    path('search/users/', views.user_search, name='user_search'),
]

