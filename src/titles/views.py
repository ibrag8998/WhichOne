from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from titles.models import Title
from titles.services import (
    IndexServiceMixin,
    PickServiceMixin,
    PickedServiceMixin,
)


class IndexView(IndexServiceMixin, ListView):
    model = Title
    template_name = 'titles/index.html'
    context_object_name = 'titles'


class PickView(LoginRequiredMixin, PickServiceMixin, ListView):
    model = Title
    template_name = 'titles/pick.html'
    context_object_name = 'titles'


class PickedView(LoginRequiredMixin, PickedServiceMixin, DetailView):
    model = Title


class AddView(LoginRequiredMixin, CreateView):
    model = Title
    template_name = 'titles/add.html'
    fields = ('text', )
    success_url = reverse_lazy('titles:add')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
