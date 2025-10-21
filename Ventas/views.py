from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required    
from .models import Venta
# Create your views here.

class VentasView(TemplateView):
    template_name ="ventas.html"

class ListadoVentasView(ListView):
    template_name ="listadoventas.html"
    model = Venta
    context_object_name = "ventas"

def about(request):
    return HttpResponse("Hola soy la pagina de Acerca de")

@login_required
def bienvenida(request):
    if request.method == 'POST':
        return HttpResponse("Hola soy la pagina de bienvenida")
    else:
        return HttpResponse("Pagina no encontrada", status=404)
    
def buscar(request, nombre):
    if (request.user.is_authenticated):
        return HttpResponse("Se va a buscar un producto con nombre " + nombre)
    else:
        return HttpResponse("No estas autorizado para buscar productos", status=401)
    
@permission_required('ventas.view_venta', raise_exception=True)
def listadoventas(request):
    if(request.user.groups.filter(name='Administrador').exists()):
        return HttpResponse("Se va a listar las ventas")
    else:
        return HttpResponse("No estas autorizado para listar las ventas", status=401)
    
   