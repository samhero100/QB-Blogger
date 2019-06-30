from django.shortcuts import render ,get_object_or_404
from .models import Post,Comment
from .forms import NewComments,PostCreatForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import CreateView,UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
# start index.html////////////////////////////////////////
def home(request):
    posts=Post.objects.all()
    paginator=Paginator(posts,4)
    page=request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)    
    except EmptyPage:    
        posts=paginator.page(paginator.num_pages) 
    context={
        'title':'الصفحه الرئيسية',
        'posts':posts,
        'page':page,
    }
    return render(request,'index.html',context)
# end index.html/////////////////////////////////

# start about.html////////////////////////////////////////

# start  detail.html////////////////////////////////////////
@login_required(login_url='Login')
def posts_detail(request,post_id):
    post=get_object_or_404(Post,pk=post_id)
    comments= post.comments.filter(active=True)
#check before save data from comment form
    if request.method=='POST':
            comment_form=NewComments(data=request.POST)
            if comment_form.is_valid():
                new_comment= comment_form.save(commit=False)
                new_comment.post=post
                new_comment.save()
                comment_form=NewComments()
    else:
            comment_form=NewComments()  
    context={
        'title':post,
        'post':post,
        'comments':comments,
        'comment_form':comment_form,
    }
    
    return render(request,'detail.html',context)
# end detail.html////////////////////////////////////////


# start Post Create////////////////////////////////////////
class PostCreateView(LoginRequiredMixin , CreateView):
    model=Post
    template_name='new_post.html'
    form_class=PostCreatForm
    def form_valid(self,form):
        form.instance.auther=self.request.user
        return super().form_valid(form)
# end Post Create/////////////////////////////////////////


# start Post Update////////////////////////////////////////
class PostUpdateView(UserPassesTestMixin,LoginRequiredMixin , UpdateView):
    model=Post
    template_name='post_update.html'
    form_class=PostCreatForm
    def form_valid(self,form):
        form.instance.auther=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()    
        if self.request.user == post.auther:
            return True
        else:
            return False    
# end Post Update/////////////////////////////////////////


# STRAT Post Delete/////////////////////////////////////////
class PostDeleteView(UserPassesTestMixin,LoginRequiredMixin ,DeleteView):
    model= Post
    template_name='post_confirm_delete.html'
    success_url = '/'
    def test_func(self):
        post=self.get_object()    
        if self.request.user == post.auther:
            return True
        return False 
# end Post Delete/////////////////////////////////////////