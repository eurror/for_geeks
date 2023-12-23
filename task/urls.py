from django.urls import path
from .views import TaskViewSet


app_name = 'task'
urlpatterns = [
    path('tasks/', TaskViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('tasks/<int:pk>/', TaskViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy', 'post': 'create'})),
]
