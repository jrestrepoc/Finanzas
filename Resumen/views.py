from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from Data.models import montos
from .models import ChatBot
from django.http import HttpResponseRedirect, JsonResponse
import google.generativeai as genai

genai.configure(api_key="AIzaSyC1F09Pw2VjBST3N_XyevTomD4uXG67UUM")

# Create your views here.
@login_required
def resume(request):
    if request.method == "POST":
        current_user = request.user
        # Filtra los datos según el usuario actual
        ingresos = montos.objects.filter(user=current_user).aggregate(Sum('ingresos'))['ingresos__sum']
        gastos = montos.objects.filter(user=current_user).aggregate(Sum('gastos'))['gastos__sum']
        saldo = montos.objects.filter(user=current_user).aggregate(Sum('saldo'))['saldo__sum']
        text = request.POST.get("text")
        model = genai.GenerativeModel("gemini-pro")
        chat = model.start_chat()
        response = chat.send_message(text)
        user = request.user
        chats = ChatBot.objects.filter(user=user)
        ChatBot.objects.create(text_input=text, gemini_output=response.text, user=user)
        print(text, response.text)
        # Extract necessary data from response
        response_data = {
            'text': response.text,  # Assuming response.text contains the relevant response data
            # Add other relevant data from response if needed
        }
        return render(request, 'stadistics.html', {'data': response_data, 'ingresos': ingresos, 'gastos': gastos, 'saldo': saldo, 'chats': chats})
    else:
        current_user = request.user
        # Filtra los datos según el usuario actual
        ingresos = montos.objects.filter(user=current_user).aggregate(Sum('ingresos'))['ingresos__sum']
        gastos = montos.objects.filter(user=current_user).aggregate(Sum('gastos'))['gastos__sum']
        saldo = montos.objects.filter(user=current_user).aggregate(Sum('saldo'))['saldo__sum']
        return render(request, 'stadistics.html', {'ingresos': ingresos, 'gastos': gastos, 'saldo': saldo})
    