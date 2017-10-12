from django.views.generic import TemplateView,FormView
from django.http.response import HttpResponse
from .forms import LoginForm,RegisterForm
from django.views.generic import ListView,DetailView
from .models import Article
from django.conf import settings
from django import forms
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


from django.core.exceptions import ObjectDoesNotExist


class ArticleListView(ListView):
    template_name = 'app01/index.html'
    #context_object_name = 'article_list'

    page_type = ''
    paginate_by = settings.PAGINATE_BY
    page_kwarg = 'page'

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        article_list = Article.objects.all()
        paginator = Paginator(article_list, 5)
        page = self.request.GET.get('page')
        try:
            article_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            article_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            article_list = paginator.page(paginator.num_pages)
        context['article_list'] = article_list
        return context




class IndexView(ArticleListView):

    def get_queryset(self):
        article_list = Article.objects.all()
        return article_list


class RegisterView(FormView):
    template_name = 'app01/register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_invalid(self, form):
        form = RegisterForm(data=self.request.POST)

        return self.render_to_response({
            'form':form
        })

class LoginView(FormView):
    template_name = 'app01/login.html'
    form_class = LoginForm
    success_url = '/'

    def form_invalid(self, form):
        form = LoginForm(data=self.request.POST)

        return self.render_to_response({
            'form':form
        })



