# Generated by Django 2.2 on 2023-07-18 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIcashless', '0173_auto_20230718_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='prix',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Prix de vente'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='prix_achat',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name="Prix d'achat"),
        ),
        migrations.AlterField(
            model_name='articlevendu',
            name='prix',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='articlevendu',
            name='prix_achat',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]