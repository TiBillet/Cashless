# Generated by Django 2.2 on 2024-11-29 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIcashless', '0244_auto_20241128_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='siret',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
