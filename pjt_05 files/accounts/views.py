from django.shortcuts import render, redirect
from . import models
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as my_login
from django.contrib.auth import logout as my_logout


# Create your views here.
# login 관련 내용 사용할 것 -> usermodel까지 받아와야 함
# login 자체를 사용할 form
# login 작성 페이지를 만들고 -> 그것을 받아줄 페이지를 작성해야 함
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST) #사용자 정보를 받아오고, request를 통해 세션 검증하기 위함
        if form.is_valid():
            my_login(request, form.get_user()) #user 정보 받아서 -> 로그인 시킨다.
            return redirect('movies:index')
            #main페이지로 리다이렉트 시켜준다. -> index.html로 수정
    else :
        form = AuthenticationForm()
    context = {
        'form' : form
    } #인증 받지 못하면 다시 작성 요청 or 로그인 자체를 진행할 요청 방법
    return render(request, 'accounts/login.html', context)

#단순히 그냥 진행하면됨 -> 무엇을 불러올 필요가 없음 : 세션 자체를 받아와서 사용
def logout(request):
    my_logout(request) #main페이지로 redirect == POST로 받아서 삭제해야함
    return redirect('movies:index')

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = UserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)