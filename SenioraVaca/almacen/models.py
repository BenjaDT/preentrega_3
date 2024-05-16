from django.db import models

# Create your models here.

# persona, productos, proveedores, trabajadores, posiciones

class Persona(models.Model):
    nombre = models.CharField(max_length=150)
    dni = models.PositiveIntegerField(unique=True)
    celular = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.nombre

class Provedor(models.Model):
    nombre = models.CharField(max_length=150)
    Cuil = models.PositiveIntegerField(unique=True)
    contacto = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.nombre

#Posicion se refiere a los diferentes puestos de trabajo, es heredada por trabajador
class Posicion(models.Model):
    nombre = models.CharField(max_length=150)
    sueldo = models.PositiveIntegerField(unique=False)

    def __str__(self) -> str:
        return self.nombre

class Trabajador(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, blank=True)
    puesto = models.ForeignKey(Posicion, on_delete=models.SET_NULL, null=True, blank=True)
    #antiguedad es la fecha en la que entraron en la empresa
    antiguedad = models.DateField()

    def __str__(self) -> str:
        return f'Nombre: {self.persona.nombre}, Puesto: {self.puesto.nombre}'
    
class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    provedor = models.ForeignKey(Provedor, on_delete=models.SET_NULL, null=True, blank=True)
    precio = models.PositiveIntegerField(unique=False)
    stock = models.PositiveIntegerField
