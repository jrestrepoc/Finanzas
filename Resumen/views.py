from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from Data.models import montos
from .models import ChatBot
from django.http import HttpResponseRedirect, JsonResponse
import google.generativeai as genai
from django.utils import timezone
from django.http import HttpResponse

genai.configure(api_key="AIzaSyC1F09Pw2VjBST3N_XyevTomD4uXG67UUM")

# Create your views here.
@login_required
def resume(request):
    chats = ChatBot.objects.filter(user=request.user)
    if request.method == "POST":
        user = request.user
        ingresos = montos.objects.filter(user=user).aggregate(Sum('ingresos'))['ingresos__sum']
        gastos = montos.objects.filter(user=user).aggregate(Sum('gastos'))['gastos__sum']
        saldo = montos.objects.filter(user=user).aggregate(Sum('saldo'))['saldo__sum']
        message = request.POST.get("message")
        response = ask_gemini(message)
        chat = ChatBot(text_input=message, gemini_output=response, user=request.user, date=timezone.now())
        chat.save()
        print(message, response)
        # Extract necessary data from response
        return JsonResponse({'message': message, 'response':response, 'ingresos': ingresos, 'gastos': gastos, 'saldo': saldo})
    else:
        current_user = request.user
        # Filtra los datos según el usuario actual
        ingresos = montos.objects.filter(user=current_user).aggregate(Sum('ingresos'))['ingresos__sum']
        gastos = montos.objects.filter(user=current_user).aggregate(Sum('gastos'))['gastos__sum']
        saldo = montos.objects.filter(user=current_user).aggregate(Sum('saldo'))['saldo__sum']
        return render(request, 'stadistics.html', {'ingresos': ingresos, 'gastos': gastos, 'saldo': saldo, 'chats': chats})

def ask_gemini(promt):
    model = genai.GenerativeModel("gemini-pro")
    chat = model.start_chat()
    response = chat.send_message(promt)
    print(response.text)
    return response.text

def acerca(request):
    return render(request, 'acerca.html')