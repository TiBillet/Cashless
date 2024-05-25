# Generated by Django 2.2 on 2024-05-25 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIcashless', '0228_auto_20240521_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='subscription_type',
            field=models.CharField(choices=[('N', 'Non applicable'), ('Y', '365 Jours'), ('M', '30 Jours'), ('D', '1 Jour'), ('H', '1 Heure'), ('C', 'Civile')], default='N', max_length=1, verbose_name="durée d'abonnement"),
        ),
    ]