from rest_framework.routers import DefaultRouter
from api.views import ServicioStreamingViewSet, RegistroHuellaCarbonoViewSet, UsuarioPremiumViewSet, ReporteAdminViewSet

router = DefaultRouter()
router.register(r'servicios-streaming', ServicioStreamingViewSet)
router.register(r'registros-huella-carbono', RegistroHuellaCarbonoViewSet)
router.register(r'usuarios-premium', UsuarioPremiumViewSet)
router.register(r'reportes-admin', ReporteAdminViewSet)

urlpatterns = router.urls
