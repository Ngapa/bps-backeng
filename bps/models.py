from secrets import choice
from signal import default_int_handler
from django.db import models
# Create your models here.


class PdrbMigas(models.Model):
    a = models.FloatField(
        verbose_name="Pertanian dan Kehutanan", default=None)
    b = models.FloatField(
        verbose_name="Pertambangan dan Penggalian", default=None)
    c = models.FloatField(verbose_name="Industri", default=None)
    d = models.FloatField(verbose_name="Listrik dan Gas",
                          default=None)
    e = models.FloatField(
        verbose_name="Air, Sampah/Limbah dan Daur Ulang", default=None)
    f = models.FloatField(verbose_name="Kontruksi", default=None)
    g = models.FloatField(
        verbose_name="Perdagangan, Reparasi Mobil/Sepeda Motor", default=None)
    h = models.FloatField(
        verbose_name="Transportasi dan Pergudangan", default=None)
    i = models.FloatField(
        verbose_name="Penyediaan Akomodasi dan Makan Minum", default=None)
    j = models.FloatField(
        verbose_name="Informasi dan Komunikasi", default=None)
    k = models.FloatField(
        verbose_name="Jasa Keuangan dan Asuransi", default=None)
    l = models.FloatField(verbose_name="Real Estate", default=None)
    m_n = models.FloatField(
        verbose_name="Jasa Perusahaan", default=None)
    o = models.FloatField(
        verbose_name="Administrasi Pemerintahan, Pertahanan, dan Jaminan Sosial Wajib", default=None)
    p = models.FloatField(verbose_name="Jasa Pendidikan",
                          default=None)
    q = models.FloatField(
        verbose_name="Jasa Kesehatan dan Kegiatan Sosial", default=None)
    r_s_t_u = models.FloatField(
        verbose_name="Jasa Lainnya", default=None)
    total_pdrb = models.FloatField(
        verbose_name="Total", default=None, editable=False)
    tanggal = models.DateField()

    def save(self, *args, **kwargs):
        self.total_pdrb = self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h + \
            self.i + self.j + self.k + self.l + self.m_n + \
            self.o + self.p + self.q + self.r_s_t_u
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tanggal

    class Meta:
        verbose_name = "Produk Domestik Regional Bruto Dengan Migas"
        verbose_name_plural = "Produk Domestik Regional Bruto Dengan Migas"


class DistribusiPdrbMigas(models.Model):
    a = models.FloatField(
        verbose_name="Pertanian dan Kehutanan", default=None)
    b = models.FloatField(
        verbose_name="Pertambangan dan Penggalian", default=None)
    c = models.FloatField(verbose_name="Industri", default=None)
    d = models.FloatField(verbose_name="Listrik dan Gas",
                          default=None)
    e = models.FloatField(
        verbose_name="Air, Sampah/Limbah dan Daur Ulang", default=None)
    f = models.FloatField(verbose_name="Kontruksi", default=None)
    g = models.FloatField(
        verbose_name="Perdagangan, Reparasi Mobil/Sepeda Motor", default=None)
    h = models.FloatField(
        verbose_name="Transportasi dan Pergudangan", default=None)
    i = models.FloatField(
        verbose_name="Penyediaan Akomodasi dan Makan Minum", default=None)
    j = models.FloatField(
        verbose_name="Informasi dan Komunikasi", default=None)
    k = models.FloatField(
        verbose_name="Jasa Keuangan dan Asuransi", default=None)
    l = models.FloatField(verbose_name="Real Estate", default=None)
    m_n = models.FloatField(
        verbose_name="Jasa Perusahaan", default=None)
    o = models.FloatField(
        verbose_name="Administrasi Pemerintahan, Pertahanan, dan Jaminan Sosial Wajib", default=None)
    p = models.FloatField(verbose_name="Jasa Pendidikan",
                          default=None)
    q = models.FloatField(
        verbose_name="Jasa Kesehatan dan Kegiatan Sosial", default=None)
    r_s_t_u = models.FloatField(
        verbose_name="Jasa Lainnya", default=None)
    total_pdrb = models.FloatField(
        verbose_name="Total", default=None, editable=False)
    tanggal = models.DateField()

    def save(self, *args, **kwargs):
        self.total_pdrb = self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h + \
            self.i + self.j + self.k + self.l + self.m_n + \
            self.o + self.p + self.q + self.r_s_t_u
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tanggal

    class Meta:
        verbose_name = "Distribusi Produk Domestik Regional Bruto Dengan Migas"
        verbose_name_plural = "Distribusi Produk Domestik Regional Bruto Dengan Migas"


