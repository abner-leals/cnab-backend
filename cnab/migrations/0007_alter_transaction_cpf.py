# Generated by Django 4.1.3 on 2022-11-28 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cnab", "0006_alter_transaction_store_delete_store"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="cpf",
            field=models.CharField(max_length=12),
        ),
    ]
