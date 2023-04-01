from django.shortcuts import render, redirect
from app01 import models


def algorithm_list(request):
    """算法列表"""
    queryset = models.Algorithm.objects.all()
    return render(request, "algorithm_list.html", {'queryset': queryset})


def algorithm_add(request):
    """添加算法"""
    if request.method == "GET":
        return render(request, "algorithm_add.html")
    """获取用户通过post输入的数据"""
    algorithm = request.POST.get('algorithm')
    """保存到数据库"""
    models.Algorithm.objects.create(algorithm=algorithm)
    """重定向"""
    return redirect("/depart/list/")


def algorithm_delete(request):
    """删除算法"""
    nid = request.GET.get('nid')
    models.Algorithm.objects.filter(id=nid).delete()
    return redirect("/depart/list/")


def algorithm_edit(request, nid):
    """修改算法"""
    if request.method == "GET":
        row_obj = models.Algorithm.objects.filter(id=nid).first()
        return render(request, 'algorithm_edit.html', {"row_obj": row_obj})
    algorithm = request.POST.get("algorithm")
    models.Algorithm.objects.filter(id=nid).update(algorithm=algorithm)
    return redirect("/depart/list/")
