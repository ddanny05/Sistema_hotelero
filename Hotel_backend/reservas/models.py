from django.db import models

# Create your models here.

class Cliente(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True, blank=False)
    nombre = models.CharField(max_length=50, blank=False)
    apellido = models.CharField(max_length=50, blank=False)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField(blank=False)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.cedula} - {self.nombre} {self.apellido}'
    
class Habitacion(models.Model):
    codigo = models.CharField(primary_key=True,max_length=4)
    numero = models.CharField(max_length=4)
    tipo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Habitación {self.numero} - {self.tipo}'

class Reserva(models.Model):
    cedula = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    codigo = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField()
    def __str__(self):
        return f'Reserva de {self.cedula.apellido} en habitación {self.codigo.numero}'

