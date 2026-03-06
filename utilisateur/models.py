from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    photo_de_profile = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Photo de profil"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description"
    )
    age = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Âge"
    )
    lien_cv = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="Lien CV"
    )
    telephone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Téléphone"
    )

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"

    def __str__(self):
        return self.username
