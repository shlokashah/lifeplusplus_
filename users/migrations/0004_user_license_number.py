# Generated by Django 2.2.2 on 2019-09-01 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_delete_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='license_number',
            field=models.CharField(default='Not applicable', max_length=50),
        ),
    ]