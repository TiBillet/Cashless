# Generated by Django 2.2 on 2021-07-10 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIcashless', '0065_configuration_remboursement_auto_annulation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groupementcategorie',
            options={'verbose_name': 'Préparation & impréssion', 'verbose_name_plural': 'Préparations & impréssions'},
        ),
        migrations.AlterField(
            model_name='commandesauvegarde',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]