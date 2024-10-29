from django.db import models
from django.contrib.auth.models import User


class ServicioStreaming(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    consumo_energia = models.DecimalField(
        max_digits=10, decimal_places=2)
    factor_huella_carbono = models.DecimalField(
        max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


class RegistroHuellaCarbono(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    servicio_streaming = models.ForeignKey(
        ServicioStreaming, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    horas_uso = models.DecimalField(
        max_digits=5, decimal_places=2)  # tiempo de uso en horas
    co2_calculado = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)  # CO2 calculado

    def save(self, *args, **kwargs):
        # Cálculo básico de huella de carbono usando el factor del servicio
        if not self.co2_calculado:
            self.co2_calculado = self.horas_uso * \
                self.servicio_streaming.factor_huella_carbono
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.usuario} - {self.servicio_streaming} - {self.fecha}"


class UsuarioPremium(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_suscripcion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Usuario Premium: {self.usuario.username}"


class ReporteAdmin(models.Model):
    fecha_generacion = models.DateField(auto_now_add=True)
    promedio_huella_carbono = models.DecimalField(
        max_digits=10, decimal_places=2)
    total_consultas = models.IntegerField()

    def __str__(self):
        return f"Reporte - {self.fecha_generacion}"
