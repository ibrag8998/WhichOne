from django.urls import path

from .views import IndexView, PickView, PickedView, AddView

app_name = 'titles'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('pick/', PickView.as_view(), name='pick'),
    path('picked/', PickedView.as_view(), name='picked'),
    path('add/', AddView.as_view(), name='add'),
]
