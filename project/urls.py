"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ejemplo.views import (index, sumar, buscar, 
                            mostrar_familiares, BuscarFamiliar, AltaFamiliar, ActualizarFamiliar, 
                            FamiliarList, FamiliarCrear, FamiliarBorrar, FamiliarActualizar, 
                            EmpleadoDetail, EmpleadoList, EmpleadoCrear, EmpleadoBorrar, EmpleadoActualizar, 
                            AlumnoList, AlumnoCrear, AlumnoBorrar, AlumnoActualizar, AlumnoDetail)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index), 
    path('sumar/<a>/<b>/', sumar),
    path('buscar/', buscar),
    path('mi-familia/', mostrar_familiares), 
    path('mi-familia/buscar', BuscarFamiliar.as_view()), 
    path('mi-familia/alta', AltaFamiliar.as_view()), 
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()), 
    path('panel-familia/', FamiliarList.as_view()), 
    path('panel-familia/crear', FamiliarCrear.as_view()), 
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()), 
    path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()), 
    path('panel-empleado/', EmpleadoList.as_view()),
    path('panel-empleado/crear', EmpleadoCrear.as_view()), 
    path('panel-empleado/<int:pk>/borrar', EmpleadoBorrar.as_view()), 
    path('panel-empleado/<int:pk>/actualizar', EmpleadoActualizar.as_view()), 
    path('panel-empleado/<int:pk>/detalle', EmpleadoDetail.as_view()), 
    path('panel-alumno/', AlumnoList.as_view()),
    path('panel-alumno/crear', AlumnoCrear.as_view()), 
    path('panel-alumno/<int:pk>/borrar', AlumnoBorrar.as_view()), 
    path('panel-alumno/<int:pk>/actualizar', AlumnoActualizar.as_view()), 
    path('panel-alumno/<int:pk>/detalle', AlumnoDetail.as_view()), 
]
