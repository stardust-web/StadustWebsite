# Generated by Django 3.2.4 on 2021-07-01 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0022_technical_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='nontechnical',
            name='rank',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='rocketry',
            name='rank',
            field=models.IntegerField(default=1),
        ),
    ]