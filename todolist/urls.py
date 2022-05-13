from django.urls import path, include
from . import views


app_name = 'todolist'

urlpatterns = [
    path('delete/<int:id>/', views.delete, name='delete_todo'),
    path('complete/<int:id>/', views.complete, name='completed_todo'),
    path('', views.todos, name='todos'),
]