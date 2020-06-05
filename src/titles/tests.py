from django.test import TestCase
from django.urls import reverse

from titles import models as m


def add_title(**kwargs):
    if kwargs.get('text') is None:
        kwargs['text'] = 'test'
    return m.Title.objects.create(**kwargs)


class IndexViewTests(TestCase):
    url = reverse('titles:index')

    def test_no_titles(self):
        """ Special message should appear """
        resp = self.client.get(self.url)
        self.assertContains(resp, 'There are no questions')

    def test_titles_appearance(self):
        """ Titles should appear on index page """
        add_title()
        resp = self.client.get(self.url)
        self.assertContains(resp, 'test')


class PickViewTests(TestCase):
    url = reverse('titles:pick')

    def test_no_titles(self):
        """ Redirect to index page """
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 302)

    def test_enough_titles(self):
        """ Status code 200 """
        for i in range(10):
            add_title(text=f'test{i}')
        resp = self.client.get(self.url)

        self.assertEqual(resp.status_code, 200)
