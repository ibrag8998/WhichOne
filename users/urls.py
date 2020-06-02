from django.urls import path

from . import views as v

app_name = 'users'
urlpatterns = [
    path('signup/', v.SignUpView.as_view(), name='signup'),
    path('signin/', v.SignInView.as_view(), name='signin'),
    path('logout/', v.LogOutView.as_view(), name='logout'),
]
