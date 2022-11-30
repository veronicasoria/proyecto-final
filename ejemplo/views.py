from django.shortcuts import render
from ejemplo.models import Familiar

def index(request):
    return render(request, "ejemplo/saludar.html")


def sumar(request, a, b):
    return render(request, 
    "ejemplo/sumar.html", 
     {"a": a,
      "b": b,
      "resultado": a + b}
    )

def buscar(request):
    lista_de_nombres = ["German", "Martin", "Daniel", "Roman"]
    query = request.GET['q']
   
    if query in lista_de_nombres: 
    #http://127.0.0.1:8000/buscar/?q=German
        indice_de_resultado = lista_de_nombres.index(query)
        resultado  = lista_de_nombres[indice_de_resultado]
    else: 
    #http://127.0.0.1:8000/buscar/?q=alo
        resultado = 'No hay match'
    
    return render(request, 'ejemplo/buscar.html', {'resultado': resultado})

def mostrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})


