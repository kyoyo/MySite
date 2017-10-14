from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from .forms import AuthorForm,BookForm
from django.core.urlresolvers import reverse

# Create your views here.


class AuthorCreateView(FormView):
    template_name = 'app02/index.html'
    form_class = AuthorForm

    def form_valid(self, form):
        form = AuthorForm(self.request.POST)
        form.save()

        is_save = True
        return self.render_to_response({
            'form':form,
            'is_save':is_save
        })

class BookCreateView(FormView):
    template_name = 'app02/index.html'
    form_class = BookForm

    def form_valid(self, form):
        form = BookForm(self.request.POST)

        return self.render_to_response({
            'form':form
        })