class LajuPertumbuhanPdrbMigas(models.Model):
    a = models.FloatField(
        verbose_name="Pertanian dan Kehutanan", default=None)
    b = models.FloatField(
        verbose_name="Pertambangan dan Penggalian", default=None)
    c = models.FloatField(verbose_name="Industri", default=None)
    d = models.FloatField(verbose_name="Listrik dan Gas",
                          default=None)
    e = models.FloatField(
        verbose_name="Air, Sampah/Limbah dan Daur Ulang", default=None)
    f = models.FloatField(verbose_name="Kontruksi", default=None)
    g = models.FloatField(
        verbose_name="Perdagangan, Reparasi Mobil/Sepeda Motor", default=None)
    h = models.FloatField(
        verbose_name="Transportasi dan Pergudangan", default=None)
    i = models.FloatField(
        verbose_name="Penyediaan Akomodasi dan Makan Minum", default=None)
    j = models.FloatField(
        verbose_name="Informasi dan Komunikasi", default=None)
    k = models.FloatField(
        verbose_name="Jasa Keuangan dan Asuransi", default=None)
    l = models.FloatField(verbose_name="Real Estate", default=None)
    m_n = models.FloatField(
        verbose_name="Jasa Perusahaan", default=None)
    o = models.FloatField(
        verbose_name="Administrasi Pemerintahan, Pertahanan, dan Jaminan Sosial Wajib", default=None)
    p = models.FloatField(verbose_name="Jasa Pendidikan",
                          default=None)
    q = models.FloatField(
        verbose_name="Jasa Kesehatan dan Kegiatan Sosial", default=None)
    r_s_t_u = models.FloatField(
        verbose_name="Jasa Lainnya", default=None)
    total_pdrb = models.FloatField(
        verbose_name="Total", default=None, editable=False)
    tanggal = models.DateField()

    def save(self, *args, **kwargs):
        self.total_pdrb = self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h + \
            self.i + self.j + self.k + self.l + self.m_n + \
            self.o + self.p + self.q + self.r_s_t_u
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tanggal

    class Meta:
        verbose_name = "Laju Pertumbuhan Produk Domestik Regional Bruto Dengan Migas"
        verbose_name_plural = "Laju Pertumbuhan Produk Domestik Regional Bruto Dengan Migas"


class SumberPertumbuhanPdrbMigas(models.Model):
    a = models.FloatField(
        verbose_name="Pertanian dan Kehutanan", default=None)
    b = models.FloatField(
        verbose_name="Pertambangan dan Penggalian", default=None)
    c = models.FloatField(verbose_name="Industri", default=None)
    d = models.FloatField(verbose_name="Listrik dan Gas",
                          default=None)
    e = models.FloatField(
        verbose_name="Air, Sampah/Limbah dan Daur Ulang", default=None)
    f = models.FloatField(verbose_name="Kontruksi", default=None)
    g = models.FloatField(
        verbose_name="Perdagangan, Reparasi Mobil/Sepeda Motor", default=None)
    h = models.FloatField(
        verbose_name="Transportasi dan Pergudangan", default=None)
    i = models.FloatField(
        verbose_name="Penyediaan Akomodasi dan Makan Minum", default=None)
    j = models.FloatField(
        verbose_name="Informasi dan Komunikasi", default=None)
    k = models.FloatField(
        verbose_name="Jasa Keuangan dan Asuransi", default=None)
    l = models.FloatField(verbose_name="Real Estate", default=None)
    m_n = models.FloatField(
        verbose_name="Jasa Perusahaan", default=None)
    o = models.FloatField(
        verbose_name="Administrasi Pemerintahan, Pertahanan, dan Jaminan Sosial Wajib", default=None)
    p = models.FloatField(verbose_name="Jasa Pendidikan",
                          default=None)
    q = models.FloatField(
        verbose_name="Jasa Kesehatan dan Kegiatan Sosial", default=None)
    r_s_t_u = models.FloatField(
        verbose_name="Jasa Lainnya", default=None)
    total_pdrb = models.FloatField(
        verbose_name="Total", default=None, editable=False)
    tanggal = models.DateField()

    def save(self, *args, **kwargs):
        self.total_pdrb = self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h + \
            self.i + self.j + self.k + self.l + self.m_n + \
            self.o + self.p + self.q + self.r_s_t_u
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tanggal

    class Meta:
        verbose_name = "Sumber Pertumbuhan Produk Domestik Regional Bruto Dengan Migas"
        verbose_name_plural = "Sumber Pertumbuhan Produk Domestik Regional Bruto Dengan Migas"


