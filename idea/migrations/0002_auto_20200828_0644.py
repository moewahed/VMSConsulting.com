# Generated by Django 2.2 on 2020-08-28 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='topic',
            field=models.IntegerField(choices=[('1', 'Computer Science'), ('2', 'Medical'), ('3', 'Marketing'), ('4', 'Business'), ('5', 'Sport'), ('6', 'Places'), ('7', 'Development'), ('8', 'Other')], max_length=255, verbose_name='Topic'),
        ),
    ]