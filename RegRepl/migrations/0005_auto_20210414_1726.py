# Generated by Django 3.1.2 on 2021-04-14 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RegRepl', '0004_auto_20210414_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subdepartament',
            name='location',
            field=models.ForeignKey(max_length=256, on_delete=django.db.models.deletion.CASCADE, to='RegRepl.location', verbose_name='Территория '),
        ),
    ]