class PdrbNonMigas(models.Model):
    a = models.FloatField(
        verbose_name="Pertanian dan Kehutanan", default=None)
    b = models.FloatField(
        verbose_name="Pertambangan dan Penggalian", default=None)
    c = models.FloatField(verbose_name="Industri", default=None)
    d = models.FloatField(verbose_name="Listrik dan Gas",
                          default=None)
    e = models.FloatField(
        verbose_name="Air, Sampah/Limbah dan Daur Ulang", default=None)
    f = models.FloatField(verbose_name="Kontruksi", default=None)
    g = models.FloatField(
        verbose_name="Perdagangan, Reparasi Mobil/Sepeda Motor", default=None)
    h = models.FloatField(
        verbose_name="Transportasi dan Pergudangan", default=None)
    i = models.FloatField(
        verbose_name="Penyediaan Akomodasi dan Makan Minum", default=None)
    j = models.FloatField(
        verbose_name="Informasi dan Komunikasi", default=None)
    k = models.FloatField(
        verbose_name="Jasa Keuangan dan Asuransi", default=None)
    l = models.FloatField(verbose_name="Real Estate", default=None)
    m_n = models.FloatField(
        verbose_name="Jasa Perusahaan", default=None)
    o = models.FloatField(
        verbose_name="Administrasi Pemerintahan, Pertahanan, dan Jaminan Sosial Wajib", default=None)
    p = models.FloatField(verbose_name="Jasa Pendidikan",
                          default=None)
    q = models.FloatField(
        verbose_name="Jasa Kesehatan dan Kegiatan Sosial", default=None)
    r_s_t_u = models.FloatField(
        verbose_name="Jasa Lainnya", default=None)
    total_pdrb = models.FloatField(
        verbose_name="Total", default=None, editable=False)
    tanggal = models.DateField()

    def save(self, *args, **kwargs):
        self.total_pdrb = self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h + \
            self.i + self.j + self.k + self.l + self.m_n + \
            self.o + self.p + self.q + self.r_s_t_u
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tanggal

    class Meta:
        verbose_name = "Produk Domestik Regional Bruto Non Migas"
        verbose_name_plural = "Produk Domestik Regional Bruto Non Migas"


class DistribusiPdrbNonMigas(models.Model):
    a = models.FloatField(
        verbose_name="Pertanian dan Kehutanan", default=None)
    b = models.FloatField(
        verbose_name="Pertambangan dan Penggalian", default=None)
    c = models.FloatField(verbose_name="Industri", default=None)
    d = models.FloatField(verbose_name="Listrik dan Gas",
                          default=None)
    e = models.FloatField(
        verbose_name="Air, Sampah/Limbah dan Daur Ulang", default=None)
    f = models.FloatField(verbose_name="Kontruksi", default=None)
    g = models.FloatField(
        verbose_name="Perdagangan, Reparasi Mobil/Sepeda Motor", default=None)
    h = models.FloatField(
        verbose_name="Transportasi dan Pergudangan", default=None)
    i = models.FloatField(
        verbose_name="Penyediaan Akomodasi dan Makan Minum", default=None)
    j = models.FloatField(
        verbose_name="Informasi dan Komunikasi", default=None)
    k = models.FloatField(
        verbose_name="Jasa Keuangan dan Asuransi", default=None)
    l = models.FloatField(verbose_name="Real Estate", default=None)
    m_n = models.FloatField(
        verbose_name="Jasa Perusahaan", default=None)
    o = models.FloatField(
        verbose_name="Administrasi Pemerintahan, Pertahanan, dan Jaminan Sosial Wajib", default=None)
    p = models.FloatField(verbose_name="Jasa Pendidikan",
                          default=None)
    q = models.FloatField(
        verbose_name="Jasa Kesehatan dan Kegiatan Sosial", default=None)
    r_s_t_u = models.FloatField(
        verbose_name="Jasa Lainnya", default=None)
    total_pdrb = models.FloatField(
        verbose_name="Total", default=None, editable=False)
    tanggal = models.DateField()

    def save(self, *args, **kwargs):
        self.total_pdrb = self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h + \
            self.i + self.j + self.k + self.l + self.m_n + \
            self.o + self.p + self.q + self.r_s_t_u
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tanggal

    class Meta:
        verbose_name = "Distribusi Produk Domestik Regional Bruto Non Migas"
        verbose_name_plural = "Distribusi Produk Domestik Regional Bruto Non Migas"


