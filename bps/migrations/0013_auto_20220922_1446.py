# Generated by Django 3.2 on 2022-09-22 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bps', '0012_auto_20220922_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipm',
            name='hls',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ipm',
            name='ipm',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ipm',
            name='pertumbuhan',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ipm',
            name='ppp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ipm',
            name='rls',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ipm',
            name='uhh',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
