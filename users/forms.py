from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.utils import AuthFormMixin

from users.models import User


class SignUpForm(AuthFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class SignInForm(AuthFormMixin, AuthenticationForm):
    pass
