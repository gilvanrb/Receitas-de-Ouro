from django.shortcuts import render, get_object_or_404

from .models import Receitas

def home(request):
    receitas = Receitas.objects.all()
    return render(request, 'home/principal.html', {'receitas': receitas})
# Create your views here.

def ver_receitas(request, id):
    receita = get_object_or_404(Receitas, pk=id)
    return render(request, 'home/receitas.html', {'receitas': receita})
