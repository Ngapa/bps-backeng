# Generated by Django 3.2 on 2022-08-22 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bps', '0008_auto_20220817_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistribusiPdrbMigas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.FloatField(default=None, verbose_name='Pertanian dan Kehutanan')),
                ('b', models.FloatField(default=None, verbose_name='Pertambangan dan Penggalian')),
                ('c', models.FloatField(default=None, verbose_name='Industri')),
                ('d', models.FloatField(default=None, verbose_name='Listrik dan Gas')),
                ('e', models.FloatField(default=None, verbose_name='Air, Sampah/Limbah dan Daur Ulang')),
                ('f', models.FloatField(default=None, verbose_name='Kontruksi')),
                ('g', models.FloatField(default=None, verbose_name='Perdagangan, Reparasi Mobil/Sepeda Motor')),
                ('h', models.FloatField(default=None, verbose_name='Transportasi dan Pergudangan')),
                ('i', models.FloatField(default=None, verbose_name='Penyediaan Akomodasi dan Makan Minum')),
                ('j', models.FloatField(default=None, verbose_name='Informasi dan Komunikasi')),
                ('k', models.FloatField(default=None, verbose_name='Jasa Keuangan dan Asuransi')),
                ('l', models.FloatField(default=None, verbose_name='Real Estate')),
                ('m_n', models.FloatField(default=None, verbose_name='Jasa Perusahaan')),
                ('o', models.FloatField(default=None, verbose_name='Administrasi Pemerintahan, Pertahanan, dan Jaminan Sosial Wajib')),
                ('p', models.FloatField(default=None, verbose_name='Jasa Pendidikan')),
                ('q', models.FloatField(default=None, verbose_name='Jasa Kesehatan dan Kegiatan Sosial')),
                ('r_s_t_u', models.FloatField(default=None, verbose_name='Jasa Lainnya')),
                ('total_pdrb', models.FloatField(default=None, editable=False, verbose_name='Total')),
                ('tanggal', models.DateField()),
            ],
            options={
                'verbose_name': 'Distribusi Produk Domestik Regional Bruto Dengan Migas',
                'verbose_name_plural': 'Distribusi Produk Domestik Regional Bruto Dengan Migas',
            },
        ),
        migrations.CreateModel(
            name='DistribusiPdrbNonMigas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.FloatField(default=None, verbose_name='Pertanian dan Kehutanan')),
                ('b', models.FloatField(default=None, verbose_name='Pertambangan dan Penggalian')),
                ('c', models.FloatField(default=None, verbose_name='Industri')),
                ('d', models.FloatField(default=None, verbose_name='Listrik dan Gas')),
                ('e', models.FloatField(default=None, verbose_name='Air, Sampah/Limbah dan Daur Ulang')),
                ('f', models.FloatField(default=None, verbose_name='Kontruksi')),
                ('g', models.FloatField(default=None, verbose_name='Perdagangan, Reparasi Mobil/Sepeda Motor')),
                ('h', models.FloatField(default=None, verbose_name='Transportasi dan Pergudangan')),
                ('i', models.FloatField(default=None, verbose_name='Penyediaan Akomodasi dan Makan Minum')),
                ('j', models.FloatField(default=None, verbose_name='Informasi dan Komunikasi')),
                ('k', models.FloatField(default=None, verbose_name='Jasa Keuangan dan Asuransi')),
                ('l', models.FloatField(default=None, verbose_name='Real Estate')),
                ('m_n', models.FloatField(default=None, verbose_name='Jasa Perusahaan')),
                ('o', models.FloatField(default=None, verbose_name='Administrasi Pemerintahan, Pertahanan, dan Jaminan Sosial Wajib')),
                ('p', models.FloatField(default=None, verbose_name='Jasa Pendidikan')),
                ('q', models.FloatField(default=None, verbose_name='Jasa Kesehatan dan Kegiatan Sosial')),
                ('r_s_t_u', models.FloatField(default=None, verbose_name='Jasa Lainnya')),
                ('total_pdrb', models.FloatField(default=None, editable=False, verbose_name='Total')),
                ('tanggal', models.DateField()),
            ],
            options={
                'verbose_name': 'Distribusi Produk Domestik Regional Bruto Non Migas',
                'verbose_name_plural': 'Distribusi Produk Domestik Regional Bruto Non Migas',
            },
        ),
        migrations.CreateModel(
            name='InflasiDod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sandang', models.FloatField(default=None)),
                ('sembako', models.FloatField(default=None)),
                ('perumahan', models.FloatField(default=None)),
                ('kesehatan', models.FloatField(default=None)),
                ('transportasi', models.FloatField(default=None)),
                ('informasi', models.FloatField(default=None)),
                ('rekreasi', models.FloatField(default=None)),
                ('pendidikan', models.FloatField(default=None)),
                ('penyedia_pangan', models.FloatField(default=None)),
                ('perawatan_pribadi', models.FloatField(default=None)),
                ('total_inflasi', models.FloatField(default=None)),
                ('tanggal', models.DateField()),
            ],
            options={
                'verbose_name': 'Inflasi Date on Date',
                'verbose_name_plural': 'Inflasi Date on Date',
            },
        ),
        migrations.CreateModel(
            name='InflasiYoy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sandang', models.FloatField(default=None)),
                ('sembako', models.FloatField(default=None)),
                ('perumahan', models.FloatField(default=None)),
                ('kesehatan', models.FloatField(default=None)),
                ('transportasi', models.FloatField(default=None)),
                ('informasi', models.FloatField(default=None)),
                ('rekreasi', models.FloatField(default=None)),
                ('pendidikan', models.FloatField(default=None)),
                ('penyedia_pangan', models.FloatField(default=None)),
                ('perawatan_pribadi', models.FloatField(default=None)),
                ('total_inflasi', models.FloatField(default=None)),
                ('tanggal', models.DateField()),
            ],
            options={
                'verbose_name': 'Inflasi Year on Year',
                'verbose_name_plural': 'Inflasi Year on Year',
            },
        ),
        migrations.CreateModel(
            name='Ipm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uhh', models.FloatField(default=None)),
                ('rls', models.FloatField(default=None)),
                ('hls', models.FloatField(default=None)),
                ('ppp', models.FloatField(default=None)),
                ('ipm', models.FloatField(default=None)),
                ('pertumbuhan', models.FloatField(default=None)),
                ('tanggal', models.DateField()),
            ],
            options={
                'verbose_name': 'Indeks Pembangunan Manusia',
                'verbose_name_plural': 'Indeks Pembangunan Manusia',
            },
        ),
        migrations.CreateModel(
            name='Kemiskinan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ppdk_mskn', models.FloatField(default=None)),
                ('p0', models.FloatField(default=None)),
                ('p1', models.FloatField(default=None)),
                ('p2', models.FloatField(default=None)),
                ('gk', models.FloatField(default=None)),
                ('tanggal', models.DateField()),
            ],
            options={
                'verbose_name': 'Kemiskinan',
                'verbose_name_plural': 'Kemiskinan',
            },
        ),
        migrations.CreateModel(
            name='LajuPertumbuhanPdrbMigas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.FloatField(default=None, verbose_name='Pertanian dan Kehutanan')),
                ('b', models.FloatField(default=None, verbose_name='Pertambangan dan Penggalian')),
                ('c', models.FloatField(default=None, verbose_name='Industri')),
                ('d', models.FloatField(default=None, verbose_name='Listrik dan Gas')),
                ('e', models.FloatField(default=None, verbose_name='Air, Sampah/Limbah dan Daur Ulang')),
                ('f', models.FloatField(default=None, verbose_name='Kontruksi')),
                ('g', models.FloatField(default=None, verbose_name='Perdagangan, Reparasi Mobil/Sepeda Motor')),
                ('h', models.FloatField(default=None, verbose_name='Transportasi dan Pergudangan')),
                ('i', models.FloatField(default=None, verbose_name='Penyediaan Akomodasi dan Makan Minum')),
                ('j', models.FloatField(default=None, verbose_name='Informasi dan Komunikasi')),
                ('k', models.FloatField(default=None, verbose_name='Jasa Keuangan dan Asuransi')),
                ('l', models.FloatField(default=None, verbose_name='Real Estate')),
                ('m_n', models.FloatField(default=None, verbose_name='Jasa Perusahaan')),
                ('o', models.FloatField(default=None, verbose_name='Administrasi Pemerintahan, Pertahanan, dan Jaminan Sosial Wajib')),
                ('p', models.FloatField(default=None, verbose_name='Jasa Pendidikan')),
                ('q', models.FloatField(default=None, verbose_name='Jasa Kesehatan dan Kegiatan Sosial')),
                ('r_s_t_u', models.FloatField(default=None, verbose_name='Jasa Lainnya')),
                ('total_pdrb', models.FloatField(default=None, editable=False, verbose_name='Total')),
                ('tanggal', models.DateField()),
            ],
            options={
                'verbose_name': 'Laju Pertumbuhan Produk Domestik Regional Bruto Dengan Migas',
                'verbose_name_plural': 'Laju Pertumbuhan Produk Domestik Regional Bruto Dengan Migas',
            },
        ),
        migrations.CreateModel(
            name='LajuPertumbuhanPdrbNonMigas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.FloatField(default=None, verbose_name='Pertanian dan Kehutanan')),
                ('b', models.FloatField(default=None, verbose_name='Pertambangan dan Penggalian')),
                ('c', models.FloatField(default=None, verbose_name='Industri')),
                ('d', models.FloatField(default=None, verbose_name='Listrik dan Gas')),
                ('e', models.FloatField(default=None, verbose_name='Air, Sampah/Limbah dan Daur Ulang')),
                ('f', models.FloatField(default=None, verbose_name='Kontruksi')),
                ('g', models.FloatField(default=None, verbose_name='Perdagangan, Reparasi Mobil/Sepeda Motor')),
                ('h', models.FloatField(default=None, verbose_name='Transportasi dan Pergudangan')),
                ('i', models.FloatField(default=None, verbose_name='Penyediaan Akomodasi dan Makan Minum')),
                ('j', models.FloatField(default=None, verbose_name='Informasi dan Komunikasi')),
                ('k', models.FloatField(default=None, verbose_name='Jasa Keuangan dan Asuransi')),
                ('l', models.FloatField(default=None, verbose_name='Real Estate')),
                ('m_n', models.FloatField(default=None, verbose_name='Jasa Perusahaan')),
                ('o', models.FloatField(default=None, verbose_name='Administrasi Pemerintahan, Pertahanan, dan Jaminan Sosial Wajib')),
                ('p', models.FloatField(default=None, verbose_name='Jasa Pendidikan')),
                ('q', models.FloatField(default=None, verbose_name='Jasa Kesehatan dan Kegiatan Sosial')),
                ('r_s_t_u', models.FloatField(default=None, verbose_name='Jasa Lainnya')),
                ('total_pdrb', models.FloatField(default=None, editable=False, verbose_name='Total')),
                ('tanggal', models.DateField()),
            ],
            options={
                'verbose_name': 'Laju Pertumbuhan Produk Domestik Regional Bruto Non Migas',
                'verbose_name_plural': 'Laju Pertumbuhan Produk Domestik Regional Bruto Non Migas',
            },
        ),
        migrations.CreateModel(
            name='PdrbMigas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.FloatField(default=None, verbose_name='Pertanian dan Kehutanan')),
                ('b', models.FloatField(default=None, verbose_name='Pertambangan dan Penggalian')),
                ('c', models.FloatField(default=None, verbose_name='Industri')),
                ('d', models.FloatField(default=None, verbose_name='Listrik dan Gas')),
                ('e', models.FloatField(default=None, verbose_name='Air, Sampah/Limbah dan Daur Ulang')),
                ('f', models.FloatField(default=None, verbose_name='Kontruksi')),
                ('g', models.FloatField(default=None, verbose_name='Perdagangan, Reparasi Mobil/Sepeda Motor')),
                ('h', models.FloatField(default=None, verbose_name='Transportasi dan Pergudangan')),
                ('i', models.FloatField(default=None, verbose_name='Penyediaan Akomodasi dan Makan Minum')),
                ('j', models.FloatField(default=None, verbose_name='Informasi dan Komunikasi')),
                ('k', models.FloatField(default=None, verbose_name='Jasa Keuangan dan Asuransi')),
                ('l', models.FloatField(default=None, verbose_name='Real Estate')),
                ('m_n', models.FloatField(default=None, verbose_name='Jasa Perusahaan')),
                ('o', models.FloatField(default=None, verbose_name='Administrasi Pemerintahan, Pertahanan, dan Jaminan Sosial Wajib')),
                ('p', models.FloatField(default=None, verbose_name='Jasa Pendidikan')),
                ('q', models.FloatField(default=None, verbose_name='Jasa Kesehatan dan Kegiatan Sosial')),
                ('r_s_t_u', models.FloatField(default=None, verbose_name='Jasa Lainnya')),
                ('total_pdrb', models.FloatField(default=None, editable=False, verbose_name='Total')),
                ('tanggal', models.DateField()),
            ],
            options={
                'verbose_name': 'Produk Domestik Regional Bruto Dengan Migas',
                'verbose_name_plural': 'Produk Domestik Regional Bruto Dengan Migas',
            },
        ),
        migrations.CreateModel(
            name='PdrbNonMigas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.FloatField(default=None, verbose_name='Pertanian dan Kehutanan')),
                ('b', models.FloatField(default=None, verbose_name='Pertambangan dan Penggalian')),
                ('c', models.FloatField(default=None, verbose_name='Industri')),
                ('d', models.FloatField(default=None, verbose_name='Listrik dan Gas')),
                ('e', models.FloatField(default=None, verbose_name='Air, Sampah/Limbah dan Daur Ulang')),
                ('f', models.FloatField(default=None, verbose_name='Kontruksi')),
                ('g', models.FloatField(default=None, verbose_name='Perdagangan, Reparasi Mobil/Sepeda Motor')),
                ('h', models.FloatField(default=None, verbose_name='Transportasi dan Pergudangan')),
                ('i', models.FloatField(default=None, verbose_name='Penyediaan Akomodasi dan Makan Minum')),
                ('j', models.FloatField(default=None, verbose_name='Informasi dan Komunikasi')),
                ('k', models.FloatField(default=None, verbose_name='Jasa Keuangan dan Asuransi')),
                ('l', models.FloatField(default=None, verbose_name='Real Estate')),
                ('m_n', models.FloatField(default=None, verbose_name='Jasa Perusahaan')),
                ('o', models.FloatField(default=None, verbose_name='Administrasi Pemerintahan, Pertahanan, dan Jaminan Sosial Wajib')),
                ('p', models.FloatField(default=None, verbose_name='Jasa Pendidikan')),
                ('q', models.FloatField(default=None, verbose_name='Jasa Kesehatan dan Kegiatan Sosial')),
                ('r_s_t_u', models.FloatField(default=None, verbose_name='Jasa Lainnya')),
                ('total_pdrb', models.FloatField(default=None, editable=False, verbose_name='Total')),
                ('tanggal', models.DateField()),
            ],
            options={
                'verbose_name': 'Produk Domestik Regional Bruto Non Migas',
                'verbose_name_plural': 'Produk Domestik Regional Bruto Non Migas',
            },
        ),
        migrations.CreateModel(
            name='SumberPertumbuhanPdrbMigas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.FloatField(default=None, verbose_name='Pertanian dan Kehutanan')),
                ('b', models.FloatField(default=None, verbose_name='Pertambangan dan Penggalian')),
                ('c', models.FloatField(default=None, verbose_name='Industri')),
                ('d', models.FloatField(default=None, verbose_name='Listrik dan Gas')),
                ('e', models.FloatField(default=None, verbose_name='Air, Sampah/Limbah dan Daur Ulang')),
                ('f', models.FloatField(default=None, verbose_name='Kontruksi')),
                ('g', models.FloatField(default=None, verbose_name='Perdagangan, Reparasi Mobil/Sepeda Motor')),
                ('h', models.FloatField(default=None, verbose_name='Transportasi dan Pergudangan')),
                ('i', models.FloatField(default=None, verbose_name='Penyediaan Akomodasi dan Makan Minum')),
                ('j', models.FloatField(default=None, verbose_name='Informasi dan Komunikasi')),
                ('k', models.FloatField(default=None, verbose_name='Jasa Keuangan dan Asuransi')),
                ('l', models.FloatField(default=None, verbose_name='Real Estate')),
                ('m_n', models.FloatField(default=None, verbose_name='Jasa Perusahaan')),
                ('o', models.FloatField(default=None, verbose_name='Administrasi Pemerintahan, Pertahanan, dan Jaminan Sosial Wajib')),
                ('p', models.FloatField(default=None, verbose_name='Jasa Pendidikan')),
                ('q', models.FloatField(default=None, verbose_name='Jasa Kesehatan dan Kegiatan Sosial')),
                ('r_s_t_u', models.FloatField(default=None, verbose_name='Jasa Lainnya')),
                ('total_pdrb', models.FloatField(default=None, editable=False, verbose_name='Total')),
                ('tanggal', models.DateField()),
            ],
            options={
                'verbose_name': 'Sumber Pertumbuhan Produk Domestik Regional Bruto Dengan Migas',
                'verbose_name_plural': 'Sumber Pertumbuhan Produk Domestik Regional Bruto Dengan Migas',
            },
        ),
        migrations.CreateModel(
            name='SumberPertumbuhanPdrbNonMigas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.FloatField(default=None, verbose_name='Pertanian dan Kehutanan')),
                ('b', models.FloatField(default=None, verbose_name='Pertambangan dan Penggalian')),
                ('c', models.FloatField(default=None, verbose_name='Industri')),
                ('d', models.FloatField(default=None, verbose_name='Listrik dan Gas')),
                ('e', models.FloatField(default=None, verbose_name='Air, Sampah/Limbah dan Daur Ulang')),
                ('f', models.FloatField(default=None, verbose_name='Kontruksi')),
                ('g', models.FloatField(default=None, verbose_name='Perdagangan, Reparasi Mobil/Sepeda Motor')),
                ('h', models.FloatField(default=None, verbose_name='Transportasi dan Pergudangan')),
                ('i', models.FloatField(default=None, verbose_name='Penyediaan Akomodasi dan Makan Minum')),
                ('j', models.FloatField(default=None, verbose_name='Informasi dan Komunikasi')),
                ('k', models.FloatField(default=None, verbose_name='Jasa Keuangan dan Asuransi')),
                ('l', models.FloatField(default=None, verbose_name='Real Estate')),
                ('m_n', models.FloatField(default=None, verbose_name='Jasa Perusahaan')),
                ('o', models.FloatField(default=None, verbose_name='Administrasi Pemerintahan, Pertahanan, dan Jaminan Sosial Wajib')),
                ('p', models.FloatField(default=None, verbose_name='Jasa Pendidikan')),
                ('q', models.FloatField(default=None, verbose_name='Jasa Kesehatan dan Kegiatan Sosial')),
                ('r_s_t_u', models.FloatField(default=None, verbose_name='Jasa Lainnya')),
                ('total_pdrb', models.FloatField(default=None, editable=False, verbose_name='Total')),
                ('tanggal', models.DateField()),
            ],
            options={
                'verbose_name': 'Sumber Pertumbuhan Produk Domestik Regional Bruto Non Migas',
                'verbose_name_plural': 'Sumber Pertumbuhan Produk Domestik Regional Bruto Non Migas',
            },
        ),
        migrations.CreateModel(
            name='TenagaKerja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('angkatan_kerja', models.FloatField(default=None)),
                ('bekerja', models.FloatField(default=None)),
                ('pengangguran', models.FloatField(default=None)),
                ('bkn_angkatan_kerja', models.FloatField(default=None)),
                ('sekolah', models.FloatField(default=None)),
                ('urur_ruta', models.FloatField(default=None)),
                ('lainnya', models.FloatField(default=None)),
                ('gender', models.CharField(choices=[('LK', 'Laki-Laki'), ('PR', 'Perempuan')], max_length=15)),
            ],
            options={
                'verbose_name': 'Ketenagakerjaan',
                'verbose_name_plural': 'Ketenagakerjaan',
            },
        ),
        migrations.AlterModelOptions(
            name='inflasi',
            options={'verbose_name': 'Inflasi', 'verbose_name_plural': 'Inflasi'},
        ),
        migrations.AlterModelOptions(
            name='kota',
            options={'verbose_name': 'Kota', 'verbose_name_plural': 'Kota'},
        ),
        migrations.RemoveField(
            model_name='kota',
            name='pdrb',
        ),
        migrations.AlterField(
            model_name='inflasi',
            name='informasi',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='inflasi',
            name='kesehatan',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='inflasi',
            name='pendidikan',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='inflasi',
            name='penyedia_pangan',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='inflasi',
            name='perawatan_pribadi',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='inflasi',
            name='perumahan',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='inflasi',
            name='rekreasi',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='inflasi',
            name='sandang',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='inflasi',
            name='sembako',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='inflasi',
            name='total_inflasi',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='inflasi',
            name='transportasi',
            field=models.FloatField(default=None),
        ),
        migrations.DeleteModel(
            name='ProdukDomestikRegionalBruto',
        ),
        migrations.AddField(
            model_name='kota',
            name='dist_pdrb_migas',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='distribusi_pdrb_migas', to='bps.distribusipdrbmigas'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kota',
            name='dist_pdrb_non_migas',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='distribusi_pdrb_non_migas', to='bps.distribusipdrbnonmigas'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kota',
            name='inflasi_dod',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='inflasi_dod_kota', to='bps.inflasidod'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kota',
            name='inlfasi_yoy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='inflasi_yoy_kota', to='bps.inflasiyoy'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kota',
            name='laju_pert_pdrb_migas',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='laju_pertumbuhan_pdrb_migas', to='bps.lajupertumbuhanpdrbmigas'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kota',
            name='laju_pert_pdrb_non_migas',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, related_name='laju_pertumbuhan_pdrb_non_migas', to='bps.lajupertumbuhanpdrbnonmigas'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kota',
            name='pdrb_migas',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pdrb_kota', to='bps.pdrbmigas'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kota',
            name='pdrb_non_migas',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pdrb_kota', to='bps.pdrbnonmigas'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kota',
            name='sum_pert_pdrb_migas',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sumber_pertumbuhan_pdrb_migas', to='bps.sumberpertumbuhanpdrbmigas'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kota',
            name='sum_pert_pdrb_non_migas',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sumber_pertumbuhan_pdrb_non_migas', to='bps.sumberpertumbuhanpdrbnonmigas'),
            preserve_default=False,
        ),
    ]
