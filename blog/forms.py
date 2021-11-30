from django import forms
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.utils.translation import gettext, gettext_lazy as _

from django.contrib.auth.models import User
from .models import AddPost,AddComment,ContactUs

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User

        fields = ['username','first_name','last_name','email']
        labels = {'first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets ={'username': forms.TextInput(attrs={'class': 'form-control'}),
                  'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                  'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                  'email': forms.EmailInput(attrs={'class': 'form-control'}),

        }
class Login(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomlete':'current-password','class':'form-control'}))


class AddNewPost(forms.ModelForm):
    class Meta:
        model = AddPost
        fields = ['title','pst']
        labels = {'title':'Title','pst':'Post'}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),'pst':forms.Textarea(attrs={'class':'form-control'}),}


class AddNewComments(forms.ModelForm):
    class Meta:
        model=AddComment
        fields = ['comment',]
        widgets = {'comment': forms.TextInput(attrs={'class': 'form-control'}),}


class ContactPage(forms.ModelForm):
    class Meta:
        model = ContactUs

        fields = ['name','email','phone','desc']
        labels = {'name':'Full Name','email':'Email','phone':'Mobile','desc':'Description'}
        widgets ={'name': forms.TextInput(attrs={'class': 'form-control'}),
                  'desc': forms.Textarea(attrs={'class': 'form-control'}),
                  'phone': forms.TextInput(attrs={'class': 'form-control','type':'phone'}),
                  'email': forms.EmailInput(attrs={'class': 'form-control'}),
                  }