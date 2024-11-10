from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.core.auth_view import AuthViewSet
from .views.modules.tarea_view import TareaViewSet

router = DefaultRouter()
router.register(r'auth', AuthViewSet, basename='auth')
router.register(r'tarea', TareaViewSet, basename='tarea')

urlpatterns = [
    path('', include(router.urls)),
]
