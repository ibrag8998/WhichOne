from django.views.generic import ListView, DetailView

from titles import models as m
from titles import services as s


class IndexView(s.IndexServiceMixin, ListView):
    model = m.Title
    template_name = 'titles/index.html'
    context_object_name = 'titles'


class PickView(s.PickServiceMixin, ListView):
    model = m.Title
    template_name = 'titles/pick.html'
    context_object_name = 'titles'


class PickedView(s.PickedServiceMixin, DetailView):
    model = m.Title
