from django.urls import path
from task_manager.users.views import UsersView

app_name = 'users'

urlpatterns = [
    path('', UsersView.as_view(), name='users')
]
