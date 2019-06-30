from django.shortcuts import render,redirect
from .forms import UserCreationForm,UserUpdateForm,ProfilUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate , login,logout
from blog.models import Post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# start register Form///////////////////////////////////////////////////////////////////////

def register(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            messages.success(request,f'تهانينا {new_user} لقد تمت عملية التسجيل بنجاح')
            return redirect('Login')
    else:
        form=UserCreationForm()
    return render(request,'register.html',{
        'title':'التسجيل',
        'form':form,
    })


# end register Form///////////////////////////////////////////////////////////////////////

# start Login Form ///////////////////////////////////////////////////////////////////////

def login_user(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request , username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            messages.warning(request ,'هناك خطأ في اسم المستخدم او كلمه المرور')
    return render(request,'Login.html',{
        'title':'تسجيل الدخول',
    })


# end Login Form ///////////////////////////////////////////////////////////////////////

# start logout Form ///////////////////////////////////////////////////////////////////////
def logout_user(request):
    logout(request)
    return render(request,'Logout.html',{
        'title':'تسجيل الخروج',
    })

# end logout Form ///////////////////////////////////////////////////////////////////////

# start profile ///////////////////////////////////////////////////////////////////////
@login_required(login_url='Login')
def profile(request):
    posts=Post.objects.filter(auther=request.user)
    post_list=Post.objects.filter(auther=request.user)
    paginator=Paginator(post_list,4)
    page=request.GET.get('page')
    try:
        post_list=paginator.page(page)
    except PageNotAnInteger:
        post_list=paginator.page(1)    
    except EmptyPage:    
        post_list=paginator.page(paginator.num_pages)  
    return render(request,'profile.html',{
        'title':'الملف الشخصي',
        'posts':posts,
        'post_list':post_list,
        'page':page,
    })

# end profile  ///////////////////////////////////////////////////////////////////////


# start profile_update  ///////////////////////////////////////////////////////////////////////
@login_required(login_url='Login')
def profile_update(request):
    if request.method == 'POST':
        user_form=UserUpdateForm(request.POST , instance=request.user)    
        profile_form=ProfilUpdateForm(request.POST ,request.FILES ,instance=request.user.profile)  
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            messages.success(request,f'تم تحديث الملف الشخصي')
            return redirect('profile')
    else:
        user_form=UserUpdateForm(instance=request.user)    
        profile_form=ProfilUpdateForm(instance=request.user.profile)  
    context={
        'title':'تعديل الملف الشخصي',
        'user_form':user_form,
        'profile_form':profile_form
    }
    return render(request,'profile_update.html',context)



# end profile_update  ///////////////////////////////////////////////////////////////////////    