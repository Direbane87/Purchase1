# Generated by Django 3.2.3 on 2021-05-18 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spr1_kvr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kvr', models.PositiveSmallIntegerField(verbose_name='КВР')),
                ('analytical_code', models.CharField(max_length=10, verbose_name='Анал.код')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Справочник 1 (КВР)',
            },
        ),
        migrations.CreateModel(
            name='Spr2_okved2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=20, verbose_name='Раздел')),
                ('description', models.TextField(verbose_name='Наименование')),
                ('parent', models.CharField(max_length=20, verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Справочник 2 (ОКВЕД2)',
            },
        ),
        migrations.CreateModel(
            name='Spr3_okpd2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=20, verbose_name='Раздел')),
                ('description', models.TextField(verbose_name='Наименование')),
                ('parent', models.CharField(max_length=20, verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Справочник 3 (ОКПД2)',
            },
        ),
        migrations.CreateModel(
            name='Spr4_requirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Справочник 4 (требования)',
            },
        ),
        migrations.CreateModel(
            name='Spr5_unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.PositiveSmallIntegerField(verbose_name='Код')),
                ('name', models.CharField(max_length=25, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Справочник 5 (единица измерения)',
            },
        ),
        migrations.CreateModel(
            name='Spr6_region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15, verbose_name='Код региона')),
                ('name', models.CharField(max_length=25, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Справочник 6 (Регион поставки)',
            },
        ),
        migrations.CreateModel(
            name='Spr7_method',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=150, verbose_name='Способ')),
                ('point', models.CharField(max_length=15, verbose_name='Пункт')),
            ],
            options={
                'verbose_name': 'Справочник 7 (способ закупки)',
            },
        ),
        migrations.CreateModel(
            name='Spr8_result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Результат')),
            ],
            options={
                'verbose_name': 'Справочник 8 (результат)',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_contract', models.TextField(verbose_name='Предмет договора')),
                ('info_quantity', models.PositiveSmallIntegerField(verbose_name='Сведения о количестве')),
                ('info_start_price', models.PositiveSmallIntegerField(default=0, verbose_name='Начальная цена')),
                ('g2021', models.PositiveSmallIntegerField(default=0, verbose_name='2021')),
                ('g2022', models.PositiveSmallIntegerField(default=0, verbose_name='2022')),
                ('g2023', models.PositiveSmallIntegerField(default=0, verbose_name='2023')),
                ('g2024', models.PositiveSmallIntegerField(default=0, verbose_name='2024')),
                ('next', models.PositiveSmallIntegerField(default=0, verbose_name='Последующие')),
                ('data_placing', models.CharField(max_length=15, verbose_name='Дата размещения')),
                ('term_execution', models.CharField(max_length=15, verbose_name='Срок размещения')),
                ('electronic_form', models.BooleanField(default=False)),
                ('smp', models.BooleanField(default=False)),
                ('source_finance', models.CharField(max_length=40, verbose_name='Источник финансирования')),
                ('executor_human', models.CharField(max_length=150, verbose_name='Отв. исполнитель')),
                ('executor', models.CharField(max_length=255, verbose_name='Испольнитель')),
                ('number_contract', models.CharField(max_length=100, verbose_name='Номер договора')),
                ('kvr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.spr1_kvr', verbose_name='КВР')),
                ('method', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.spr7_method', verbose_name='Способ')),
                ('min_req', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.spr4_requirements', verbose_name='Мин. требования')),
                ('okpd2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.spr3_okpd2', verbose_name='ОКПД2')),
                ('okved2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.spr2_okved2', verbose_name='ОКВЕД2')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.spr6_region', verbose_name='Регион')),
                ('result', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.spr8_result', verbose_name='Результат')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.spr5_unit', verbose_name='Единица измерения')),
            ],
            options={
                'verbose_name': 'План',
            },
        ),
    ]