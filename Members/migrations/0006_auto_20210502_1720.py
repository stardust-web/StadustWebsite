# Generated by Django 2.0.4 on 2021-05-02 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0005_auto_20210502_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technical',
            name='position',
            field=models.CharField(choices=[('None', 'None'), ('SSH', 'Subsystem Head'), ('CSE', 'Chief System Engineer'), ('SE', 'System Engineer'), ('SSE', 'Subsystem Engineer')], max_length=5),
        ),
    ]