class LajuPertumbuhanPdrbNonMigas(models.Model):
    a = models.FloatField(
        verbose_name="Pertanian dan Kehutanan", default=None)
    b = models.FloatField(
        verbose_name="Pertambangan dan Penggalian", default=None)
    c = models.FloatField(verbose_name="Industri", default=None)
    d = models.FloatField(verbose_name="Listrik dan Gas",
                          default=None)
    e = models.FloatField(
        verbose_name="Air, Sampah/Limbah dan Daur Ulang", default=None)
    f = models.FloatField(verbose_name="Kontruksi", default=None)
    g = models.FloatField(
        verbose_name="Perdagangan, Reparasi Mobil/Sepeda Motor", default=None)
    h = models.FloatField(
        verbose_name="Transportasi dan Pergudangan", default=None)
    i = models.FloatField(
        verbose_name="Penyediaan Akomodasi dan Makan Minum", default=None)
    j = models.FloatField(
        verbose_name="Informasi dan Komunikasi", default=None)
    k = models.FloatField(
        verbose_name="Jasa Keuangan dan Asuransi", default=None)
    l = models.FloatField(verbose_name="Real Estate", default=None)
    m_n = models.FloatField(
        verbose_name="Jasa Perusahaan", default=None)
    o = models.FloatField(
        verbose_name="Administrasi Pemerintahan, Pertahanan, dan Jaminan Sosial Wajib", default=None)
    p = models.FloatField(verbose_name="Jasa Pendidikan",
                          default=None)
    q = models.FloatField(
        verbose_name="Jasa Kesehatan dan Kegiatan Sosial", default=None)
    r_s_t_u = models.FloatField(
        verbose_name="Jasa Lainnya", default=None)
    total_pdrb = models.FloatField(
        verbose_name="Total", default=None, editable=False)
    tanggal = models.DateField()

    def save(self, *args, **kwargs):
        self.total_pdrb = self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h + \
            self.i + self.j + self.k + self.l + self.m_n + \
            self.o + self.p + self.q + self.r_s_t_u
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tanggal

    class Meta:
        verbose_name = "Laju Pertumbuhan Produk Domestik Regional Bruto Non Migas"
        verbose_name_plural = "Laju Pertumbuhan Produk Domestik Regional Bruto Non Migas"


class SumberPertumbuhanPdrbNonMigas(models.Model):
    a = models.FloatField(
        verbose_name="Pertanian dan Kehutanan", default=None)
    b = models.FloatField(
        verbose_name="Pertambangan dan Penggalian", default=None)
    c = models.FloatField(verbose_name="Industri", default=None)
    d = models.FloatField(verbose_name="Listrik dan Gas",
                          default=None)
    e = models.FloatField(
        verbose_name="Air, Sampah/Limbah dan Daur Ulang", default=None)
    f = models.FloatField(verbose_name="Kontruksi", default=None)
    g = models.FloatField(
        verbose_name="Perdagangan, Reparasi Mobil/Sepeda Motor", default=None)
    h = models.FloatField(
        verbose_name="Transportasi dan Pergudangan", default=None)
    i = models.FloatField(
        verbose_name="Penyediaan Akomodasi dan Makan Minum", default=None)
    j = models.FloatField(
        verbose_name="Informasi dan Komunikasi", default=None)
    k = models.FloatField(
        verbose_name="Jasa Keuangan dan Asuransi", default=None)
    l = models.FloatField(verbose_name="Real Estate", default=None)
    m_n = models.FloatField(
        verbose_name="Jasa Perusahaan", default=None)
    o = models.FloatField(
        verbose_name="Administrasi Pemerintahan, Pertahanan, dan Jaminan Sosial Wajib", default=None)
    p = models.FloatField(verbose_name="Jasa Pendidikan",
                          default=None)
    q = models.FloatField(
        verbose_name="Jasa Kesehatan dan Kegiatan Sosial", default=None)
    r_s_t_u = models.FloatField(
        verbose_name="Jasa Lainnya", default=None)
    total_pdrb = models.FloatField(
        verbose_name="Total", default=None, editable=False)
    tanggal = models.DateField()

    def save(self, *args, **kwargs):
        self.total_pdrb = self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h + \
            self.i + self.j + self.k + self.l + self.m_n + \
            self.o + self.p + self.q + self.r_s_t_u
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tanggal

    class Meta:
        verbose_name = "Sumber Pertumbuhan Produk Domestik Regional Bruto Non Migas"
        verbose_name_plural = "Sumber Pertumbuhan Produk Domestik Regional Bruto Non Migas"


