# Generated by Django 2.2 on 2021-10-06 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIcashless', '0084_auto_20211005_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecommandesauvegarde',
            name='reste_a_servir',
            field=models.FloatField(default=0),
        ),
    ]
