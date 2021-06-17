# Generated by Django 2.0.4 on 2021-06-03 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0014_auto_20210603_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nontechnical',
            name='team',
            field=models.CharField(choices=[('WEB', 'Website and Design'), ('SPR', 'Public Relations and Sponsorship'), ('SM', 'Social Media'), ('DOC', 'Documentation')], max_length=4),
        ),
        migrations.AlterField(
            model_name='student',
            name='core_position',
            field=models.CharField(blank=True, choices=[('None', 'None'), ('SPM', 'Senior Project Manager'), ('PM', 'Project Manager'), ('MM', 'Mission Manager'), ('MD', 'Mission Director'), ('TM', 'Team Manager'), ('NH', 'Non-Technical Head')], default='None', max_length=4, null=True),
        ),
    ]