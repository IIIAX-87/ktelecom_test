import re

from django.core.exceptions import ValidationError
from django.db import models

'''Класс для маски серийного номера'''


class MaskField(models.CharField):
    def clean(self, value, model_instance):
        value = super(MaskField, self).clean(value, model_instance)
        if not re.match(r'[NAaXZ]+', value):
            raise ValidationError('NAaXZ characters only.')
        return value


'''Класс для типа оборудования'''


class EquipmentType(models.Model):
    name = models.CharField(max_length=100, blank=False)
    mask = MaskField(max_length=50, blank=False)


'''Класс для оборудования'''


class Equipment(models.Model):
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)

