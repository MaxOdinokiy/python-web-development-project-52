from django.urls import path
from task_manager.first_hello import views

urlpatterns = [
    path('', views.index)
]