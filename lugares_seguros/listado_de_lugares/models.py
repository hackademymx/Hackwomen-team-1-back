from django.db import models

# Create your models here.


class listado_de_lugares(models.Model):

    name = models.CharField(max_length=56)
    description = models.CharField(max_length=256)
    address_state = models.CharField(max_length=32)
    address_city = models.CharField(max_length=32)
    address_colonia = models.CharField(max_length=32)
    address_street = models.CharField(max_length=32)
    address_zipcode = models.CharField(max_length=32)

    class Meta:
        db_table = 'listado_de_lugares'

    def __str__(self):
        return self.name
    