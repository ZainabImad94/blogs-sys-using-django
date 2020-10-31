from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Fieldset, HTML


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label='Email',
        max_length=254,
        widget=forms.TextInput(
            attrs={'placeholder': 'Search'}
        )
    )
    firstname = forms.CharField(label='First Name', max_length=40, required=True)
    lastname = forms.CharField(label='Last Name', max_length=40, required=False)

    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal container-fluid justify-content-center'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset("Sign Up",
                     'firstname',
                     'lastname',
                     'username',
                     'email',
                     'password1',
                     'password2',
                     Submit('Submit', 'Create New Account', css_class="btn-primary text-canter")
                     )
        )
