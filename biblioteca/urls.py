from rest_framework import routers
from .views import BibliotecaViewset

router = routers.DefaultRouter()
router.register(r'biblioteca', BibliotecaViewset) #registrando o url da bibliotecaviewset em /biblioteca
urlpatterns = router.urls #rotas registradas em router irão para urlpatterns