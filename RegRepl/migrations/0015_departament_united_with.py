# Generated by Django 3.1.7 on 2022-03-24 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RegRepl', '0014_auto_20220324_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='departament',
            name='united_with',
            field=models.ForeignKey(default='1', max_length=256, on_delete=django.db.models.deletion.CASCADE, to='RegRepl.departament', verbose_name='Объеденить с  '),
        ),
    ]