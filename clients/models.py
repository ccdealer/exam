import uuid
from datetime import timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from dirtyfields import DirtyFieldsMixin


class Client(DirtyFieldsMixin, AbstractUser):
    email = models.EmailField(
        verbose_name="email",
        unique=True,
        max_length=100
    )
    is_active = models.BooleanField(
        verbose_name="Активен",
        default=True
    )
    activation_code = models.UUIDField(
        verbose_name="Код активации",unique=True, null=True, blank=True
    )
    code_experetion_date = models.DateTimeField(
        verbose_name="Срок годности кода",
        null=True
    )

    USERNAME_FIELD = "email"     
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ("id",)
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.pk} - {self.username} - {self.email}"

    def save(self, *args, **kwargs):
        now = timezone.now()
        if self.is_superuser:
            self.is_active = True
            self.code_experetion_date = now
            return super().save(*args, **kwargs)
    
        if not self.pk:
            print("if 2 activated")
            self.code_experetion_date = now + timedelta(minutes=3)
    
        return super().save(*args, **kwargs)
    

