from django.shortcuts import render, redirect
from .forms import produtoForm
from .models import Produto

def index_view(request):
    produtos = Produto.objects.all().order_by("nome")

    return render(request, 'produtos/index.html', {"produtos":produtos})

def produto_new(request):
    if request.method == 'POST':
        form =  produtoForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('index')
        
    else:
        form = produtoForm()
    return render(request, 'produtos/produto_new.html', {'form':form})