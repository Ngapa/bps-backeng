# Generated by Django 3.2 on 2022-10-21 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bps', '0019_auto_20221022_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='ketimpangan',
            name='jumlah',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inflasienamkota',
            name='nama_kota',
            field=models.CharField(choices=[('cilacap', 'Cilacap'), ('purwokerto', 'Purwokerto'), ('kudus', 'Kudus'), ('surakarta', 'Surakarta'), ('semarang', 'Semarang'), ('tegal', 'Tegal'), ('nasional', 'Nasional')], default='cilacap', max_length=50),
        ),
    ]