from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime

RADIO_CHOICES = (
    ('1', 'Radio 1'),
    ('2', 'Radio 2'),
)

MEDIA_CHOICES = (
    ('Audio', (
        ('vinyl', 'Vinyl'),
        ('cd', 'CD'),
    )),
    ('Video', (
        ('vhs', 'VHS Tape'),
        ('dvd', 'DVD'),
    )),
    ('unknown', 'Unknown'),
)


class RegisterForm(forms.Form):



    username = forms.CharField(min_length=5,
                               max_length=10,
                               error_messages={'required': "入力必須",'min_length': "不得少于3个字"}
                               )

    password = forms.CharField(widget=forms.PasswordInput)
    birth = forms.DateField()
    datetime = forms.SplitDateTimeField(widget=AdminSplitDateTime(), required=False)
    select1 = forms.ChoiceField(choices=RADIO_CHOICES)
    select2 = forms.MultipleChoiceField(
        choices=RADIO_CHOICES,
        help_text='Check as many as you like.',
    )
    select3 = forms.ChoiceField(choices=MEDIA_CHOICES)
    select4 = forms.MultipleChoiceField(
        choices=MEDIA_CHOICES,
        help_text='Check as many as you like.',
    )



class LoginForm(forms.Form):

    # error_messages={'required': '入力必須', 'min_length': '不得少于3个字', 'max_length': '不得多于10个字'},
    # error_messages={'required': '入力必須'},
    # error_messages={'required': '必须有输入值'},
    #help_text='enter your name',
    username = forms.CharField(min_length=5,
                               max_length=10,
                               error_messages={'required': "入力必須",'min_length': "不得少于3个字"}
                               )

    password = forms.CharField(widget=forms.PasswordInput)




    required_css_class = 'bootstrap3-req'

    use_required_attribute = False


    # def clean(self):
    #     cleaned_data = super(LoginForm, self).clean()
    #
    #     raise forms.ValidationError(self.error_messages['min_length'])
    #
    #     return cleaned_data

