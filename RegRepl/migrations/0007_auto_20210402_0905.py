# Generated by Django 3.1.2 on 2021-04-01 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegRepl', '0006_auto_20210402_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departament',
            name='subdep',
            field=models.ManyToManyField(blank=True, to='RegRepl.SubDepartament', verbose_name='Cубподразделения '),
        ),
        migrations.AlterField(
            model_name='dirdepartament',
            name='dep',
            field=models.ManyToManyField(blank=True, to='RegRepl.Departament', verbose_name='Подразделения '),
        ),
    ]
