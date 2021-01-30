from django.db import models
from django.urls import reverse, reverse_lazy
# from rest_framework.reverse import reverse, reverse_lazy
# from rest_framework.reverse import reverse_lazy
# from django.http import HttpRequest


# Create your models here.

class Planeta(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    diametro = models.IntegerField(null=True, blank=True)
    periodo_rotacion = models.IntegerField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    clima = models.CharField(max_length=10, null=True, blank=True)
    gravedad = models.CharField(max_length=10, null=True, blank=True)
    poblacion = models.CharField(max_length=10, null=True, blank=True)
    periodo_orbita = models.CharField(max_length=10, null=True, blank=True)
    agua_superficie = models.CharField(max_length=10, null=True, blank=True)
    terreno  = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):  
        return reverse("planeta-list")
        # return "{0}".format(self.nombre)
        # return self.nombre

    def get_absolute_url(self):
        return reverse("planeta-list")

"""

{

    "films": [
        "https://swapi.py4e.com/api/films/1/",
        ...
    ],
    "name": "Tatooine",
    "residents": [
        "https://swapi.py4e.com/api/people/1/",
        ...
    ],
    "url": "https://swapi.py4e.com/api/planets/1/"
}

"""


class Persona(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    anho_nacimiento = models.CharField(max_length=50, null=True, blank=True)
    color_ojos = models.CharField(max_length=50, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    planeta = models.ForeignKey(Planeta, null=True, blank=True, on_delete=models.PROTECT, related_name="residentes")
    # especie = models.ForeignKey(Especie, null=True, blank=True, on_delete=models.PROTECT, related_name="especies")
    genero = models.CharField(max_length=10, null=True, blank=True)
    color_cabello = models.CharField(max_length=10, null=True, blank=True)
    estatura = models.CharField(max_length=10, null=True, blank=True)
    peso = models.CharField(max_length=10, null=True, blank=True)
    color_piel = models.CharField(max_length=10, null=True, blank=True)
    
    def __str__(self):  
        return "{0}".format(self.nombre)

    def get_absolute_url(self):
        return reverse("persona-list")


"""
    "films": [
        "https://swapi.py4e.com/api/films/1/",
        ...
    ],
    "homeworld": "https://swapi.py4e.com/api/planets/1/",
    "starships": [
        "https://swapi.py4e.com/api/starships/12/",
        ...
    ],
    "vehicles": [
        "https://swapi.py4e.com/api/vehicles/14/"
        ...
    ]
"""

        
        
        
class Especie(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    esperanza_vida = models.CharField(max_length=10, null=True, blank=True)
    clasificacion = models.CharField(max_length=10, null=True, blank=True)
    designacion = models.CharField(max_length=10, null=True, blank=True)
    color_ojos = models.CharField(max_length=50, null=True, blank=True)
    color_cabello = models.CharField(max_length=10, null=True, blank=True)
    lenguaje = models.CharField(max_length=10, null=True, blank=True)
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.PROTECT, related_name="especies")
    estatura_promedio = models.CharField(max_length=10, null=True, blank=True)
    planeta = models.ForeignKey(Planeta, null=True, blank=True, on_delete=models.PROTECT, related_name="especies")

    def __str__(self):  
        return "{0}".format(self.nombre)
        # return self.nombre

"""
    "people": [
        "https://swapi.py4e.com/api/people/13/"
    ],
    "films": [
        "https://swapi.py4e.com/api/films/1/",
        "https://swapi.py4e.com/api/films/2/"
    ],
    "skin_colors": "gray",
    "url": "https://swapi.py4e.com/api/species/3/"    

"""

class Vehiculo(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    capacidad_carga = models.CharField(max_length=10, null=True, blank=True)
    consumbibles = models.CharField(max_length=10, null=True, blank=True)
    costo_en_creditos = models.CharField(max_length=10, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    tripulacion = models.CharField(max_length=10, null=True, blank=True)
    longitud = models.CharField(max_length=10, null=True, blank=True)
    fabricante = models.CharField(max_length=50, null=True, blank=True)
    maxima_velocidad = models.CharField(max_length=10, null=True, blank=True)
    modelo = models.CharField(max_length=50, null=True, blank=True)
    pasajeros = models.CharField(max_length=10, null=True, blank=True)
    clase_vehiculo = models.CharField(max_length=10, null=True, blank=True)
        
        
"""

    "pilots": [],
    "films": [
        "https://swapi.py4e.com/api/films/1/"
    ],
    "url": "https://swapi.py4e.com/api/vehicles/4/",
"""


class Nave(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    MGLT = models.CharField(max_length=10, null=True, blank=True)
    consumibles = models.CharField(max_length=10, null=True, blank=True)
    costo_en_creditos = models.CharField(max_length=10, null=True, blank=True)
    tripulacion = models.CharField(max_length=10, null=True, blank=True)
    puntaje_hyperdrive = models.CharField(max_length=10, null=True, blank=True)
    longitud = models.CharField(max_length=10, null=True, blank=True)
    fabricante = models.CharField(max_length=50, null=True, blank=True)
    maxima_velocidad = models.CharField(max_length=10, null=True, blank=True)
    modelo = models.CharField(max_length=50, null=True, blank=True)
    pasajeros = models.CharField(max_length=10, null=True, blank=True)
    clase_nave = models.CharField(max_length=50, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

"""
{
    "MGLT": "10 MGLT",
    "cargo_capacity": "1000000000000",
    "consumables": "3 years",
    "cost_in_credits": "1000000000000",
    "created": "2014-12-10T16:36:50.509000Z",
    "crew": "342953",
    "edited": "2014-12-10T16:36:50.509000Z",
    "hyperdrive_rating": "4.0",
    "length": "120000",
    "manufacturer": "Imperial Department of Military Research, Sienar Fleet Systems",
    "max_atmosphering_speed": "n/a",
    "model": "DS-1 Orbital Battle Station",
    "name": "Death Star",
    "passengers": "843342",
    "films": [
        "https://swapi.py4e.com/api/films/1/"
    ],
    "pilots": [],
    "starship_class": "Deep Space Mobile Battlestation",
    "url": "https://swapi.py4e.com/api/starships/9/"
}

"""



class Pelicula(models.Model):
    titulo = models.CharField(max_length=50, null=False, blank=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    director = models.CharField(max_length=50, null=True, blank=True)
    codigo_episodio = models.CharField(max_length=50, null=True, blank=True)
    texto_apertura = models.CharField(max_length=200, null=True, blank=True)
    productor = models.CharField(max_length=50, null=True, blank=True)
    fecha_emision = models.CharField(max_length=50, null=True, blank=True)

"""

{
    "characters": [
        "https://swapi.py4e.com/api/people/1/",
        ...
    ],
    "planets": [
        "https://swapi.py4e.com/api/planets/1/",
        ...
    ],
    "species": [
        "https://swapi.py4e.com/api/species/1/",
        ...
    ],
    "starships": [
        "https://swapi.py4e.com/api/starships/2/",
        ...
    ],
    "url": "https://swapi.py4e.com/api/films/1/",
    "vehicles": [
        "https://swapi.py4e.com/api/vehicles/4/",
        ...
    ]
}
"""