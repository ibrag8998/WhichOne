from django.shortcuts import redirect
from django.contrib import messages

from titles.models import Title


class IndexServiceMixin:
    model = None

    def get_queryset(self):
        return self.model.objects.all()


class PickServiceMixin:
    model = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.all_titles = self.model.objects.all()

    def get(self, request, *args, **kwargs):
        """ In case there less than 10 titles in whole database, user should
        be redirected to index page and flash message will be sent
        """
        if self.all_titles.count() < 10:
            messages.info(request,
                          'Sorry, there are no enough titles in database :(')
            return redirect('titles:index')

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        """ Return two random titles for user to pick one """
        two_random = self.all_titles.random(2)
        for t in two_random:
            t.appearances += 1
            t.save()
        return two_random


class PickedServiceMixin:
    # Where to redirect user if he trying to send GET request or there are no
    # 'picked' key in request.POST, which normally should be specified by
    # hidden input
    redirect_to = 'titles:index'

    def get(self, request, *args, **kwargs):
        return redirect(self.redirect_to)

    def post(self, request, *args, **kwargs):
        pk = request.POST.get('picked')
        if pk is None:
            return redirect(self.redirect_to)

        t = Title.objects.get(pk=pk)
        t.picks += 1
        t.save()

        u = request.user
        u.picks.add(t)
        u.save()

        return redirect('titles:pick')


def add_sample_titles(n=10):
    for i in range(1, n + 1):
        Title.objects.create(text=f'Sample title #{i}')
