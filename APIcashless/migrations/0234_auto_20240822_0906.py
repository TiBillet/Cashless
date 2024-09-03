# Generated by Django 2.2 on 2024-08-22 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIcashless', '0233_auto_20240814_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloturecaisse',
            name='categorie',
            field=models.CharField(choices=[('K', 'Custom'), ('P', "Cloture d'un point de vente"), ('C', 'Cloture de toutes caisses'), ('H', 'Rapport hebdomadaire'), ('M', 'Rapport mensuel'), ('A', 'Rapport annuel')], default='C', max_length=1),
        ),
    ]