from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models

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
    pass
