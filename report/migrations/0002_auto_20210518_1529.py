# Generated by Django 3.2.3 on 2021-05-18 12:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plan',
            options={'verbose_name': 'План', 'verbose_name_plural': 'План'},
        ),
        migrations.AlterModelOptions(
            name='spr1_kvr',
            options={'verbose_name': 'Справочник 1 (КВР)', 'verbose_name_plural': 'Справочник 1 (КВР)'},
        ),
        migrations.AlterModelOptions(
            name='spr2_okved2',
            options={'verbose_name': 'Справочник 2 (ОКВЕД2)', 'verbose_name_plural': 'Справочник 2 (ОКВЕД2)'},
        ),
        migrations.AlterModelOptions(
            name='spr3_okpd2',
            options={'verbose_name': 'Справочник 3 (ОКПД2)', 'verbose_name_plural': 'Справочник 3 (ОКПД2)'},
        ),
        migrations.AlterModelOptions(
            name='spr4_requirements',
            options={'verbose_name': 'Справочник 4 (требования)', 'verbose_name_plural': 'Справочник 4 (требования)'},
        ),
        migrations.AlterModelOptions(
            name='spr5_unit',
            options={'verbose_name': 'Справочник 5 (единица измерения)', 'verbose_name_plural': 'Справочник 5 (единица измерения)'},
        ),
        migrations.AlterModelOptions(
            name='spr6_region',
            options={'verbose_name': 'Справочник 6 (Регион поставки)', 'verbose_name_plural': 'Справочник 6 (Регион поставки)'},
        ),
        migrations.AlterModelOptions(
            name='spr7_method',
            options={'verbose_name': 'Справочник 7 (способ закупки)', 'verbose_name_plural': 'Справочник 7 (способ закупки)'},
        ),
        migrations.AlterModelOptions(
            name='spr8_result',
            options={'verbose_name': 'Справочник 8 (результат)', 'verbose_name_plural': 'Справочник 8 (результат)'},
        ),
        migrations.AlterField(
            model_name='plan',
            name='data_placing',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата размещения'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='term_execution',
            field=models.DateField(default=datetime.date.today, verbose_name='Срок размещения'),
        ),
    ]