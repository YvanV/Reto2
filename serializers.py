from rest_framework import serializers

from .models import *

class EspecieIdSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = "especie-detail"
    )
    class Meta:
        model = Especie
        fields = ["url"]

class NaveIdSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = "nave-detail"
    )
    class Meta:
        model = Nave
        fields = ["url"]

class PeliculaIdSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = "pelicula-detail"
    )
    class Meta:
        model = Pelicula
        fields = ["url"]

class VehiculoIdSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = "vehiculo-detail"
    )
    class Meta:
        model = Vehiculo
        fields = ["url"]

class PersonaSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = "persona-detail"
    )
    especies = EspecieIdSerializer(many=True, read_only=True)
    # planeta2 = serializers.HyperlinkedIdentityField(
    #     view_name = "planeta-detail",
    #     lookup_field = "planeta_id"
    # )
    class Meta:
        model = Persona
        fields = ["id", "anho_nacimiento", "color_ojos", "nombre", 
        "fecha_creacion", "fecha_actualizacion", "planeta",
        "genero", "color_cabello", "estatura", "peso", "color_piel", "url", "especies"
        ]   



class PersonaIdSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = "persona-detail"
    )
    class Meta:
        model = Persona
        fields = ["url"]


class PlanetaSerializer(serializers.ModelSerializer):
    residentes = PersonaIdSerializer(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name = "planeta-detail"
    )

    class Meta:
        model = Planeta
        fields = ["id", "nombre", "diametro", "periodo_rotacion", "fecha_creacion", 
        "fecha_actualizacion", "residentes", "clima", "gravedad", "poblacion", 
        "periodo_orbita", "agua_superficie", "terreno", "url"]
    
class EspecieSerializer(serializers.ModelSerializer):
    # residentes = PersonaIdSerializer(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name = "especie-detail"
    )

    class Meta:
        model = Especie
        fields = ["nombre", "esperanza_vida", "clasificacion", "designacion", 
        "color_ojos", "color_cabello", "lenguaje", "url", "persona"]
    
class VehiculoSerializer(serializers.ModelSerializer):
    # residentes = PersonaIdSerializer(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name = "vehiculo-detail"
    )

    class Meta:
        model = Vehiculo
        fields = ["nombre", "capacidad_carga", "consumbibles", "costo_en_creditos", "fecha_creacion",
        "fecha_actualizacion", "tripulacion", "longitud", "fabricante",
        "maxima_velocidad", "modelo", "pasajeros", "clase_vehiculo", "url"]

class NaveSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = "nave-detail"
    )

    class Meta:
        model = Nave
        fields = ["nombre", "MGLT", "consumibles", "costo_en_creditos","tripulacion", 
        "puntaje_hyperdrive",
        "longitud", "fabricante", "maxima_velocidad", "modelo", 
        "pasajeros", "clase_nave", "fecha_creacion", "fecha_actualizacion", "url"
        ]

class PeliculaSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = "pelicula-detail"
    )

    class Meta:
        model = Pelicula
        fields = ["titulo", "fecha_creacion", "fecha_actualizacion", "director",
        "codigo_episodio", "texto_apertura", "productor", "fecha_emision", "url"
        ]


