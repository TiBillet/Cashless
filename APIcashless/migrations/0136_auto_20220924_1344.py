# Generated by Django 2.2 on 2022-09-24 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIcashless', '0135_auto_20220924_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='cashback_active',
            field=models.BooleanField(default=False, verbose_name='Activez le cashbash pour les paiements en ligne'),
        ),
    ]