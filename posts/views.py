from django.shortcuts import render,redirect
from .models import Post,Category
from django.contrib import messages


def base(request):
    return render(request,'base.html',{})
def post_list(request):

    posts=Post.objects.all()
    category=Category.objects.all()
    context={
        'posts':posts,
        'category':category
    }
    return render(request,'posts/post_list.html',context)

def add_post(request):
    if request.method=='POST':
        user=request.user
        title=request.POST['title']
        content=request.POST['content']
       
        image=request.FILES['image'].name
     
        draft=request.POST['draft']
        category=request.POST['category']

        Post.objects.create(
            user=user,
            title=title,
            content=content,
           
            image=image,
            draft=draft,
            category_id=category
        )
        messages.success(request,'ok done post added now')
        return redirect('/posts/')