class TenagaKerja(models.Model):
    CHOICES = [
        ("LK", "Laki-Laki"),
        ("PR", "Perempuan")
    ]
    angkatan_kerja = models.FloatField(default=None)
    bekerja = models.FloatField(default=None)
    pengangguran = models.FloatField(default=None)
    bkn_angkatan_kerja = models.FloatField(default=None)
    sekolah = models.FloatField(default=None)
    urur_ruta = models.FloatField(default=None)
    lainnya = models.FloatField(default=None)
    gender = models.CharField(max_length=15, choices=CHOICES)

    def __str__(self):
        return self.tanggal

    class Meta:
        verbose_name = "Ketenagakerjaan"
        verbose_name_plural = "Ketenagakerjaan"


class Kemiskinan(models.Model):
    ppdk_mskn = models.FloatField(default=None)
    p0 = models.FloatField(default=None)
    p1 = models.FloatField(default=None)
    p2 = models.FloatField(default=None)
    gk = models.FloatField(default=None)
    tanggal = models.DateField()

    def __str__(self):
        return self.tanggal

    class Meta:
        verbose_name = "Kemiskinan"
        verbose_name_plural = "Kemiskinan"

# class ForeignTrade(models.Model):


class Ipm(models.Model):
    uhh = models.FloatField(default=None)
    rls = models.FloatField(default=None)
    hls = models.FloatField(default=None)
    ppp = models.FloatField(default=None)
    ipm = models.FloatField(default=None)
    pertumbuhan = models.FloatField(default=None)
    tanggal = models.DateField()

    def __str__(self):
        return self.tanggal

    class Meta:
        verbose_name = "Indeks Pembangunan Manusia"
        verbose_name_plural = "Indeks Pembangunan Manusia"


class Inflasi(models.Model):
    sandang = models.FloatField(default=None)
    sembako = models.FloatField(default=None)
    perumahan = models.FloatField(default=None)
    kesehatan = models.FloatField(default=None)
    transportasi = models.FloatField(default=None)
    informasi = models.FloatField(default=None)
    rekreasi = models.FloatField(default=None)
    pendidikan = models.FloatField(default=None)
    penyedia_pangan = models.FloatField(default=None)
    perawatan_pribadi = models.FloatField(default=None)
    total_inflasi = models.FloatField(default=None)
    tanggal = models.DateField()

    def save(self, *args, **kwargs):
        self.total_inflasi = self.sandang + self.sembako + self.perumahan + self.kesehatan + \
            self.transportasi + self.informasi + self.rekreasi + \
            self.pendidikan + self.penyedia_pangan + self.perawatan_pribadi
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tanggal

    class Meta:
        verbose_name = "Inflasi"
        verbose_name_plural = "Inflasi"


class InflasiDod(models.Model):

    sandang = models.FloatField(default=None)
    sembako = models.FloatField(default=None)
    perumahan = models.FloatField(default=None)
    kesehatan = models.FloatField(default=None)
    transportasi = models.FloatField(default=None)
    informasi = models.FloatField(default=None)
    rekreasi = models.FloatField(default=None)
    pendidikan = models.FloatField(default=None)
    penyedia_pangan = models.FloatField(default=None)
    perawatan_pribadi = models.FloatField(default=None)
    total_inflasi = models.FloatField(default=None)
    tanggal = models.DateField()

    def save(self, *args, **kwargs):
        self.total_inflasi = self.sandang + self.sembako + self.perumahan + self.kesehatan + \
            self.transportasi + self.informasi + self.rekreasi + \
            self.pendidikan + self.penyedia_pangan + self.perawatan_pribadi
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tanggal

    class Meta:
        verbose_name = "Inflasi Date on Date"
        verbose_name_plural = "Inflasi Date on Date"


