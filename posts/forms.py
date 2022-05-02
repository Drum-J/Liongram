import imp
from sre_parse import CATEGORIES
from unicodedata import category
from django import forms
from .models import Post

# class PostBaseForm(forms.Form):
#     CATEGORY_CHOICES = [
#         ('1','일반'),
#         ('2','계정')
#     ]
#     iamge = forms.ImageField(label='이미지')
#     content = forms.CharField(label='내용', widget=forms.Textarea)
#     category = forms.ChoiceField(label='카테고리',choices=CATEGORY_CHOICES)

class PostBaseForm(forms.ModelForm):
    # forms.ModelForm 을 상속받을 때에는 class를 하나 더 만들어야 한다.
    class Meta :
        model = Post
        fields = '__all__'
        # models.py 의 Post class의 모든 필드가 적용이 된다.

from django.core.exceptions import ValidationError
class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields = ['iamge','content']
    
    def clean_content(self):
        data = self.cleaned_data['content']
        if '비속어' == data:
            raise ValidationError("'비속어'는 사용할 수 없습니다.")
        return data

class PostUpdateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields = ['iamge','content']

class PostDetailForm(PostBaseForm):
    def __init__(self,*args,**kwargs):
        super(PostDetailForm,self).__init__(*args,**kwargs)
        for key in self.fields:
            self.fields[key].widget.attrs['disabled']=True
            # detail.html에서 {{form.as_p}} 부분을 주석처리 해뒀음!