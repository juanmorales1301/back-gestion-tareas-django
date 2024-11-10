from rest_framework import serializers
from ...models.modules.tarea_model import TareaModel


class TareaSerializer(serializers.ModelSerializer):
    usuario_asignado = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = TareaModel
        fields = [
            "id",
            "titulo",
            "descripcion",
            "fecha_creacion",
            "fecha_inicio",
            "fecha_vencimiento",
            "fecha_actualizacion",
            "prioridad",
            "usuario_asignado",
            "categoria",
            "tiempo_estimado",
            "tiempo_real",
            "tags",
            "estado",
        ]
        read_only_fields = ["usuario_asignado", "fecha_creacion", "fecha_actualizacion"]
