from django.urls import path

from users import views as v

app_name = 'users'
urlpatterns = [
    path('me/', v.MyProfileView.as_view(), name='my_profile'),
]
