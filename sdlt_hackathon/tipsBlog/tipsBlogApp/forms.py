from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = '__all__'

    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
      'author': forms.Select(attrs={'class': 'form-control'}),
      'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
      'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description of the tip(s)'}),
    
    }

class EditForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'title_tag', 'body')

    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
      'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description of the tip(s)'}),
    }