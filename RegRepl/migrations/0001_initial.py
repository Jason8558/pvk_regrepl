# Generated by Django 3.1.2 on 2021-04-06 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
    migrations.CreateModel(
        name='Location',
        fields=[
            ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('name', models.CharField(max_length=256, verbose_name='Наименование ')),
        ],
        options={
            'verbose_name': 'Территория',
            'ordering': ['id'],
        },
    ),
        migrations.CreateModel(
            name='Departament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='Введите название подразделения', max_length=256, verbose_name='Название подразделения ')),
            ],
            options={
                'verbose_name': 'Подразделение',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DirDepartament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='Введите название дирекции', max_length=256, verbose_name='Название дирекции ')),
                ('dep', models.ManyToManyField(blank=True, to='RegRepl.Departament', verbose_name='Подразделения ')),
            ],
            options={
                'verbose_name': 'Дирекция',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='Введите ФИО сотрудника', max_length=256, verbose_name='Сотрудник ')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='RegularReplacement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.DateField(db_index=True, help_text='Введите дату', verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Штатное замещение',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SubDepartament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='Введите название субподразделения', max_length=256, verbose_name='Название субподразделения ')),
            ],
            options={
                'verbose_name': 'Субподразделение',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='RegularReplacementPos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='Введите должность', max_length=256, verbose_name='Название должности ')),
                ('units', models.IntegerField(db_index=True, max_length=256, verbose_name='Кол-во едениц по штатному расписанию ')),
                ('level', models.CharField(blank=True, max_length=256, verbose_name='Разряд по штатному расписанию')),
                ('cat', models.CharField(choices=[('РУК', 'РУК'), ('СПЕЦ', 'СПЕЦ'), ('РАБ', 'РАБ')], max_length=256, verbose_name='Категория по штатному расписанию ')),
                ('payment', models.CharField(max_length=3, verbose_name='Ступень оплаты по штатному расписанию')),
                ('salary', models.CharField(db_index=True, max_length=256, verbose_name='Оклад по штатному расписанию ')),
                ('units_rr', models.IntegerField(db_index=True, max_length=256, verbose_name='Кол-во едениц по штатному замещению ')),
                ('level_rr', models.CharField(blank=True, max_length=256, verbose_name='Разряд по штатному замещению')),
                ('cat_rr', models.CharField(choices=[('РУК', 'РУК'), ('СПЕЦ', 'СПЕЦ'), ('РАБ', 'РАБ')], max_length=256, verbose_name='Категория по штатному замещению ')),
                ('payment_rr', models.CharField(max_length=3, verbose_name='Ступень оплаты по штатному замещению')),
                ('salary_rr', models.CharField(db_index=True, max_length=256, verbose_name='Оклад по штатному замещению ')),
                ('employer1', models.CharField(blank=True, db_index=True, default='', max_length=256, verbose_name='Сотрудник 1 ')),
                ('employer2', models.CharField(blank=True, db_index=True, default='', max_length=256, verbose_name='Сотрудник 2 ')),
                ('employer3', models.CharField(blank=True, db_index=True, default='', max_length=256, verbose_name='Сотрудник 3 ')),
                ('free', models.BooleanField(default=False, verbose_name='Ставка свободна ')),
                ('comm', models.CharField(blank=True, db_index=True, default='', max_length=256, verbose_name='Комментарий ')),
                ('bound_regrepl', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='RegRepl.regularreplacement', verbose_name='Штатное замещение ')),
                ('dep', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='RegRepl.departament', verbose_name='Подразделение ')),
                ('dir', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='RegRepl.dirdepartament', verbose_name='Дирекция ')),
                ('subdep', models.ForeignKey(blank=True, default='1', on_delete=django.db.models.deletion.CASCADE, to='RegRepl.subdepartament', verbose_name='Субподразделение ')),
            ],
            options={
                'verbose_name': 'Позиция штатного замещения',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='departament',
            name='subdep',
            field=models.ManyToManyField(blank=True, to='RegRepl.SubDepartament', verbose_name='Cубподразделения '),
        ),
    ]
