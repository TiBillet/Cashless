# Generated by Django 2.2 on 2023-06-19 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIcashless', '0164_auto_20230504_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlevendu',
            name='prix_achat',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
