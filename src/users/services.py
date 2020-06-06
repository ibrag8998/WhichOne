from django.shortcuts import render


class MyProfileServiceMixin:
    def get(self, request):
        return render(request, self.template_name)
