from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
from . models import Post

# Create your views here.
def index(request):
    return render(request,'post/index.html')

def create_post(request):
    if request.method=='POST':
        title=request.POST['title']
        description=request.POST['description']
        if (len(title)==0):
            messages.info(request,'title field cannot be empty')
            return render(request,'post/createpost.html',)
        elif (len(description)==0):
            messages.info(request,'description field cannot be empty',)
            return render(request,'post/createpost.html')
        else:
            post=Post.objects.create(title=title,description=description)
            post.save()
            return redirect('allpost')   
    else: 
        return render(request,'post/createpost.html')


def all_post(request):
    posts=Post.objects.all()
    return render(request,'post/allpost.html',{'posts':posts})
        
def single_post(request,id):
    post=Post.objects.get(id=id)
    return render(request,'post/singlepost.html',{'post':post})

def update_post(request,id):
    try:
        if request.method=='POST':
            post=Post.objects.get(id=id)
            if post is not None:
                title=request.POST['title']
                description=request.POST['description']
                if (len(title) !=0 and len(description) !=0):
                    post.title=title
                    post.description=description
                    post.save()
                    return redirect('http://127.0.0.1:8000/post/'+id)
                    # return render(request,'post/singlepost.html',{'post':post})
                else:
                    return render(request,'post/updatepost.html',{'id':id, 'post':post})
        else:
            post=Post.objects.get(id=id)
            return render(request,'post/updatepost.html',{'id':id, 'post':post})
    except Exception as e:
        return JsonResponse({'success':False, 'error':str(e)})
    
def delete_post(request,id):
    try:
        post=Post.objects.filter(id=id)
        print(post)
        if len(post) !=0:
            post.delete()
            return redirect('allpost')
        else:
            return JsonResponse({'success':False,'message':'Sorry, no record found'})
    except Exception as e:
        return JsonResponse({'success':False, 'error':str(e)})
    