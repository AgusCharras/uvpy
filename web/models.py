from django.db import models

class Carrera(models.Model):
    CATEGORIA = {
        "P": "Posgrado",
        "G": "Grado",
        "L": "Licenciatura",
        "T": "Tecnicatura",
    }
    nombre = models.CharField(max_length=64)
    duracion = models.CharField(max_length=24, blank=True)
    titulo = models.CharField(max_length=32)
    categoria = models.CharField(max_length=1, choices=CATEGORIA)
    descripcion = models.TextField()
    img = models.ImageField(upload_to="carreras/", blank=True, null=True)

    def __str__(self):
        return self.nombre