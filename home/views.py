from django.shortcuts import render

def home(request):
    return render(request, 'home/principal.html')

# Create your views here.
def ver_receitas(request):
    return render(request, 'home/receitas.html')