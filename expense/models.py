from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount=models.FloatField()
    notes = models.TextField()
    created_timestamp   = models.DateTimeField(auto_now=True)
    updated_timestamp   = models.DateTimeField(auto_now=True)
