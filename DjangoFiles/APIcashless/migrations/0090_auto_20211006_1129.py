# Generated by Django 2.2 on 2021-10-06 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APIcashless', '0089_rapporttableaucomptable_pos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rapporttableaucomptable_pos',
            old_name='monnaie',
            new_name='moyen_paiement',
        ),
    ]