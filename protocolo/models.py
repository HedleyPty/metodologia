from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Protocolo(models.Model):
    titulo=models.CharField(default="", max_length=100)
    resumen=models.TextField(default="", max_length=10000)
    planteamiento=models.TextField(default="", max_length=10000)
    justificacion=models.TextField(default="", max_length=10000)
    resultados=models.TextField(default="", max_length=10000)
    resultados_puntuacion=models.IntegerField(default=0)
    marco=models.TextField(default="", max_length=10000)
    general=models.TextField(default="", max_length=10000)
    especifico=models.TextField(default="", max_length=10000)
    variables=models.TextField(default="", max_length=10000)
    tipo=models.TextField(default="", max_length=10000)
    universo=models.TextField(default="", max_length=10000)
    seleccion=models.TextField(default="", max_length=10000)
    etica=models.TextField(default="", max_length=10000)
    analisis=models.TextField(default="", max_length=10000)

    
class Evaluacion(models.Model):
    protocolo=models.ForeignKey(Protocolo, on_delete=models.CASCADE, default="")
    titulo=models.CharField(default="", max_length=1000)
    titulo_puntuacion=models.IntegerField(default=0)
    resumen=models.TextField(default="", max_length=10000)
    resumen_puntuacion=models.IntegerField(default=0)
    planteamiento=models.TextField(default="", max_length=10000)
    planteamiento_puntuacion=models.IntegerField(default=0)
    justificacion=models.TextField(default="", max_length=10000)
    justificacion_puntuacion=models.IntegerField(default=0)
    resultados=models.TextField(default="", max_length=10000)
    resultados_puntuacion=models.IntegerField(default=0)
    marco=models.TextField(default="", max_length=10000)
    marco_puntuacion=models.IntegerField(default=0)
    general=models.TextField(default="", max_length=10000)
    general_puntuacion=models.IntegerField(default=0)
    especifico=models.TextField(default="", max_length=10000)
    especifico_puntuacion=models.IntegerField(default=0)
    variables=models.TextField(default="", max_length=10000)
    variables_puntuacion=models.IntegerField(default=0)
    tipo=models.TextField(default="", max_length=10000)
    tipo_puntuacion=models.IntegerField(default=0)
    universo=models.TextField(default="", max_length=10000)
    universo_puntuacion=models.IntegerField(default=0)
    seleccion=models.TextField(default="", max_length=10000)
    seleccion_puntuacion=models.IntegerField(default=0)
    etica=models.TextField(default="", max_length=10000)
    etica_puntuacion=models.IntegerField(default=0)
    analisis=models.TextField(default="", max_length=10000)
    analisis_puntuacion=models.IntegerField(default=0)
class Autor(User):
    protocolo=models.OneToOneField(Protocolo, on_delete=models.CASCADE, default="")
class Revisor(User):
    protocolo=models.ForeignKey(Protocolo, on_delete=models.CASCADE, default="")