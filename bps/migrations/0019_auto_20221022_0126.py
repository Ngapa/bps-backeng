# Generated by Django 3.2 on 2022-10-21 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bps', '0018_auto_20221002_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='InflasiEnamKota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_kota', models.CharField(max_length=50)),
                ('mtom', models.FloatField(blank=True, null=True, verbose_name='M-to-M')),
                ('ytod', models.FloatField(blank=True, null=True, verbose_name='Y-to-D')),
                ('ytoy', models.FloatField(blank=True, null=True, verbose_name='Y-to-Y')),
                ('tanggal', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Inflasi Enam Kota',
                'verbose_name_plural': 'Inflasi Enam Kota',
            },
        ),
        migrations.CreateModel(
            name='InflasiKlmpkPengeluaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sembako', models.FloatField(blank=True, null=True, verbose_name='Makanan, Minuman, Tembakau')),
                ('sandang', models.FloatField(blank=True, null=True, verbose_name='Pakaian dan Alas Kaki')),
                ('perumahan', models.FloatField(blank=True, null=True, verbose_name='Perumahan, Air, Listrik, BB Lain')),
                ('perlengkapan', models.FloatField(blank=True, null=True, verbose_name='Perlengkapan, Pemeliharaan Rutin Rumah Tangga')),
                ('kesehatan', models.FloatField(blank=True, null=True, verbose_name='Kesehatan')),
                ('transportasi', models.FloatField(blank=True, null=True, verbose_name='Transportasi')),
                ('informasi', models.FloatField(blank=True, null=True, verbose_name='Informasi, Komunikasi, Keuangan')),
                ('rekreasi', models.FloatField(blank=True, null=True, verbose_name='Rekreasi, Olahraga, Budaya')),
                ('pendidikan', models.FloatField(blank=True, null=True, verbose_name='Pendidikan')),
                ('penyedia_pangan', models.FloatField(blank=True, null=True, verbose_name='Penyedia Makanan Minuman / Restoran')),
                ('perawatan_pribadi', models.FloatField(blank=True, null=True, verbose_name='Perawatan Pribadi, Jasa Lainnya')),
                ('total_inflasi', models.FloatField(blank=True, null=True, verbose_name='Total Inflasi')),
                ('tanggal', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Inflasi Kelompok Pengeluaran',
                'verbose_name_plural': 'Inflasi Kelompok Pengeluaran',
            },
        ),
        migrations.CreateModel(
            name='Ketimpangan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pddk', models.CharField(choices=[('rendah', 'Rendah'), ('sedang', 'Sedang'), ('tinggi', 'Tinggi')], default='rendah', max_length=30, verbose_name='Penduduk')),
                ('tanggal', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Ketimpangan',
            },
        ),
        migrations.AlterField(
            model_name='inflasi',
            name='informasi',
            field=models.FloatField(blank=True, null=True, verbose_name='Informasi, Komunikasi, Keuangan'),
        ),
        migrations.AlterField(
            model_name='inflasi',
            name='kesehatan',
            field=models.FloatField(blank=True, null=True, verbose_name='Kesehatan'),
        ),
        migrations.AlterField(
            model_name='inflasi',
            name='pendidikan',
            field=models.FloatField(blank=True, null=True, verbose_name='Pendidikan'),
        ),
        migrations.AlterField(
            model_name='inflasi',
            name='penyedia_pangan',
            field=models.FloatField(blank=True, null=True, verbose_name='Penyedia Makanan Minuman / Restoran'),
        ),
        migrations.AlterField(
            model_name='inflasi',
            name='perawatan_pribadi',
            field=models.FloatField(blank=True, null=True, verbose_name='Perawatan Pribadi, Jasa Lainnya'),
        ),
        migrations.AlterField(
            model_name='inflasi',
            name='perlengkapan',
            field=models.FloatField(blank=True, null=True, verbose_name='Perlengkapan, Pemeliharaan Rutin Rumah Tangga'),
        ),
        migrations.AlterField(
            model_name='inflasi',
            name='perumahan',
            field=models.FloatField(blank=True, null=True, verbose_name='Perumahan, Air, Listrik, BB Lain'),
        ),
        migrations.AlterField(
            model_name='inflasi',
            name='rekreasi',
            field=models.FloatField(blank=True, null=True, verbose_name='Rekreasi, Olahraga, Budaya'),
        ),
        migrations.AlterField(
            model_name='inflasi',
            name='sandang',
            field=models.FloatField(blank=True, null=True, verbose_name='Pakaian dan Alas Kaki'),
        ),
        migrations.AlterField(
            model_name='inflasi',
            name='sembako',
            field=models.FloatField(blank=True, null=True, verbose_name='Makanan, Minuman, Tembakau'),
        ),
        migrations.AlterField(
            model_name='inflasi',
            name='total_inflasi',
            field=models.FloatField(blank=True, null=True, verbose_name='Total Inflasi'),
        ),
        migrations.AlterField(
            model_name='inflasi',
            name='transportasi',
            field=models.FloatField(blank=True, null=True, verbose_name='Transportasi'),
        ),
        migrations.DeleteModel(
            name='Kota',
        ),
    ]