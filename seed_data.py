from ejemplo.models import Familiar

Familiar(fecha = "2020-01-01", nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123).save()
Familiar(fecha = "2020-01-01", nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890).save()
Familiar(fecha = "2020-01-01", nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345).save()
Familiar(fecha = "2020-01-01", nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567).save()
print("Se cargo con éxito los usuarios de pruebas")