from django.shortcuts import render
from django.db.models import Sum
from Data.models import montos

# Create your views here.
def resume(request):
    current_user = request.user

    # Filtra los datos según el usuario actual
    ingresos = montos.objects.filter(user=current_user).aggregate(Sum('ingresos'))['ingresos__sum']
    gastos = montos.objects.filter(user=current_user).aggregate(Sum('gastos'))['gastos__sum']
    saldo = montos.objects.filter(user=current_user).aggregate(Sum('saldo'))['saldo__sum']

    return render(request, 'stadistics.html', {'ingresos': ingresos, 'gastos': gastos, 'saldo': saldo})