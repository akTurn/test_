from django.urls import path
from .views import TodoList, TodoDetail, TodoReset

urlpatterns = [
    path('', TodoList.as_view(), name='todo-list'),
    path('api/todos/', TodoList.as_view(), name='todo-list'),
    path('api/todos/<int:pk>/', TodoDetail.as_view(), name='todo-detail'),
    path('api/todos/reset/', TodoReset.as_view(), name='todo-reset'),
]
