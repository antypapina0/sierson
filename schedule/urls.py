from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.schedule, name='schedule'),
]