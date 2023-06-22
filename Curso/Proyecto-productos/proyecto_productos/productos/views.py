from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect

from .models import Productos
from .forms import ProductosForms

# Create your views here.

class Index(View):
    template_name = 'index.html'
    def post(self, request):
        form = ProductosForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
        return render(request, self.template_name, {'form': form})
    
    def get(self, request):
        productos = Productos.objects.all()

        form = ProductosForms()
        return render(request, self.template_name, {'form': form,'productos': productos})
    
    