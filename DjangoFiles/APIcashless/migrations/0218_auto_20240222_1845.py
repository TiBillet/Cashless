# Generated by Django 2.2 on 2024-02-22 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIcashless', '0217_configuration_journal_out_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='pin_code_primary_link',
            field=models.CharField(blank=True, editable=False, max_length=8, null=True, verbose_name='Code PIN pour appareillement'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='domaine_cashless',
            field=models.URLField(blank=True, null=True, verbose_name='Url publique du serveur cashless'),
        ),
    ]
