# Generated by Django 3.1.7 on 2022-03-28 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RegRepl', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departament',
            options={'ordering': ['id'], 'verbose_name': 'Подразделение'},
        ),
        migrations.RemoveField(
            model_name='departament',
            name='iter',
        ),
    ]