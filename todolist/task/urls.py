from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, TarefaViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r'usuario', UsuarioViewSet)
router.register(r'tarefa', TarefaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]