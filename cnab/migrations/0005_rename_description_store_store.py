# Generated by Django 4.1.3 on 2022-11-28 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cnab", "0004_store_alter_transaction_store"),
    ]

    operations = [
        migrations.RenameField(
            model_name="store",
            old_name="description",
            new_name="store",
        ),
    ]
