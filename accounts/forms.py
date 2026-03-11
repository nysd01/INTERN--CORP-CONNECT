
from django import forms
from .models import CompanyProfile, InternProfile

class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ['name', 'description', 'website', 'photo', 'address']

class InternProfileForm(forms.ModelForm):
    class Meta:
        model = InternProfile
        fields = ['domain', 'resume', 'bio', 'photo', 'address']
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class RegisterForm(UserCreationForm):
    USER_TYPE_CHOICES = (
        ('intern', 'Intern'),
        ('company', 'Company'),
    )
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ('username', 'email', 'user_type', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
