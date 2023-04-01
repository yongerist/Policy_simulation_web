from django.shortcuts import render, redirect


def main(request):
    return render(request, "main.html")


def goods_list(request):
    return render(request, "goods_list.html")


def register(request):
    return render(request, "register.html")


def super_login(request):
    return render(request, "super_login.html")
