# Generated by Django 2.2 on 2024-12-06 07:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('APIcashless', '0245_auto_20241129_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Terminal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nom')),
                ('stripe_id', models.CharField(blank=True, max_length=21, null=True, verbose_name='Stripe ID')),
                ('type', models.CharField(choices=[('W', 'bbpos_wisepos_e')], default='W', max_length=2, verbose_name='Type')),
            ],
        ),
        migrations.AlterModelOptions(
            name='groupementcategorie',
            options={'verbose_name': 'Préparation & impression', 'verbose_name_plural': 'Préparations & impressions'},
        ),
        migrations.AddField(
            model_name='configuration',
            name='stripe_api_key',
            field=models.CharField(blank=True, editable=False, max_length=110, null=True),
        ),
        migrations.AddField(
            model_name='configuration',
            name='stripe_location',
            field=models.CharField(blank=True, max_length=21, null=True),
        ),
        migrations.AddField(
            model_name='configuration',
            name='stripe_payouts_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='stripe_connect_account',
            field=models.CharField(blank=True, max_length=21, null=True),
        ),
        migrations.CreateModel(
            name='PaymentsIntent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.PositiveSmallIntegerField()),
                ('payment_intent_stripe_id', models.CharField(blank=True, max_length=30, null=True, verbose_name='Paiement intent stripe id')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('R', 'requires_payment_method'), ('P', 'in_progress'), ('A', 'Paiement autorisé, mais pas encore capturé'), ('S', 'Succes'), ('C', 'Canceled')], default='R', max_length=2, verbose_name='Status')),
                ('pos', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='APIcashless.PointDeVente', verbose_name='Point de vente')),
                ('terminal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='APIcashless.Terminal', verbose_name='TPE')),
            ],
        ),
        migrations.AddField(
            model_name='articlevendu',
            name='payment_intent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='APIcashless.PaymentsIntent', verbose_name='Paiement stripe'),
        ),
    ]
