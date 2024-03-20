from django.shortcuts import render
def frontview(request):
    return render(request, 'core/template/front.html')