# Generated by Django 3.1.7 on 2022-03-28 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RegRepl', '0003_auto_20220328_1614'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dirdepartament',
            options={'ordering': ['id'], 'verbose_name': 'Дирекция'},
        ),
        migrations.RemoveField(
            model_name='dirdepartament',
            name='iter',
        ),
    ]
