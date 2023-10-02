import uuid

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseModel(models.Model):
    fecha_creacion = models.DateTimeField(null=True, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False,
                                        editable=False,
                                        related_name='%(app_label)s_%(class)s_related_crea',
                                        default=1,
                                        on_delete=models.CASCADE)
    fecha_ult_mod = models.DateTimeField(null=True,
                                         auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=False,
                                        editable=False,
                                        related_name='%(app_label)s_%(class)s_related_modif',
                                        default=1,
                                        on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Concepto(BaseModel):
    OPCIONES_DOMINIO = ((1, 'Imagenes'), (2, 'Procedimientos'), (3, 'Laboratorio'))
    fsn = models.CharField('Fully Specified Name', max_length=255, )
    dominio = models.IntegerField(choices=OPCIONES_DOMINIO, default=1)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    def __str__(self):
        return self.fsn

    class Meta:
        ordering = ['id']
        verbose_name_plural = "conceptos"