from django.urls import path
from task_manager.first_hello.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]