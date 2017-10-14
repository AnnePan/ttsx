from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# 登录功能
def login(request):
    # print(request.GET['username'])
    # print(request.GET['pwd'])
    # 处理登录的逻辑

    return render(request, 'login.html')

















