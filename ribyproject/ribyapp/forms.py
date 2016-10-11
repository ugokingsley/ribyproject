from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model=Post
        fields=['name','email']

    def clean_email(self):
        email= self.cleaned_data.get('email')
        return email

    def clean_name(self):
        name=self.cleaned_data.get('name')
        return name