class InflasiYoy(models.Model):
    sandang = models.FloatField(default=None)
    sembako = models.FloatField(default=None)
    perumahan = models.FloatField(default=None)
    kesehatan = models.FloatField(default=None)
    transportasi = models.FloatField(default=None)
    informasi = models.FloatField(default=None)
    rekreasi = models.FloatField(default=None)
    pendidikan = models.FloatField(default=None)
    penyedia_pangan = models.FloatField(default=None)
    perawatan_pribadi = models.FloatField(default=None)
    total_inflasi = models.FloatField(default=None)
    tanggal = models.DateField()

    def save(self, *args, **kwargs):
        self.total_inflasi = self.sandang + self.sembako + self.perumahan + self.kesehatan + \
            self.transportasi + self.informasi + self.rekreasi + \
            self.pendidikan + self.penyedia_pangan + self.perawatan_pribadi
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tanggal

    class Meta:
        verbose_name = "Inflasi Year on Year"
        verbose_name_plural = "Inflasi Year on Year"


class PendudukLaki(models.Model):
    a = models.IntegerField(default=None, verbose_name='0-4 Tahun')
    b = models.IntegerField(default=None, verbose_name='5-9 Tahun')
    c = models.IntegerField(default=None, verbose_name='10-14 Tahun')
    d = models.IntegerField(default=None, verbose_name='15-19 Tahun')
    e = models.IntegerField(default=None, verbose_name='20-24 Tahun')
    f = models.IntegerField(default=None, verbose_name='25-29 Tahun')
    g = models.IntegerField(default=None, verbose_name='30-34 Tahun')
    h = models.IntegerField(default=None, verbose_name='35-39 Tahun')
    i = models.IntegerField(default=None, verbose_name='40-44 Tahun')
    j = models.IntegerField(default=None, verbose_name='45-49 Tahun')
    k = models.IntegerField(default=None, verbose_name='50-54 Tahun')
    l = models.IntegerField(default=None, verbose_name='55-59 Tahun')
    m = models.IntegerField(default=None, verbose_name='60-64 Tahun')
    n = models.IntegerField(default=None, verbose_name='65-69 Tahun')
    o = models.IntegerField(default=None, verbose_name='70-74 Tahun')
    p = models.IntegerField(default=None, verbose_name='75+ Tahun')
    total = models.IntegerField(default=None, editable=False)
    tanggal = models.DateField()

    def save(self, *args, **kwargs):
        self.total = self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h + \
            self.i + self.j + self.k + self.l + self.m + \
            self.n + self.o + self.p
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tanggal


class PendudukPr(models.Model):
    a = models.IntegerField(default=None, verbose_name='0-4 Tahun')
    b = models.IntegerField(default=None, verbose_name='5-9 Tahun')
    c = models.IntegerField(default=None, verbose_name='10-14 Tahun')
    d = models.IntegerField(default=None, verbose_name='15-19 Tahun')
    e = models.IntegerField(default=None, verbose_name='20-24 Tahun')
    f = models.IntegerField(default=None, verbose_name='25-29 Tahun')
    g = models.IntegerField(default=None, verbose_name='30-34 Tahun')
    h = models.IntegerField(default=None, verbose_name='35-39 Tahun')
    i = models.IntegerField(default=None, verbose_name='40-44 Tahun')
    j = models.IntegerField(default=None, verbose_name='45-49 Tahun')
    k = models.IntegerField(default=None, verbose_name='50-54 Tahun')
    l = models.IntegerField(default=None, verbose_name='55-59 Tahun')
    m = models.IntegerField(default=None, verbose_name='60-64 Tahun')
    n = models.IntegerField(default=None, verbose_name='65-69 Tahun')
    o = models.IntegerField(default=None, verbose_name='70-74 Tahun')
    p = models.IntegerField(default=None, verbose_name='75+ Tahun')
    total = models.IntegerField(default=None, editable=False)
    tanggal = models.DateField()

    def save(self, *args, **kwargs):
        self.total = self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h + \
            self.i + self.j + self.k + self.l + self.m + \
            self.n + self.o + self.p
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tanggal


