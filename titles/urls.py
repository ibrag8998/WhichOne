from django.urls import path

from . import views as v

app_name = 'titles'
urlpatterns = [
    path('', v.IndexView.as_view(), name='index'),
    path('pick/', v.PickView.as_view(), name='pick'),
    path('picked/', v.PickedView.as_view(), name='picked'),
]
