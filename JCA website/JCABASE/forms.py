from django.forms import ModelForm
from django import forms
from .models import *


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = '__all__'


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'


class ContactForm(forms.Form):
    yourname = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(required=False,label='Your e-mail address')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)



