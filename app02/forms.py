from django import forms
from django.forms import BaseFormSet
from django.forms import formset_factory
import datetime
from .models import Author,Book

class ArticleForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()


class BaseArticleFormset(BaseFormSet):
    def clean(self):

        if any(self.errors):
            return

        titles = []

        for form in self.forms:
            title = form.cleaned_data['title']

            if title in titles:
                raise forms.ValidationError('Articles in a set must have distinct title.')
            titles.append(title)




# ArticleFormSet = formset_factory(ArticleForm,formset=BaseArticleFormset)
# #formset = ArticleFormSet(initial=[{'title':'django is now open source','pub_date':datetime.date.today()}])
#
# data = {
#     'form-TOTAL_FORMS': '2',
#     'form-INITIAL_FORMS': '0',
#     'form-MAX_NUM_FORMS': '',
#     'form-0-title':'Test',
#     'form-0-pub_date':'2017/10-12',
#     'form-1-title':'Test',
#     'form-1-pub_date':'2017-10-13'
# }
# formset = ArticleFormSet(data)
#
# def print_formset():
#     for form in formset:
#         print(form.as_table())

class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['name','title','birth_date']

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['name','authors']
