from django.shortcuts import redirect, render
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .forms import UserCreateForm,SignUpForm
from users.models import User

def singup_view(request):
    #GET 요청 시 HTML 응답
    if request.method == 'GET':
        form = SignUpForm
        context = {'form' : form}
        return render(request, 'accounts/signup.html',context)
    else :
        #POST 요청 시 HTML 응답
        form = SignUpForm(request.POST)

        if form.is_valid():
            # #회원가입 처리
            # username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # password2 = form.cleaned_data['password2']
            instance = form.save() #.save는 장고에서 제공해주는 함수.
            return redirect('index')
        else:
            #리다이렉트
            return redirect('accounts:signup')

def login_view(request):
    # GET, POST 분리
    if request.method == 'GET':
        # 로그인 HTML응답
        return render(request,'accounts/login.html',{'form':AuthenticationForm()})
    else:
        # 데이터 유효성 검사
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            # 비즈니스 로직 처리 - 로그인 처리
            login(request,form.user_cache)
            # 응답
            return redirect('index')
        else:
            # 비즈니스 로직 처리 - 로그인 실패
            # 응답
            return render(request,'accounts/login.html',{'form':form})

        # username = request.POST.get('username')
        # if username == "" or username == None:
        #     pass
        # user = User.object.get(username=username)
        # if user == None:
        #     pass
        # password = request.POST.get('password')

def logout_view(request):
    #데이터 유효성 검사
    if request.user.is_authenticated:
        #비즈니스 로직 처리 - 로그아웃
        logout(request)
    
    #응답
    return redirect('index')