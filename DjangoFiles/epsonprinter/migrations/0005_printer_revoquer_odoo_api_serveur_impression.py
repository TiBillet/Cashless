# Generated by Django 2.2 on 2022-08-17 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epsonprinter', '0004_auto_20220816_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='printer',
            name='revoquer_odoo_api_serveur_impression',
            field=models.BooleanField(default=False, help_text='Selectionnez et validez pour supprimer la clé API et entrer une nouvelle.', verbose_name='Révoquer la clé API'),
        ),
    ]
