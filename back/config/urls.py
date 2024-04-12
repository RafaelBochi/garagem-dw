from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from usuario.router import router as usuario_router
from usuario import views
from app.views import AcessorioViewSet, CarroViewSet, CategoriaViewSet, CorViewSet, MarcaViewSet

router = DefaultRouter()
router.register(r"acessorios", AcessorioViewSet)
router.register(r"carros", CarroViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"cores", CorViewSet)
router.register(r"marcas", MarcaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(usuario_router.urls)),
    path("", include(router.urls)),

    path("api/user/login/", views.login, name="login"),
    path("api/user/register/", views.register, name="register"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
