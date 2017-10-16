from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^list/$', views.list),
    url(r'^detail/$', views.detail),
    url(r'^cart/$', views.cart),
    url(r'^place_order/$', views.place_order),
    url(r'^login.html/$', views.login),
    url(r'^register.html/$', views.register),
    url(r'^user_center_info/$', views.user_center_info),
    url(r'^user_center_order/$', views.user_center_order),
    url(r'^user_center_site/$', views.user_center_site),

]