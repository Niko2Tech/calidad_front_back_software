from rest_framework import viewsets, permissions
from api.models import ServicioStreaming, RegistroHuellaCarbono, UsuarioPremium, ReporteAdmin
from api.serializers import ServicioStreamingSerializer, RegistroHuellaCarbonoSerializer, UsuarioPremiumSerializer, ReporteAdminSerializer

# ViewSet para ServicioStreaming


class ServicioStreamingViewSet(viewsets.ModelViewSet):
    queryset = ServicioStreaming.objects.all()
    serializer_class = ServicioStreamingSerializer
    permission_classes = [permissions.AllowAny]

# ViewSet para RegistroHuellaCarbono


class RegistroHuellaCarbonoViewSet(viewsets.ModelViewSet):
    queryset = RegistroHuellaCarbono.objects.all()
    serializer_class = RegistroHuellaCarbonoSerializer
    permission_classes = [permissions.AllowAny]

# ViewSet para UsuarioPremium


class UsuarioPremiumViewSet(viewsets.ModelViewSet):
    queryset = UsuarioPremium.objects.all()
    serializer_class = UsuarioPremiumSerializer
    permission_classes = [permissions.AllowAny]

# ViewSet para ReporteAdmin


class ReporteAdminViewSet(viewsets.ModelViewSet):
    queryset = ReporteAdmin.objects.all()
    serializer_class = ReporteAdminSerializer
    permission_classes = [permissions.AllowAny]
