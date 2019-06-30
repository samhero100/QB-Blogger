from django import forms

from .models import Comment ,Post

class NewComments(forms.ModelForm):
    class Meta:
        model= Comment
        fields =('name','email','body')

class PostCreatForm(forms.ModelForm):
    title=forms.CharField(label='عنوان التدوينة')
    content=forms.CharField(label='نص التدوينة', widget=forms.Textarea)
    class Meta:
        model = Post
        fields =['title','content']
        