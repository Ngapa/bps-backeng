# Generated by Django 3.2 on 2022-08-24 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bps', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distribusipdrbmigas',
            name='total_pdrb',
        ),
        migrations.RemoveField(
            model_name='distribusipdrbnonmigas',
            name='total_pdrb',
        ),
        migrations.RemoveField(
            model_name='inflasidod',
            name='total_inflasi',
        ),
        migrations.RemoveField(
            model_name='inflasiyoy',
            name='total_inflasi',
        ),
        migrations.RemoveField(
            model_name='kota',
            name='total_pend',
        ),
        migrations.RemoveField(
            model_name='lajupertumbuhanpdrbmigas',
            name='total_pdrb',
        ),
        migrations.RemoveField(
            model_name='lajupertumbuhanpdrbnonmigas',
            name='total_pdrb',
        ),
        migrations.RemoveField(
            model_name='pdrbmigas',
            name='total_pdrb',
        ),
        migrations.RemoveField(
            model_name='pdrbnonmigas',
            name='total_pdrb',
        ),
        migrations.RemoveField(
            model_name='penduduklaki',
            name='total',
        ),
        migrations.RemoveField(
            model_name='penduduklakikecamatan',
            name='total',
        ),
        migrations.RemoveField(
            model_name='pendudukpr',
            name='total',
        ),
        migrations.RemoveField(
            model_name='pendudukprkecamatan',
            name='total',
        ),
        migrations.RemoveField(
            model_name='sumberpertumbuhanpdrbmigas',
            name='total_pdrb',
        ),
        migrations.RemoveField(
            model_name='sumberpertumbuhanpdrbnonmigas',
            name='total_pdrb',
        ),
    ]
