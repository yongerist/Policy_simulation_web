from django.shortcuts import render, redirect
from app01 import models
from app01.utills.form import UserModelForm

"""对指标的操作"""


def target_list(request):
    """指标列表"""
    queryset = models.Target.objects.all()
    return render(request, "target_list.html", {'queryset': queryset})


def target_add(request):
    """添加指标"""
    if request.method == "GET":
        return render(request, "target_add.html")
    """获取用户通过post输入的数据"""
    target = request.POST.get('target')
    """保存到数据库"""
    models.Target.objects.create(target=target)
    """重定向"""
    return redirect("/target/list/")


def target_delete(request):
    """删除指标"""
    nid = request.GET.get('nid')
    models.Target.objects.filter(id=nid).delete()
    return redirect("/target/list/")


def target_edit(request, nid):
    """修改指标"""
    if request.method == "GET":
        row_obj = models.Target.objects.filter(id=nid).first()
        return render(request, 'target_edit.html', {"row_obj": row_obj})
    target = request.POST.get("target")
    models.Target.objects.filter(id=nid).update(target=target)
    return redirect("/target/list/")
