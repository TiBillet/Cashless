# Generated by Django 2.2 on 2021-05-24 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIcashless', '0049_auto_20210524_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupementcategorie',
            name='serveur_impression',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name="Adresse du serveur d'impression"),
        ),
        migrations.AlterField(
            model_name='groupementcategorie',
            name='thermal_printer_adress',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name="Adresse locale de l'imprimante ( usb ou ip )"),
        ),
        migrations.AlterField(
            model_name='groupementcategorie',
            name='thermal_printer_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name="Nom de l'imprimante"),
        ),
    ]
