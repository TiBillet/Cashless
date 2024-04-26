# Generated by Django 2.2 on 2022-10-31 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIcashless', '0139_cartecashless_recharge_suspendue'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartemaitresse',
            options={'verbose_name': 'Carte primaire', 'verbose_name_plural': 'Cartes primaires'},
        ),
        migrations.AddField(
            model_name='moyenpaiement',
            name='is_federated',
            field=models.BooleanField(default=False),
        ),
    ]