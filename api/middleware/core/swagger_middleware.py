# api/middleware/swagger_middleware.py
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import AnonymousUser

class SwaggerFakeUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Si es una solicitud de Swagger para generar la documentación
        if getattr(request, 'swagger_fake_view', False):
            # Asigna un usuario anónimo para Swagger
            request.user = AnonymousUser()
            # También elimina la autenticación requerida para Swagger
            request.META['HTTP_AUTHORIZATION'] = ''
        return None
