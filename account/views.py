from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # 사용자 인증
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # 로그인 성공 시, `auth_login` 함수에 `request`와 `user` 전달
            auth_login(request, user)
            return redirect("main:mainpage")  # 메인 페이지 URL로 변경하세요
        else:
            # 로그인 실패 시 에러 메시지와 함께 로그인 페이지를 다시 렌더링
            return render(request, 'account/login.html', {'error': '아이디 또는 비밀번호가 잘못되었습니다.'})
    
    return render(request, 'account/login.html')


# views.py
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        name = request.POST.get("name")
        password = request.POST.get("password")
        
        # 유저 생성
        user = get_user_model().objects.create_user(username=username, password=password)
        user.name = name  # 이름 필드 저장
        user.save()
        
        return redirect("main:mainpage")

    return render(request, "account/signup.html")