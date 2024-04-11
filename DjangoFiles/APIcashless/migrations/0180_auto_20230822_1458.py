# Generated by Django 2.2 on 2023-08-22 10:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('APIcashless', '0179_auto_20230822_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartecashless',
            name='wallet',
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moyenpaiement',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]