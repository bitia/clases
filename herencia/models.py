from __future__ import unicode_literals

from django.db import models
from core.labels import etiquetas1
from core.models import PreguntaModel
# Create your models here.

class OrganizacionEstudio(PreguntaModel):
    def __init__(self):
        self.etiquetas=etiquetas1

class OrganizacionEstudio1(PreguntaModel):
    def __init__(self):
        self.etiquetas=etiquetas2

class OrganizacionEstudio2(PreguntaModel):
    def __init__(self):
        self.etiquetas=etiquetas3