class PendudukLakiKecamatan(models.Model):
    KECAMATAN = [
        ('Dayeuhluhur', 'Dayeuhluhur'),
        ('Wanareja', 'Wanareja'),
        ('Majenang', 'Majenang'),
        ('Cimanggu', 'Cimanggu'),
        ('Karangpucung', 'Karangpucung'),
        ('Cipari', 'Cipari'),
        ('Sidareja', 'Sidareja'),
        ('Kedungreja', 'Kedungreja'),
        ('Patimuan', 'Patimuan'),
        ('Gandrungmangu', 'Gandrungmangu'),
        ('Bantarsari', 'Bantarsari'),
        ('Kawunganten', 'Kawunganten'),
        ('Kampung Laut',  'Kampung Laut'),
        ('Jeruklegi', 'Jeruklegi'),
        ('Kesugihan', 'Kesugihan'),
        ('Adipala', 'Adipala'),
        ('Maos', 'Maos'),
        ('Kroya', 'Kroya'),
        ('Binangun', 'Binangun'),
        ('Sampang', 'Sampang'),
        ('Nusawungu', 'Nusawungu'),
        ('Cilacap Selatan', 'Cilacap Selatan'),
        ('Cilacap Tengah', 'Cilacap Tengah'),
        ('Cilacap Utara', 'Cilacap Utara'),
    ]
    kec = models.CharField(verbose_name='Kecamatan',
                           choices=KECAMATAN, max_length=35, default='Dayeuhluhur')
    a = models.IntegerField(default=None, verbose_name='0-4 Tahun')
    b = models.IntegerField(default=None, verbose_name='5-9 Tahun')
    c = models.IntegerField(default=None, verbose_name='10-14 Tahun')
    d = models.IntegerField(default=None, verbose_name='15-19 Tahun')
    e = models.IntegerField(default=None, verbose_name='20-24 Tahun')
    f = models.IntegerField(default=None, verbose_name='25-29 Tahun')
    g = models.IntegerField(default=None, verbose_name='30-34 Tahun')
    h = models.IntegerField(default=None, verbose_name='35-39 Tahun')
    i = models.IntegerField(default=None, verbose_name='40-44 Tahun')
    j = models.IntegerField(default=None, verbose_name='45-49 Tahun')
    k = models.IntegerField(default=None, verbose_name='50-54 Tahun')
    l = models.IntegerField(default=None, verbose_name='55-59 Tahun')
    m = models.IntegerField(default=None, verbose_name='60-64 Tahun')
    n = models.IntegerField(default=None, verbose_name='65-69 Tahun')
    o = models.IntegerField(default=None, verbose_name='70-74 Tahun')
    p = models.IntegerField(default=None, verbose_name='75+ Tahun')
    total = models.IntegerField(default=None, editable=False)
    tanggal = models.DateField()

    def save(self, *args, **kwargs):
        self.total = self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h + \
            self.i + self.j + self.k + self.l + self.m + \
            self.n + self.o + self.p
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tanggal


