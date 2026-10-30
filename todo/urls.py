from django.urls import path
from . import views


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.task_add, name='task_add'),
    path('<int:task_id>/', views.task_detail, name='task_detail'),
    path('<int:task_id>/delete/', views.task_delete, name='task_delete'),
    path('<int:task_id>/update/', views.task_update, name='task_update'),
]
