# Generated by Django 2.2 on 2021-05-24 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIcashless', '0050_auto_20210524_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupementcategorie',
            name='api_serveur_impression',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name="Clé d'api pour serveur d'impression"),
        ),
    ]