class PendudukPrKecamatan(models.Model):
    KECAMATAN = [
        ('Dayeuhluhur', 'Dayeuhluhur'),
        ('Wanareja', 'Wanareja'),
        ('Majenang', 'Majenang'),
        ('Cimanggu', 'Cimanggu'),
        ('Karangpucung', 'Karangpucung'),
        ('Cipari', 'Cipari'),
        ('Sidareja', 'Sidareja'),
        ('Kedungreja', 'Kedungreja'),
        ('Patimuan', 'Patimuan'),
        ('Gandrungmangu', 'Gandrungmangu'),
        ('Bantarsari', 'Bantarsari'),
        ('Kawunganten', 'Kawunganten'),
        ('Kampung Laut',  'Kampung Laut'),
        ('Jeruklegi', 'Jeruklegi'),
        ('Kesugihan', 'Kesugihan'),
        ('Adipala', 'Adipala'),
        ('Maos', 'Maos'),
        ('Kroya', 'Kroya'),
        ('Binangun', 'Binangun'),
        ('Sampang', 'Sampang'),
        ('Nusawungu', 'Nusawungu'),
        ('Cilacap Selatan', 'Cilacap Selatan'),
        ('Cilacap Tengah', 'Cilacap Tengah'),
        ('Cilacap Utara', 'Cilacap Utara'),
    ]
    kec = models.CharField(verbose_name='Kecamatan',
                           choices=KECAMATAN, max_length=35, default='Dayeuhluhur')
    a = models.IntegerField(default=None, verbose_name='0-4 Tahun')
    b = models.IntegerField(default=None, verbose_name='5-9 Tahun')
    c = models.IntegerField(default=None, verbose_name='10-14 Tahun')
    d = models.IntegerField(default=None, verbose_name='15-19 Tahun')
    e = models.IntegerField(default=None, verbose_name='20-24 Tahun')
    f = models.IntegerField(default=None, verbose_name='25-29 Tahun')
    g = models.IntegerField(default=None, verbose_name='30-34 Tahun')
    h = models.IntegerField(default=None, verbose_name='35-39 Tahun')
    i = models.IntegerField(default=None, verbose_name='40-44 Tahun')
    j = models.IntegerField(default=None, verbose_name='45-49 Tahun')
    k = models.IntegerField(default=None, verbose_name='50-54 Tahun')
    l = models.IntegerField(default=None, verbose_name='55-59 Tahun')
    m = models.IntegerField(default=None, verbose_name='60-64 Tahun')
    n = models.IntegerField(default=None, verbose_name='65-69 Tahun')
    o = models.IntegerField(default=None, verbose_name='70-74 Tahun')
    p = models.IntegerField(default=None, verbose_name='75+ Tahun')
    total = models.IntegerField(default=None, editable=False)
    tanggal = models.DateField()

    def save(self, *args, **kwargs):
        self.total = self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h + \
            self.i + self.j + self.k + self.l + self.m + \
            self.n + self.o + self.p
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tanggal


class Kota (models.Model):
    nama_kota = models.TextField(max_length=50)
    inflasi = models.ForeignKey(
        Inflasi, related_name='inflasi_kota', on_delete=models.CASCADE)
    inflasi_dod = models.ForeignKey(
        InflasiDod, related_name="inflasi_dod_kota", on_delete=models.CASCADE)
    inlfasi_yoy = models.ForeignKey(
        InflasiYoy, related_name="inflasi_yoy_kota", on_delete=models.CASCADE)
    pdrb_migas = models.ForeignKey(
        PdrbMigas, related_name='pdrb_kota', on_delete=models.CASCADE)
    dist_pdrb_migas = models.ForeignKey(
        DistribusiPdrbMigas, related_name="distribusi_pdrb_migas", on_delete=models.CASCADE)
    laju_pert_pdrb_migas = models.ForeignKey(
        LajuPertumbuhanPdrbMigas, related_name="laju_pertumbuhan_pdrb_migas", on_delete=models.CASCADE)
    sum_pert_pdrb_migas = models.ForeignKey(
        SumberPertumbuhanPdrbMigas, related_name="sumber_pertumbuhan_pdrb_migas", on_delete=models.CASCADE)
    pdrb_non_migas = models.ForeignKey(
        PdrbNonMigas, related_name='pdrb_kota', on_delete=models.CASCADE)
    dist_pdrb_non_migas = models.ForeignKey(
        DistribusiPdrbNonMigas, related_name="distribusi_pdrb_non_migas", on_delete=models.CASCADE)
    laju_pert_pdrb_non_migas = models.ForeignKey(
        LajuPertumbuhanPdrbNonMigas, related_name="laju_pertumbuhan_pdrb_non_migas", on_delete=models.CASCADE)
    sum_pert_pdrb_non_migas = models.ForeignKey(
        SumberPertumbuhanPdrbNonMigas, related_name="sumber_pertumbuhan_pdrb_non_migas", on_delete=models.CASCADE)
    pend_lk = models.ForeignKey(
        PendudukLaki, related_name="penduduk_laki", on_delete=models.CASCADE)
    pend_pr = models.ForeignKey(
        PendudukPr, related_name="penduduk_perempuan", on_delete=models.CASCADE)
    total_pend = models.IntegerField()

    def save(self, *args, **kwargs):
        self.total_pend = self.pend_lk + self.pend_pr
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tanggal

    class Meta:
        verbose_name = "Kota"
        verbose_name_plural = "Kota"
