# Generated by Django 2.2 on 2021-04-09 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIcashless', '0010_auto_20210409_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='statut',
            field=models.CharField(choices=[('L', 'Libre'), ('O', 'En cours de service'), ('S', 'Servie, en attente de paiement')], default='L', max_length=1),
        ),
    ]