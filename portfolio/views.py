from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from datetime import datetime
from .models import Portfolio

# 포트폴리오 상세 페이지
def detail(request, id):
    portfolio_instance = get_object_or_404(Portfolio, id=id)  # ID로 포트폴리오 객체를 가져옴
    return render(request, 'portfolio/detail.html', {'portfolio': portfolio_instance})

# 포트폴리오 목록 페이지
def detailpage(request):
    portfolios = Portfolio.objects.all()  # 모든 포트폴리오 가져오기
    return render(request, 'portfolio/detailpage.html', {'portfolios': portfolios})

# 포트폴리오 생성 폼 페이지
def portfolio(request):
    return render(request, 'portfolio/portfolio.html')

# 새 포트폴리오 생성 페이지
def new_portfolio(request):
    return render(request, 'portfolio/new-portfolio.html')

# 포트폴리오 생성 처리
def create(request):
    if request.method == 'POST':
        new_portfolio = Portfolio()  # 새 포트폴리오 객체 생성

        # 폼 데이터 처리
        new_portfolio.kind = request.POST['kind']
        new_portfolio.title = request.POST['title']
        new_portfolio.starttime = datetime.strptime(request.POST['starttime'], '%Y-%m-%d %H:%M:%S')
        new_portfolio.finishtime = datetime.strptime(request.POST['finishtime'], '%Y-%m-%d %H:%M:%S')
        new_portfolio.name = request.POST['name']
        new_portfolio.body = request.POST['body']

        new_portfolio.save()  # 포트폴리오 객체 저장

        return redirect('portfolio:detail', id=new_portfolio.id)  # 저장 후 상세 페이지로 리디렉션

    return render(request, 'portfolio/new-portfolio.html')  # GET 요청일 경우 폼 보여주기
