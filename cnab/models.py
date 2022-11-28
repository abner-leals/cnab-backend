from django.db import models
import uuid


class TransactionType(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    description = models.CharField(max_length=50)
    nature = models.CharField(max_length=50)


class Transaction(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type = models.ForeignKey(
        "cnab.TransactionType", on_delete=models.CASCADE, related_name="transaction"
    )
    day = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    cpf = models.CharField(max_length=12)
    card = models.CharField(max_length=12)
    hour = models.TimeField()
    owner = models.CharField(max_length=20)
    store = models.CharField(max_length=30)
