# Generated by Django 2.0.4 on 2021-05-02 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0007_auto_20210502_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nontechnical',
            name='position',
            field=models.CharField(choices=[('None', 'None'), ('H', 'Head'), ('SH', 'Sub Head')], default='None', max_length=5),
        ),
    ]
