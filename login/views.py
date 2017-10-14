from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


#  1、index.html   网站首页，顶部“注册|登录”和用户信息是切换显示的，
#  商品分类菜单点击直接链接滚动到本页面商品模块。首页已加入幻灯片效果。
#  此效果在课程中已讲述如何制作。
def index(request):
    return render(request, 'index.html')


# 2、list.html  商品列表页，商品分类菜单鼠标悬停时切换显示和隐藏，
# 点击菜单后链接到对应商品的列表页。
def list(request):
    return render(request, 'list.html')


#3、detail.html  商品详情页，某一件商品的详细信息。
def detail(request):
    return render(request, 'detail.html')


# 4、cart.html 我的购物车页，列出已放入购物车上的商品
def cart(request):
    return render(request, 'cart.html')


# 5、place_order.html 提交订单页
def place_order(request):
    return render(request, 'place_order.html')


# 6、login.html 登录页面
def login(request):
    # print(request.GET['username'])
    # print(request.GET['pwd'])
    # 处理登录的逻辑

    return render(request, 'login.html')


# 7、register.html 注册页面，已加入了初步的表单验证效果，此效果在课程中已讲述如何制作。
def register(request):
    return render(request, 'register.html')


# 8、user_center_info.html 用户中心-用户信息页 用户中心功能一，查看用户的基本信息
def user_center_info(request):
    return render(request, 'user_cneter_info.html')


# 9、user_center_order.html 用户中心-用户订单页 用户中心功能二，查看用户的全部订单
def user_center_order(request):
    return render(request, 'user_center_order.html')


# 10、user_center_site.html 用户中心-用户收货地址页 用户中心功能三，查看和设置用户的收货地址
def user_center_site(request):
    return render(request, 'user_center_ist.html')




















