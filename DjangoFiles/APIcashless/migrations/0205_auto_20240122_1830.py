# Generated by Django 2.2 on 2024-01-22 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APIcashless', '0204_auto_20240117_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartecashless',
            name='origin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cards', to='APIcashless.Origin'),
        ),
    ]