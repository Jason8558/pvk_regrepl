# Generated by Django 3.1.2 on 2021-04-14 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RegRepl', '0008_auto_20210415_0853'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4, verbose_name='Наименование ')),
            ],
            options={
                'verbose_name': 'Категория',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='regularreplacementpos',
            name='cat',
            field=models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, to='RegRepl.category', verbose_name='Категория '),
        ),
        migrations.AddField(
            model_name='regularreplacementpos',
            name='cat_rr',
            field=models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, related_name='cat_regrepl', to='RegRepl.category', verbose_name='Категория по штатному замещению '),
        ),
    ]