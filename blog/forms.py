from django import forms
from .models import Blog
# from django.contrib.auth.forms import UserCreationForm
# from django.core.exceptions import ValidationError
# from django.contrib.auth.models import User

class ComposeBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('subject', 'body', 'recipient')