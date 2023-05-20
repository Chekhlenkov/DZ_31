from django.contrib.auth.models import AbstractUser
from django.db import models

from users.validators import checkBDay, chek_email


class Location(models.Model):
    name = models.CharField("Название", max_length=100, unique=True)
    lat = models.DecimalField("Латтитуда", max_digits=8, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField("Лонгитуда", max_digits=8, decimal_places=6, null=True, blank=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"


class UserRoles(models.TextChoices):
    MEMBER = 'member', 'Пользователь'
    ADMIN = 'admin', 'Админ'
    MODERATOR = 'moderator', 'Модератор'


class User(AbstractUser):
    role = models.CharField(choices=UserRoles.choices, max_length=9, default=UserRoles.MEMBER)
    age = models.PositiveIntegerField(null=True)
    location = models.ManyToManyField(Location)
    birth_date = models.DateField(validators=[checkBDay], null=True)
    email = models.EmailField(unique=True, null=True, validators=[chek_email])

    def save(self, *args, **kwargs):
        self.set_password(raw_password=self.password)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["username"]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
