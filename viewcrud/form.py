from django import forms
from .models import Blog
from .models import Portfolio
class NewBlog(forms.ModelForm):
    class Meta:
        model=Blog
        #fields='__all__'
        fields=['title','body']

class NewPortfolio(forms.ModelForm):
    class meta:
        model=Portfolio
        fields='__all__'