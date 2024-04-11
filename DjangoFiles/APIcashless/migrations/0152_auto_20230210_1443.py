# Generated by Django 2.2 on 2023-02-10 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APIcashless', '0151_remove_assets_asset_categorie'),
    ]

    operations = [
        migrations.CreateModel(
            name='TauxTVA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('taux', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Taux')),
            ],
            options={
                'verbose_name': 'Taux TVA',
                'verbose_name_plural': 'Taux TVA',
            },
        ),
        migrations.AddField(
            model_name='articlevendu',
            name='tva',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Taux'),
        ),
        migrations.AlterField(
            model_name='moyenpaiement',
            name='categorie',
            field=models.CharField(choices=[('LE', 'Token local €'), ('LG', 'Token local cadeau'), ('FR', 'Fractionné'), ('AR', 'Ardoise'), ('SF', 'Token Federated Stripe'), ('SN', 'Stripe no federated'), ('CA', 'Espèces'), ('CC', 'Carte bancaire TPE'), ('CH', 'Cheque'), ('OC', 'Oceco')], default='LE', max_length=2),
        ),
        migrations.AddField(
            model_name='categorie',
            name='tva',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tva_categorie', to='APIcashless.TauxTVA'),
        ),
    ]