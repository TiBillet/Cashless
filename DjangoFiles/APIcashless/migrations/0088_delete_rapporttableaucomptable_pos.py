# Generated by Django 2.2 on 2021-10-06 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APIcashless', '0087_remove_rapporttableaucomptable_pos_monnaie'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RapportTableauComptable_POS',
        ),
    ]
