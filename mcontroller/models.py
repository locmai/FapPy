from django.core.validators import MinValueValidator
from django.db import models

from django.contrib.auth.models import User


class Masturbation(models.Model):
    m_date = models.DateTimeField(auto_now_add=True)  # Masturbation date
    m_reason = models.CharField(max_length=200, null=True)  # Reason lead to the masturbation
    m_method = models.CharField(max_length=100, null=True)  # Methodology
    m_duration = models.FloatField(default=1, validators=[MinValueValidator(0.1)])  # Duration
    m_user = models.ForeignKey(User, related_name='masturbations', on_delete=models.DO_NOTHING,null=True)