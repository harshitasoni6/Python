from django.shortcuts import render,get_object_or_404

# Create your views here.

from blog.models import Post
def allpost(request):
    post = Post.objects
    return render(request,'posts.html',{'post':post})
def detail(request,blog_id):
    detail = get_object_or_404(Post,pk = blog_id)
    return render(request,'details.html',{'post':detail})

