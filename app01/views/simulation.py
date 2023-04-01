from django.shortcuts import render, redirect
from app01 import models


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


def simu_history(request):
    """展示模拟历史"""
    queryset = models.Simulation.objects.all()
    return render(request, 'simu_history.html', {'queryset': queryset})