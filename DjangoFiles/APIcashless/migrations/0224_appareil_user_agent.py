# Generated by Django 2.2 on 2024-04-03 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIcashless', '0223_auto_20240402_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='appareil',
            name='user_agent',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
