# Generated by Django 2.2.3 on 2019-09-04 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescription', '0008_merge_20190904_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescriptions',
            name='record',
            field=models.CharField(max_length=100),
        ),
    ]