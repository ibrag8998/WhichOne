from django.contrib import messages
from django.shortcuts import redirect, render

from users.forms import SignUpForm


class SignUpViewMixin:
    def render_on_get(self, request, form):
        return render(request, self.template_name, {
            'form': form,
            'next': self.next
        })

    def get(self, request, *args, **kwargs):
        return self.render_on_get(request, SignUpForm())

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if not form.is_valid():
            for _, v in form.errors.items():
                for err in v:
                    messages.error(request, err)
            return self.render_on_get(request, form)

        form.save()

        return redirect(request.POST.get('next', next))
