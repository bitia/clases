from django.db import models

etiquetas=[]
class PreguntaModel(models.Model,etiquetas):
    opc_asertividad=(
        ('1','Si'),
        ('0','No'),
        )
    pregunta1=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas[0])
    pregunta2=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas[1])
    pregunta3=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas[2])
    pregunta4=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas[3]) 
    pregunta5=models.CharField(choices=opc_asertividad,
            blank=False,max_length=2,verbose_name=etiquetas[4])
    class Meta:
        abstract = True