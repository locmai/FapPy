from django.db import models
from django.contrib.auth.models import User


class UserManagement(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.DO_NOTHING, null=True)
    supervisor = models.ForeignKey(User, related_name='supervisor', on_delete=models.DO_NOTHING, null=True)


class UserKey(models.Model):
    supervisor_user = models.ForeignKey(User, related_name='user_key', on_delete=models.DO_NOTHING, null=False)
    key = models.CharField(max_length=150)