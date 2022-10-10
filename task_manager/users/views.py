from django.views.generic import ListView
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy
#from task_manager.users.models import User

# Create your views here.
class UsersView(ListView):
    template_name = 'users/users.html'
    model = User
    context_object_name = 'users'


    def get_context_data(self, **kwargs):
        '.'
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Users')
        return context
