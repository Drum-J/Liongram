from sre_parse import CATEGORIES
from unicodedata import category
from django import forms

class PostBaseForm(forms.Form):
    CATEGORY_CHOICES = [
        ('1','일반'),
        ('2','계정')
    ]
    iamge = forms.ImageField(label='이미지')
    content = forms.CharField(label='내용', widget=forms.Textarea)
    category = forms.ChoiceField(label='카테고리',choices=CATEGORY_CHOICES)