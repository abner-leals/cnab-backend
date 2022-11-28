# Generated by Django 4.1.3 on 2022-11-27 08:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TransactionType",
            fields=[
                (
                    "id",
                    models.IntegerField(primary_key=True, serialize=False, unique=True),
                ),
                ("description", models.CharField(max_length=50)),
                ("nature", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("date", models.DateField()),
                ("value", models.DecimalField(decimal_places=2, max_digits=10)),
                ("cpf", models.IntegerField()),
                ("card", models.CharField(max_length=12)),
                ("hour", models.TimeField()),
                ("owner", models.CharField(max_length=20)),
                ("store", models.CharField(max_length=30)),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="transaction",
                        to="cnab.transactiontype",
                    ),
                ),
            ],
        ),
    ]
