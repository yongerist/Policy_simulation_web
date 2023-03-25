from app01.models import UserInfo
from django.shortcuts import render, redirect
from app01 import models
from django import forms


# Create your views here.
# 编写函数的地方
def main(request):
    return render(request, "main.html")


def goods_list(request):
    return render(request, "goods_list.html")


def register(request):
    return render(request, "register.html")


def super_login(request):
    return render(request, "super_login.html")


def policy_simulation(request):
    """原始版"""
    target_queryset = models.Target.objects.all()
    algorithm_queryset = models.Algorithm.objects.all()

    if request.method == "GET":
        return render(request, "policy_simulation.html",
                      {'target_queryset': target_queryset, 'algorithm_queryset': algorithm_queryset})
    target = request.POST.get("target")
    algorithm = request.POST.get("algorithm")
    time = request.POST.get("time")
    data = request.POST.get("data")
    outcome = int(data) * 2
    models.Simulation.objects.create(target_id=target, algorithm_id=algorithm, data=data, outcome=outcome, time=time)

    # return redirect("/main/policy_simulation")
    return redirect("/main/simu_history")


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


""""对用户的操作"""


def user_list(request):
    """用户列表"""
    queryset = models.UserInfo.objects.all()
    return render(request, "user_list.html", {'queryset': queryset})


class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", "account", "create_time", "depart", "gender"]

    """让样式变为form-control"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


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


def simu_history(request):
    """展示模拟历史"""
    queryset = models.Simulation.objects.all()
    return render(request, 'simu_history.html', {'queryset': queryset})



