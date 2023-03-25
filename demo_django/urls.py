"""demo_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    写url和函数的对应关系
"""
from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.main),
    path('main/goods_list', views.goods_list),
    path('main/policy_simulation', views.policy_simulation),
    path('main/simu_history', views.simu_history),
    path('register/', views.register),
    path('super/login', views.super_login),
    # path('super/use', views.super_use),


    # path('test/tpl', views.tpl),
    # path('test/something', views.something),
    # path('test/login', views.login),


    # path('info/list', views.info_list),
    # path('info/add', views.info_add),
    # path('info/delete/', views.info_delete)


    path('depart/list/', views.algorithm_list),
    path('depart/add/', views.algorithm_add),
    path('depart/delete/', views.algorithm_delete),
    path('depart/<int:nid>/edit/', views.algorithm_edit),

    path('user/list/', views.user_list),
    # path('user/add/', views.user_add),
    path('user/model/form/add/', views.user_model_form_add),
    path('user/<int:nid>/edit/', views.user_edit),
    path('user/<int:nid>/delete/', views.user_delete),

    path('target/list/', views.target_list),
    path('target/add/', views.target_add),
    path('target/delete/', views.target_delete),
    path('target/<int:nid>/edit/', views.target_edit),

    path('pretty/list/', views.pretty_list),
    path('pretty/add/', views.pretty_add),
    path('pretty/<int:nid>/edit/', views.pretty_edit),
    path('pretty/<int:nid>/delete/', views.pretty_delete),

]
