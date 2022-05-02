from csv import writer
from multiprocessing import context
from re import template
import re
from sys import orig_argv
from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404, HttpResponse, JsonResponse
from django.views.generic.list import ListView
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostBaseForm,PostCreateForm,PostDetailForm
# Create your views here.
def index(request) :
    post_list = Post.objects.all().order_by('-created_at')
    context = {
        'post_list': post_list,
    }
    return render(request, 'index.html',context)
    
def post_list_view(request) :
    post_list = Post.objects.all() #Post 전체 데이터 조회
    # post_list = Post.objects.filter(writer=request.user) #Post.writer가 현재 로그인인 것 조회
    context = {
        'post_list': post_list,
    }
    return render(request, 'posts/post_list.html',context)

def post_detail_view(request, id) :

    try :
        post = Post.objects.get(id=id) # 하나만 불러올거기 때문에 get 으로 불러온다.
    except Post.DoesNotExist:
        return redirect('index') # 주소에 id값을 다른걸 입력하게 되면 index로 넘어간다. - 에러가 나지 않게 하는 것
    context = {
        'post' : post,
        'form' : PostDetailForm,
    }
    return render(request, 'posts/post_detail.html', context)

@login_required
def post_create_view(request) :
    if request.method == "GET" :
        return render(request, 'posts/post_form.html')
    else :
        image = request.FILES.get('image')
        content = request.POST.get('content')
        print(image)
        print(content)
        Post.objects.create(
            iamge=image,
            content=content,
            writer=request.user,
        )
        return redirect('index')   

def post_create_form_view(request) :
    if request.method == "GET" :
        form = PostCreateForm()
        context = {'form' : form}
        return render(request, 'posts/post_form2.html', context)
    else :
        form = PostCreateForm(request.POST, request.FILES)
        
        if form.is_valid():
            Post.objects.create(
            iamge=form.cleaned_data['iamge'],
            content=form.cleaned_data['content'],
            writer=request.user,
        )
        else :
            return redirect('posts:post-create')        
        return redirect('index')  

@login_required
def post_update_view(request, id) : #create랑 detail이랑 합쳐졌다고 생각하면 된다. 그래서 POST랑 GET 둘 다 필요하다.
    
    # post = Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id,writer=request.user)

    if request.method == "GET" :
        context = { 'post': post}
        return render(request, 'posts/post_form.html', context)
    elif request.method == "POST" :
        new_image = request.FILES.get('image')
        content = request.POST.get('content')
        print(new_image)
        print(content)
        if new_image :
            post.iamge.delete()
            post.iamge = new_image
        
        post.contene = content
        post. save()
        return redirect('posts:post-detail',post.id)

@login_required
def post_delete_view(request, id) :
    post = get_object_or_404(Post, id=id,writer=request.user)
    # if request.user != post.writer:
    #     raise Http404('잘못된 접근입니다.')
    
    if request.method == 'GET' :
        context = { 'post': post}
        return render(request, 'posts/post_confirm_delete.html', context)   
    else :
        post.delete()
        return redirect('index')
    









def url_view(request) :
    print('url_view()')
    data = {'code':'001', 'msg':'ok'}
    return HttpResponse('<h1>안녕</h1>')
    # return JsonResponse(data)

def url_parameter_view(request, username):
    print('url_parameter_view()')
    print(f'username: {username}')
    print(f'request.GET: {request.GET}')
    return HttpResponse(username)

def function_view(request) :
    print(f'request.method: {request.method}')

    if request.method =='GET' :
        print(f'request.GET: {request.GET}')
    elif request.method =='POST' :
        print(f'request.POST: {request.POST}')
    # print(f'request.GET: {request.GET}')  #GET = 데이터를 받을 때 사용
    # print(f'request.POST: {request.POST}') #POST = 데이터를 추가,수정,삭제 할 때 사용
    return render(request, 'view.html')

    # 이 위까지는 FBV 함수 기반 뷰
    # 밑에서부터는 CBV 클래스 기반 뷰

class class_view(ListView) :
    model = Post
    template_name = 'cbv_view.html'