# Generated by Django 2.2 on 2024-05-14 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIcashless', '0225_auto_20240404_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='string_connect',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Entrez la clé FEDOW pour activer le modèle fédéré :'),
        ),
    ]
