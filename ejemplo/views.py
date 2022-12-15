from django.shortcuts import render, get_object_or_404 
from ejemplo.models import Familiar, Empleado, Alumno
from ejemplo.forms import Buscar, FamiliarForm, EmpleadoForm
from django.views import View 
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView

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

class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})


class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":"", "fecha":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"Se cargó con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class ActualizarFamiliar(View):
  form_class = FamiliarForm
  template_name = 'ejemplo/actualizar_familiar.html'
  initial = {"nombre":"", "direccion":"", "numero_pasaporte":"", "fecha":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(instance=familiar)
      return render(request, self.template_name, {'form':form,'familiar': familiar})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(request.POST ,instance=familiar)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito el familiar {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'familiar': familiar,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})


class FamiliarList(ListView):
  model = Familiar


class FamiliarCrear(CreateView):
  model = Familiar
  success_url = "/panel-familia"
  fields = ["nombre", "direccion", "numero_pasaporte", "fecha"]
  initial = {"nombre":"", "direccion":"", "numero_pasaporte":"", "fecha":""}



class FamiliarBorrar(DeleteView):
  model = Familiar
  success_url = "/panel-familia"


class FamiliarActualizar(UpdateView):
  model = Familiar
  success_url = "/panel-familia"
  fields = ["nombre", "direccion", "numero_pasaporte", "fecha"]


#Empleado

class AltaEmpleado(View):

    form_class = EmpleadoForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":"", "fecha":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"Se cargó con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})


class EmpleadoDetail(DetailView):
  model = Empleado

class EmpleadoList(ListView):
  model = Empleado

class EmpleadoCrear(CreateView):
  model = Empleado
  success_url = "/panel-empleado"
  fields = ["nombre", "puesto", "documento"]
  initial = {"nombre":"", "puesto":"", "documento":""}

class EmpleadoBorrar(DeleteView):
  model = Empleado
  success_url = "/panel-empleado"

class EmpleadoActualizar(UpdateView):
  model = Empleado
  success_url = "/panel-empleado"
  fields = ["nombre", "puesto", "documento"]


#Alumno 
class AlumnoDetail(DetailView):
  model = Alumno

class AlumnoList(ListView):
  model = Alumno

class AlumnoCrear(CreateView):
  model = Alumno
  success_url = "/panel-alumno"
  fields = ["nombre", "clase", "nota_final"]
  initial = {"nombre":"", "clase":"", "nota_final":""}

class AlumnoBorrar(DeleteView):
  model = Alumno
  success_url = "/panel-alumno"

class AlumnoActualizar(UpdateView):
  model = Alumno
  success_url = "/panel-alumno"
  fields = ["nombre", "clase", "nota_final"]