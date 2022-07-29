from django.db import models
from django.core.validators import MaxValueValidator
from numpy import require

from .constants import province_choices

# Create your models here.
class WorkLoad(models.Model):
    province = models.CharField(
        choices=province_choices,
        max_length=30,
        null=False,
        blank=False,
        verbose_name = "จังหวัด"
    )
    
    hospital_name = models.CharField(
        null=False, 
        max_length=50, 
        default="", 
        verbose_name = "Hospital")
    opd = models.PositiveIntegerField(
        default=0, 
        null = False, 
        blank=False,
        verbose_name = "OPD (จำนวนคนต่อ 1 อาทิตย์)",
        validators=[MaxValueValidator(4000)]
    )
    ipd =  models.PositiveIntegerField(
        default=0, 
        null = False, 
        blank=False,
        verbose_name = "IPD (จำนวนครั้งในการ round ต่อ 1 อาทิตย์)",
        validators=[MaxValueValidator(4000)]
    )
    er =  models.PositiveIntegerField(
        default=0, 
        null = False, 
        blank=False,
        verbose_name = "ER (จำนวนคนต่อ 1 อาทิตย์)",
        validators=[MaxValueValidator(4000)]
    )
    icu =  models.PositiveIntegerField(
        default=0, 
        null = False, 
        blank=False, 
        verbose_name = "ICU (จำนวนครั้งในการ round ต่อ 1 อาทิตย์)",
        validators=[MaxValueValidator(4000)]
    )
    labour =  models.PositiveIntegerField(
        default=0, 
        null = False, 
        blank=False, 
        verbose_name = "Normal labour (จำนวนคนต่อ 1 อาทิตย์)",
        validators=[MaxValueValidator(4000)]
    )



