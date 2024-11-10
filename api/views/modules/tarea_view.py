from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from ...serializers.modules.tarea_serialize import TareaSerializer
from ...models.modules.tarea_model import TareaModel


class TareaViewSet(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    permission_classes = [IsAuthenticated]

    # Obtiene todas las tareas
    def get_queryset(self):
        return TareaModel.objects.all()

    # Crea una tarea asignada al usuario autenticado
    def perform_create(self, serializer):
        serializer.save(usuario_asignado=self.request.user)

    # Lista todas las tareas
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(
            {
                "mensaje": "Consulta exitosa.",
                "code": "CO0001",
                "correcto": True,
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    # Crea una nueva tarea
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(
                {
                    "mensaje": "Tarea creada exitosamente.",
                    "code": "IN0001",
                    "correcto": True,
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Obtiene los detalles de una tarea específica
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(
            {
                "mensaje": "Consulta exitosa.",
                "code": "CO0003",
                "correcto": True,
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    # Actualiza una tarea completa
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(
                {
                    "mensaje": "Tarea actualizada exitosamente.",
                    "code": "UP0001",
                    "correcto": True,
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Actualización parcial de una tarea
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    # Elimina una tarea
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {
                "mensaje": "Tarea eliminada exitosamente.",
                "code": "DE0001",
                "correcto": True,
            },
            status=status.HTTP_204_NO_CONTENT,
        )

    # Función adicional para listar tareas por usuario_id
    @action(
        detail=False, methods=["get"], url_path="por-usuario/(?P<usuario_id>[^/.]+)"
    )
    def listar_por_usuario(self, request, usuario_id=None):
        tareas = TareaModel.objects.filter(usuario_asignado=usuario_id)
        if tareas.exists():
            serializer = self.get_serializer(tareas, many=True)
            return Response(
                {
                    "mensaje": "Consulta exitosa.",
                    "code": "CO0002",
                    "correcto": True,
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "mensaje": "No se encontraron tareas para el usuario especificado.",
                "code": "ER0002",
                "correcto": False,
            },
            status=status.HTTP_404_NOT_FOUND,
        )
