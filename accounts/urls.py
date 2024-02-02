from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('create/', views.create_view, name='create'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
]