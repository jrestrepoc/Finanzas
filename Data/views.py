from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import montos

def Data_view(request):
    if request.method == 'POST':
        ingresos = int(request.POST.get('ingreso'))
        gastos = int(request.POST.get('gasto'))
        saldo = ingresos - gastos
        Montos = montos(user = request.user, ingresos = ingresos, gastos = gastos, saldo = saldo)
        Montos.save()
        return redirect('stadistics')
    return render(request, 'information.html')