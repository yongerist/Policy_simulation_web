from django.shortcuts import render, redirect
from app01 import models
from app01.utills.form import UserModelForm

""""对用户的操作"""


def user_list(request):
    """用户列表"""
    queryset = models.UserInfo.objects.all()
    return render(request, "user_list.html", {'queryset': queryset})


def user_model_form_add(request):
    if request.method == "GET":
        form = UserModelForm()
        return render(request, "user_model_form_add.html", {"form": form})
    form = UserModelForm(data=request.POST)
    if form.is_valid():  # 校验数据是否合法
        print(form.cleaned_data)
        form.save()  # 将数据保存到数据库
        return redirect('/user/list/')
    else:
        return render(request, "user_model_form_add.html", {"form": form})


def user_edit(request, nid):
    """编辑用户"""

    # 根据nid获取要编辑的那一行的数据
    row_obj = models.UserInfo.objects.filter(id=nid).first()
    if request.method == "GET":
        # 在编辑页面开始先显示原始数据
        form = UserModelForm(instance=row_obj)
        return render(request, "user_edit.html", {'form': form})
    form = UserModelForm(data=request.POST, instance=row_obj)  # instance指向你要更新的对象
    if form.is_valid():
        # 如果想保存用户输入以外的一些值,可以用 'form.instance.字段名 = 值'
        form.save()
        return redirect('/user/list')
    return render(request, 'user_edit.html', {'form': form})


def user_delete(request, nid):
    """删除用户"""
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')
