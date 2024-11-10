from django.db import models
from ..core.auth_model import UserAuthModel

PRIORIDADES_TAREA = [("alta", "Alta"), ("media", "Media"), ("baja", "Baja")]

ESTADOS_TAREA = [
    ("pendiente", "Pendiente"),
    ("en_progreso", "En progreso"),
    ("revision", "En revisión"),
    ("impediemnto", "Impedimento"),
    ("completada", "Completada"),
]


class TareaModel(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_inicio = models.DateTimeField()
    fecha_vencimiento = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    prioridad = models.CharField(
        max_length=10, choices=PRIORIDADES_TAREA, default="media"
    )
    usuario_asignado = models.ForeignKey(
        UserAuthModel, 
        related_name='tarea',
        on_delete=models.CASCADE
    )
    categoria = models.CharField(max_length=100, null=True, blank=True)
    tiempo_estimado = models.DurationField(null=True, blank=True)
    tiempo_real = models.ManyToManyField("self", symmetrical=False, blank=True)
    tags = models.TextField()
    estado = models.CharField(
        max_length=20, 
        choices=ESTADOS_TAREA, 
        default="pendiente"
    )
