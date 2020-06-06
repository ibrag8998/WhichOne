from django.views.generic import View

from users.models import User
from users.services import MyProfileServiceMixin


class MyProfileView(MyProfileServiceMixin, View):
    model = User
    template_name = 'users/my_profile.html'
