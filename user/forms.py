from django import forms
from django.contrib.auth.models import User
from .models import Profile
class UserCreationForm(forms.ModelForm):
    username=forms.CharField(label='اسم المستخدم', max_length=30,help_text='اسم المستخدم يجب الا يحتوي على مسافات')
    email=forms.EmailField(label='البريد الالكتروني')
    first_name=forms.CharField(label='الاسم الاول')
    last_name=forms.CharField(label='الاسم الاخير')
    password1=forms.CharField(label='كلمه المرور',widget=forms.PasswordInput(),min_length=8)
    password2=forms.CharField(label='تاكيد كلمه المرور  ',widget=forms.PasswordInput(),min_length=8)
    class Meta:
        model=User
        fields=('username','email','first_name','last_name','password1','password2')
    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('كلمه المرور غير متطابقة')
        return cd['password2']    
    def clean_username(self):
        cd=self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('يوجد مستخدم مسجل بهذا الاسم')
        return cd['username']       

class UserUpdateForm(forms.ModelForm):
    first_name=forms.CharField(label='الاسم الاول')
    last_name=forms.CharField(label='الاسم الاخير')
    email=forms.EmailField(label='البريد الالكتروني')
    class Meta:
        model = User
        fields=('username','first_name','last_name','email')
class ProfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=('image',)        

