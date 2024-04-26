# Generated by Django 2.2 on 2022-03-30 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIcashless', '0110_auto_20220326_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Odoologs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('log', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='configuration',
            name='odoo_create_invoice_membership',
            field=models.BooleanField(default=True, verbose_name='Créer les facture pour chaque adhésion'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='odoo_login',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='configuration',
            name='odoo_set_payment_auto',
            field=models.BooleanField(default=False, verbose_name='Valider le paiement automatiquement'),
        ),
    ]