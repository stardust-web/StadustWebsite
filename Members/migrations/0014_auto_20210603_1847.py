# Generated by Django 2.0.4 on 2021-06-03 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0013_auto_20210603_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
