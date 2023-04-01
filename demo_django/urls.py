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
from app01.views import main, algorithm, simulation, target, user
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('main/', main.main),
    path('main/goods_list', main.goods_list),
    path('main/policy_simulation', simulation.policy_simulation),
    path('main/simu_history', simulation.simu_history),
    path('register/', main.register),
    path('super/login', main.super_login),
    # path('super/use', views.super_use),


    # path('test/tpl', views.tpl),
    # path('test/something', views.something),
    # path('test/login', views.login),


    # path('info/list', views.info_list),
    # path('info/add', views.info_add),
    # path('info/delete/', views.info_delete)


    path('depart/list/', algorithm.algorithm_list),
    path('depart/add/', algorithm.algorithm_add),
    path('depart/delete/', algorithm.algorithm_delete),
    path('depart/<int:nid>/edit/', algorithm.algorithm_edit),

    path('user/list/', user.user_list),
    # path('user/add/', views.user_add),
    path('user/model/form/add/', user.user_model_form_add),
    path('user/<int:nid>/edit/', user.user_edit),
    path('user/<int:nid>/delete/', user.user_delete),

    path('target/list/', target.target_list),
    path('target/add/', target.target_add),
    path('target/delete/', target.target_delete),
    path('target/<int:nid>/edit/', target.target_edit),

]
