# Generated by Django 3.1.2 on 2021-04-06 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RegRepl', '0005_auto_20210407_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regularreplacementpos',
            name='dep',
            field=models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='RegRepl.departament', verbose_name='Подразделение '),
        ),
        migrations.AlterField(
            model_name='regularreplacementpos',
            name='dir',
            field=models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='RegRepl.dirdepartament', verbose_name='Дирекция '),
        ),
    ]
