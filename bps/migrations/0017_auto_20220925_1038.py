# Generated by Django 3.2 on 2022-09-25 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bps', '0016_auto_20220925_1026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pendudukkecamatan',
            old_name='jumlah',
            new_name='lk',
        ),
        migrations.RemoveField(
            model_name='pendudukkecamatan',
            name='jenis_kelamin',
        ),
        migrations.AddField(
            model_name='pendudukkecamatan',
            name='pr',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pendudukkecamatan',
            name='rasio_jk',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pendudukkecamatan',
            name='total',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
