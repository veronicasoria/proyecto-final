from django import forms
from ejemplo.models import Familiar, Empleado, Alumno

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100, 
                                widget=forms.TextInput(attrs ={'placeholder': 'Ingrese su búsqueda'}))


class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte', 'fecha']


class EmpleadoForm(forms.ModelForm):
  class Meta:
    model = Empleado
    fields = ['nombre', 'puesto', 'documento']


class AlumnoForm(forms.ModelForm):
  class Meta:
    model = Alumno
    fields = ['nombre', 'clase', 'nota_final']
