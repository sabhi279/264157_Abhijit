# Generated by Django 5.1.3 on 2025-04-29 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bankaccount",
            name="balance",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
