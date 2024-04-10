# Generated by Django 2.2 on 2021-07-27 15:23

from django.db import migrations, models
from django.core.management import call_command
import django.db.models.deletion

def check_permission(apps, schema_editor):
    pass
    # call_command('check_permissions')


class Migration(migrations.Migration):

    dependencies = [
        ('APIcashless', '0069_auto_20210726_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='RapportFinancierGlobal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('recharge_monnaie_cashless', models.FloatField(default=0, verbose_name='Recharge Cashless')),
                ('recharge_monnaie_cashless_cadeau', models.FloatField(default=0, verbose_name='Recharge Cadeau')),
                ('recharge_monnaie_cashless_cadeau_depuis_oceco', models.FloatField(default=0, verbose_name='Depuis OCECO')),
                ('total_espece', models.FloatField(default=0, verbose_name='Espece')),
                ('total_carte_bancaire', models.FloatField(default=0, verbose_name='CB')),
                ('total_web_mollie', models.FloatField(default=0, verbose_name='Web')),
                ('remboursement_monnaie_espece', models.FloatField(default=0, verbose_name='Remboursement')),
                ('remboursement_monnaie_web', models.FloatField(default=0, verbose_name='Remboursement Web')),
                ('total_adhesion', models.FloatField(default=0, verbose_name='Adhésion')),
                ('total_vente_en_monnaie_cashless', models.FloatField(default=0, verbose_name='Dépense Cashless')),
                ('total_vente_en_monnaie_cashless_cadeau', models.FloatField(default=0, verbose_name='Dépense Cadeau')),
                ('total_reste_sur_carte', models.FloatField(default=0)),
                ('_depart_caisse_total', models.FloatField(default=0)),
                ('_cloture_caisse_total', models.FloatField(default=0)),
            ],
            options={
                'verbose_name': 'R. Financier',
                'verbose_name_plural': 'R. Financiers',
                'ordering': ('-date',),
            },
        ),
        migrations.AlterModelOptions(
            name='articlevendu',
            options={'ordering': ('-date_time',), 'verbose_name': 'Detail', 'verbose_name_plural': 'Detail'},
        ),
        migrations.AlterModelOptions(
            name='rapportarticlesvendu',
            options={'ordering': ('-date',), 'verbose_name': 'Quantités vendus', 'verbose_name_plural': 'Quantités vendus'},
        ),
        migrations.AlterModelOptions(
            name='rapportbar',
            options={'ordering': ('-date',), 'verbose_name': 'EX Rapport caisse', 'verbose_name_plural': 'EX Rapports caisse'},
        ),
        migrations.CreateModel(
            name='RapportPointsDeVente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('vente_en_monnaie_cashless', models.FloatField(default=0)),
                ('vente_en_monnaie_cashless_cadeau', models.FloatField(default=0)),
                ('articles_offerts', models.FloatField(default=0)),
                ('vente_directe_en_carte_bancaire', models.FloatField(default=0)),
                ('vente_directe_en_espece', models.FloatField(default=0)),
                ('adhesions', models.FloatField(default=0)),
                ('depart_caisse', models.FloatField(default=0)),
                ('cloture_caisse', models.FloatField(default=0)),
                ('pos', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='APIcashless.PointDeVente', verbose_name='Points de vente')),
            ],
        ),
        migrations.RunPython(check_permission),
    ]
