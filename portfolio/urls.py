from django.urls import path
from . import views

app_name = 'portfolio'  # 앱 이름 정의

urlpatterns = [
    path('', views.portfolio, name='portfolio'),  # 포트폴리오 목록 페이지
    path('detail', views.detailpage, name='detailpage'),  # 포트폴리오 목록 페이지
    path('new-portfolio/', views.new_portfolio, name='new-portfolio'),  # 새 포트폴리오 생성 폼
    path('create/', views.create, name='create'),  # 포트폴리오 생성 처리
    path('detail/<int:id>/', views.detail, name='detail'),  # 포트폴리오 상세 페이지
]
