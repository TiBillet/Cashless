# Generated by Django 2.2 on 2021-05-24 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APIcashless', '0048_auto_20210524_0738'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='table',
            options={'ordering': ('poids',), 'verbose_name': 'Table', 'verbose_name_plural': 'Tables'},
        ),
        migrations.RenameField(
            model_name='configuration',
            old_name='serveur',
            new_name='serveur_impression',
        ),
    ]
