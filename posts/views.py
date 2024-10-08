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
    
def delete_post(request):
    if request.method=='POST':
        id_post=request.POST['id']
        post=Post.objects.get(id=id_post)
        post.delete()
        messages.success(request,'ok done post deleted now')
        return redirect('/posts/')
    
def edit_post(request):
    if request.method=='POST':
        post_id=request.POST['id']
        post=Post.objects.get(id=post_id)
        user=request.user
        title=request.POST['title']
        content=request.POST['content']
       
        image=request.FILES['image'].name
     
        draft=request.POST['draft']
        category=request.POST['category']


        post.user=user
        post.title=title
        post.content=content
        if image:
            post.image=image
        post.draft=draft
        post.category_id=category

        post.save()


        messages.success(request,'ok done post EDIT now')
        return redirect('/posts/')


