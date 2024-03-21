from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class montos(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    ingresos = models.IntegerField()
    gastos = models.IntegerField()
    saldo = models.IntegerField()
    
    def __str__(self):
        return f'{self.user.username}: {self.saldo}'