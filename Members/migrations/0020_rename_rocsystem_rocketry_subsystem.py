# Generated by Django 3.2.4 on 2021-06-30 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0019_auto_20210630_1609'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rocketry',
            old_name='rocsystem',
            new_name='subsystem',
        ),
    ]
