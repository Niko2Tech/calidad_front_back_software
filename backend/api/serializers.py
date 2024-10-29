from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import ServicioStreaming, RegistroHuellaCarbono, UsuarioPremium, ReporteAdmin


class ServicioStreamingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicioStreaming
        fields = ['id', 'nombre', 'consumo_energia', 'factor_huella_carbono']


class RegistroHuellaCarbonoSerializer(serializers.ModelSerializer):
    nombre_servicio = serializers.CharField(
        source='servicio_streaming.nombre', read_only=True)

    class Meta:
        model = RegistroHuellaCarbono
        fields = ['id', 'usuario', 'servicio_streaming', 'nombre_servicio',
                  'fecha', 'horas_uso', 'co2_calculado']
        read_only_fields = ['fecha', 'co2_calculado']


class UsuarioPremiumSerializer(serializers.ModelSerializer):
    # Para mostrar el nombre del usuario en lugar del ID
    usuario = serializers.StringRelatedField()

    class Meta:
        model = UsuarioPremium
        fields = ['id', 'usuario', 'fecha_suscripcion']
        read_only_fields = ['fecha_suscripcion']


class ReporteAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteAdmin
        fields = ['id', 'fecha_generacion',
                  'promedio_huella_carbono', 'total_consultas']
        read_only_fields = ['fecha_generacion']
