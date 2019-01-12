from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

from common import storage

# Create your models here.


class CreationModificationDateMixin(models.Model):
    """
    Abstract base class with a creation and modification
    date and time
    """

    class Meta:
        abstract = True

    creation = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Creation time'),
    )
    modification = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Last modification time'),
    )


class User(AbstractUser):
    """Custom user manager to allow future expansion."""
    pass


class File(CreationModificationDateMixin):
    titulo = models.CharField(
        max_length=140,
    )
    descripcion = models.CharField(
        max_length=255,
    )
    file = models.FileField(upload_to=settings.GDRIVE_STORAGE_PRENAME,
                            storage=storage.gd_storage)
