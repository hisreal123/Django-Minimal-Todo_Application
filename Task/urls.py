from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='task-home'),
    path('delete/<str:pk>/', views.deleteTask, name='task-delete')
]
