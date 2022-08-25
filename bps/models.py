from django.db import models
# Create your models here.


class PdrbMigas(models.Model):
    a = models.FloatField(
        verbose_name="Pertanian dan Kehutanan")
    b = models.FloatField(
        verbose_name="Pertambangan dan Penggalian")
    c = models.FloatField(verbose_name="Industri")
    d = models.FloatField(verbose_name="Listrik dan Gas",
                          )
    e = models.FloatField(
        verbose_name="Air, Sampah/Limbah dan Daur Ulang")
    f = models.FloatField(verbose_name="Kontruksi")
    g = models.FloatField(
        verbose_name="Perdagangan, Reparasi Mobil/Sepeda Motor")
    h = models.FloatField(
        verbose_name="Transportasi dan Pergudangan")
    i = models.FloatField(
        verbose_name="Penyediaan Akomodasi dan Makan Minum")
    j = models.FloatField(
        verbose_name="Informasi dan Komunikasi")
    k = models.FloatField(
        verbose_name="Jasa Keuangan dan Asuransi")
    l = models.FloatField(verbose_name="Real Estate")
    m_n = models.FloatField(
        verbose_name="Jasa Perusahaan")
    o = models.FloatField(
        verbose_name="Administrasi Pemerintahan, Pertahanan, dan Jaminan Sosial Wajib")
    p = models.FloatField(verbose_name="Jasa Pendidikan",
                          )
    q = models.FloatField(
        verbose_name="Jasa Kesehatan dan Kegiatan Sosial")
    r_s_t_u = models.FloatField(
        verbose_name="Jasa Lainnya")
    # # total_pdrb = models.FloatField(
    #     verbose_name="Total", editable=False, null=True)
    tanggal = models.DateField(null=True)

    @property
    def total_pdrb(self):
        total = self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h + \
            self.i + self.j + self.k + self.l + self.m_n + \
            self.o + self.p + self.q + self.r_s_t_u
        return total

    def __str__(self):
        return str(self.tanggal)

    class Meta:
        verbose_name = "Produk Domestik Regional Bruto Dengan Migas"
        verbose_name_plural = "Produk Domestik Regional Bruto Dengan Migas"


class DistribusiPdrbMigas(models.Model):
    a = models.FloatField(
        verbose_name="Pertanian dan Kehutanan")
    b = models.FloatField(
        verbose_name="Pertambangan dan Penggalian")
    c = models.FloatField(verbose_name="Industri")
    d = models.FloatField(verbose_name="Listrik dan Gas",
                          )
    e = models.FloatField(
        verbose_name="Air, Sampah/Limbah dan Daur Ulang")
    f = models.FloatField(verbose_name="Kontruksi")
    g = models.FloatField(
        verbose_name="Perdagangan, Reparasi Mobil/Sepeda Motor")
    h = models.FloatField(
        verbose_name="Transportasi dan Pergudangan")
    i = models.FloatField(
        verbose_name="Penyediaan Akomodasi dan Makan Minum")
    j = models.FloatField(
        verbose_name="Informasi dan Komunikasi")
    k = models.FloatField(
        verbose_name="Jasa Keuangan dan Asuransi")
    l = models.FloatField(verbose_name="Real Estate")
    m_n = models.FloatField(
        verbose_name="Jasa Perusahaan")
    o = models.FloatField(
        verbose_name="Administrasi Pemerintahan, Pertahanan, dan Jaminan Sosial Wajib")
    p = models.FloatField(verbose_name="Jasa Pendidikan",
                          )
    q = models.FloatField(
        verbose_name="Jasa Kesehatan dan Kegiatan Sosial")
    r_s_t_u = models.FloatField(
        verbose_name="Jasa Lainnya")
    # # total_pdrb = models.FloatField(
    #     verbose_name="Total", editable=False, null=True)
    tanggal = models.DateField(null=True)

    @property
    def total_pdrb(self):
        total = self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h + \
            self.i + self.j + self.k + self.l + self.m_n + \
            self.o + self.p + self.q + self.r_s_t_u
        return total

    def __str__(self):
        return str(self.tanggal)

    class Meta:
        verbose_name = "Distribusi Produk Domestik Regional Bruto Dengan Migas"
        verbose_name_plural = "Distribusi Produk Domestik Regional Bruto Dengan Migas"


class LajuPertumbuhanPdrbMigas(models.Model):
    a = models.FloatField(
        verbose_name="Pertanian dan Kehutanan")
    b = models.FloatField(
        verbose_name="Pertambangan dan Penggalian")
    c = models.FloatField(verbose_name="Industri")
    d = models.FloatField(verbose_name="Listrik dan Gas",
                          )
    e = models.FloatField(
        verbose_name="Air, Sampah/Limbah dan Daur Ulang")
    f = models.FloatField(verbose_name="Kontruksi")
    g = models.FloatField(
        verbose_name="Perdagangan, Reparasi Mobil/Sepeda Motor")
    h = models.FloatField(
        verbose_name="Transportasi dan Pergudangan")
    i = models.FloatField(
        verbose_name="Penyediaan Akomodasi dan Makan Minum")
    j = models.FloatField(
        verbose_name="Informasi dan Komunikasi")
    k = models.FloatField(
        verbose_name="Jasa Keuangan dan Asuransi")
    l = models.FloatField(verbose_name="Real Estate")
    m_n = models.FloatField(
        verbose_name="Jasa Perusahaan")
    o = models.FloatField(
        verbose_name="Administrasi Pemerintahan, Pertahanan, dan Jaminan Sosial Wajib")
    p = models.FloatField(verbose_name="Jasa Pendidikan",
                          )
    q = models.FloatField(
        verbose_name="Jasa Kesehatan dan Kegiatan Sosial")
    r_s_t_u = models.FloatField(
        verbose_name="Jasa Lainnya")
    # # total_pdrb = models.FloatField(
    #     verbose_name="Total", editable=False, null=True)
    tanggal = models.DateField(null=True)

    @property
    def total_pdrb(self):
        total = self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h + \
            self.i + self.j + self.k + self.l + self.m_n + \
            self.o + self.p + self.q + self.r_s_t_u
        return total

    def __str__(self):
        return str(self.tanggal)

    class Meta:
        verbose_name = "Laju Pertumbuhan Produk Domestik Regional Bruto Dengan Migas"
        verbose_name_plural = "Laju Pertumbuhan Produk Domestik Regional Bruto Dengan Migas"


class SumberPertumbuhanPdrbMigas(models.Model):
    a = models.FloatField(
        verbose_name="Pertanian dan Kehutanan")
    b = models.FloatField(
        verbose_name="Pertambangan dan Penggalian")
    c = models.FloatField(verbose_name="Industri")
    d = models.FloatField(verbose_name="Listrik dan Gas",
                          )
    e = models.FloatField(
        verbose_name="Air, Sampah/Limbah dan Daur Ulang")
    f = models.FloatField(verbose_name="Kontruksi")
    g = models.FloatField(
        verbose_name="Perdagangan, Reparasi Mobil/Sepeda Motor")
    h = models.FloatField(
        verbose_name="Transportasi dan Pergudangan")
    i = models.FloatField(
        verbose_name="Penyediaan Akomodasi dan Makan Minum")
    j = models.FloatField(
        verbose_name="Informasi dan Komunikasi")
    k = models.FloatField(
        verbose_name="Jasa Keuangan dan Asuransi")
    l = models.FloatField(verbose_name="Real Estate")
    m_n = models.FloatField(
        verbose_name="Jasa Perusahaan")
    o = models.FloatField(
        verbose_name="Administrasi Pemerintahan, Pertahanan, dan Jaminan Sosial Wajib")
    p = models.FloatField(verbose_name="Jasa Pendidikan",
                          )
    q = models.FloatField(
        verbose_name="Jasa Kesehatan dan Kegiatan Sosial")
    r_s_t_u = models.FloatField(
        verbose_name="Jasa Lainnya")
    # # total_pdrb = models.FloatField(
    #     verbose_name="Total", editable=False, null=True)
    tanggal = models.DateField(null=True)

    @property
    def total_pdrb(self):
        total = self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h + \
            self.i + self.j + self.k + self.l + self.m_n + \
            self.o + self.p + self.q + self.r_s_t_u
        return total

    def __str__(self):
        return str(self.tanggal)

    class Meta:
        verbose_name = "Sumber Pertumbuhan Produk Domestik Regional Bruto Dengan Migas"
        verbose_name_plural = "Sumber Pertumbuhan Produk Domestik Regional Bruto Dengan Migas"


class PdrbNonMigas(models.Model):
    a = models.FloatField(
        verbose_name="Pertanian dan Kehutanan")
    b = models.FloatField(
        verbose_name="Pertambangan dan Penggalian")
    c = models.FloatField(verbose_name="Industri")
    d = models.FloatField(verbose_name="Listrik dan Gas",
                          )
    e = models.FloatField(
        verbose_name="Air, Sampah/Limbah dan Daur Ulang")
    f = models.FloatField(verbose_name="Kontruksi")
    g = models.FloatField(
        verbose_name="Perdagangan, Reparasi Mobil/Sepeda Motor")
    h = models.FloatField(
        verbose_name="Transportasi dan Pergudangan")
    i = models.FloatField(
        verbose_name="Penyediaan Akomodasi dan Makan Minum")
    j = models.FloatField(
        verbose_name="Informasi dan Komunikasi")
    k = models.FloatField(
        verbose_name="Jasa Keuangan dan Asuransi")
    l = models.FloatField(verbose_name="Real Estate")
    m_n = models.FloatField(
        verbose_name="Jasa Perusahaan")
    o = models.FloatField(
        verbose_name="Administrasi Pemerintahan, Pertahanan, dan Jaminan Sosial Wajib")
    p = models.FloatField(verbose_name="Jasa Pendidikan",
                          )
    q = models.FloatField(
        verbose_name="Jasa Kesehatan dan Kegiatan Sosial")
    r_s_t_u = models.FloatField(
        verbose_name="Jasa Lainnya")
    # # total_pdrb = models.FloatField(
    #     verbose_name="Total", editable=False, null=True)
    tanggal = models.DateField(null=True)

    @property
    def total_pdrb(self):
        total = self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h + \
            self.i + self.j + self.k + self.l + self.m_n + \
            self.o + self.p + self.q + self.r_s_t_u
        return total

    def __str__(self):
        return str(self.tanggal)

    class Meta:
        verbose_name = "Produk Domestik Regional Bruto Non Migas"
        verbose_name_plural = "Produk Domestik Regional Bruto Non Migas"


class DistribusiPdrbNonMigas(models.Model):
    a = models.FloatField(
        verbose_name="Pertanian dan Kehutanan")
    b = models.FloatField(
        verbose_name="Pertambangan dan Penggalian")
    c = models.FloatField(verbose_name="Industri")
    d = models.FloatField(verbose_name="Listrik dan Gas",
                          )
    e = models.FloatField(
        verbose_name="Air, Sampah/Limbah dan Daur Ulang")
    f = models.FloatField(verbose_name="Kontruksi")
    g = models.FloatField(
        verbose_name="Perdagangan, Reparasi Mobil/Sepeda Motor")
    h = models.FloatField(
        verbose_name="Transportasi dan Pergudangan")
    i = models.FloatField(
        verbose_name="Penyediaan Akomodasi dan Makan Minum")
    j = models.FloatField(
        verbose_name="Informasi dan Komunikasi")
    k = models.FloatField(
        verbose_name="Jasa Keuangan dan Asuransi")
    l = models.FloatField(verbose_name="Real Estate")
    m_n = models.FloatField(
        verbose_name="Jasa Perusahaan")
    o = models.FloatField(
        verbose_name="Administrasi Pemerintahan, Pertahanan, dan Jaminan Sosial Wajib")
    p = models.FloatField(verbose_name="Jasa Pendidikan",
                          )
    q = models.FloatField(
        verbose_name="Jasa Kesehatan dan Kegiatan Sosial")
    r_s_t_u = models.FloatField(
        verbose_name="Jasa Lainnya")
    # # total_pdrb = models.FloatField(
    #     verbose_name="Total", editable=False, null=True)
    tanggal = models.DateField(null=True)

    @property
    def total_pdrb(self):
        total = self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h + \
            self.i + self.j + self.k + self.l + self.m_n + \
            self.o + self.p + self.q + self.r_s_t_u
        return total

    def __str__(self):
        return str(self.tanggal)

    class Meta:
        verbose_name = "Distribusi Produk Domestik Regional Bruto Non Migas"
        verbose_name_plural = "Distribusi Produk Domestik Regional Bruto Non Migas"


class LajuPertumbuhanPdrbNonMigas(models.Model):
    a = models.FloatField(
        verbose_name="Pertanian dan Kehutanan")
    b = models.FloatField(
        verbose_name="Pertambangan dan Penggalian")
    c = models.FloatField(verbose_name="Industri")
    d = models.FloatField(verbose_name="Listrik dan Gas",
                          )
    e = models.FloatField(
        verbose_name="Air, Sampah/Limbah dan Daur Ulang")
    f = models.FloatField(verbose_name="Kontruksi")
    g = models.FloatField(
        verbose_name="Perdagangan, Reparasi Mobil/Sepeda Motor")
    h = models.FloatField(
        verbose_name="Transportasi dan Pergudangan")
    i = models.FloatField(
        verbose_name="Penyediaan Akomodasi dan Makan Minum")
    j = models.FloatField(
        verbose_name="Informasi dan Komunikasi")
    k = models.FloatField(
        verbose_name="Jasa Keuangan dan Asuransi")
    l = models.FloatField(verbose_name="Real Estate")
    m_n = models.FloatField(
        verbose_name="Jasa Perusahaan")
    o = models.FloatField(
        verbose_name="Administrasi Pemerintahan, Pertahanan, dan Jaminan Sosial Wajib")
    p = models.FloatField(verbose_name="Jasa Pendidikan",
                          )
    q = models.FloatField(
        verbose_name="Jasa Kesehatan dan Kegiatan Sosial")
    r_s_t_u = models.FloatField(
        verbose_name="Jasa Lainnya")
    # # total_pdrb = models.FloatField(
    #     verbose_name="Total", editable=False, null=True)
    tanggal = models.DateField(null=True)

    @property
    def total_pdrb(self):
        total = self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h + \
            self.i + self.j + self.k + self.l + self.m_n + \
            self.o + self.p + self.q + self.r_s_t_u
        return total

    def __str__(self):
        return str(self.tanggal)

    class Meta:
        verbose_name = "Laju Pertumbuhan Produk Domestik Regional Bruto Non Migas"
        verbose_name_plural = "Laju Pertumbuhan Produk Domestik Regional Bruto Non Migas"


class SumberPertumbuhanPdrbNonMigas(models.Model):
    a = models.FloatField(
        verbose_name="Pertanian dan Kehutanan")
    b = models.FloatField(
        verbose_name="Pertambangan dan Penggalian")
    c = models.FloatField(verbose_name="Industri")
    d = models.FloatField(verbose_name="Listrik dan Gas",
                          )
    e = models.FloatField(
        verbose_name="Air, Sampah/Limbah dan Daur Ulang")
    f = models.FloatField(verbose_name="Kontruksi")
    g = models.FloatField(
        verbose_name="Perdagangan, Reparasi Mobil/Sepeda Motor")
    h = models.FloatField(
        verbose_name="Transportasi dan Pergudangan")
    i = models.FloatField(
        verbose_name="Penyediaan Akomodasi dan Makan Minum")
    j = models.FloatField(
        verbose_name="Informasi dan Komunikasi")
    k = models.FloatField(
        verbose_name="Jasa Keuangan dan Asuransi")
    l = models.FloatField(verbose_name="Real Estate")
    m_n = models.FloatField(
        verbose_name="Jasa Perusahaan")
    o = models.FloatField(
        verbose_name="Administrasi Pemerintahan, Pertahanan, dan Jaminan Sosial Wajib")
    p = models.FloatField(verbose_name="Jasa Pendidikan",
                          )
    q = models.FloatField(
        verbose_name="Jasa Kesehatan dan Kegiatan Sosial")
    r_s_t_u = models.FloatField(
        verbose_name="Jasa Lainnya")
    # # total_pdrb = models.FloatField(
    #     verbose_name="Total", editable=False, null=True)
    tanggal = models.DateField(null=True)

    @property
    def total_pdrb(self):
        total = self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h + \
            self.i + self.j + self.k + self.l + self.m_n + \
            self.o + self.p + self.q + self.r_s_t_u
        return total

    def __str__(self):
        return str(self.tanggal)

    class Meta:
        verbose_name = "Sumber Pertumbuhan Produk Domestik Regional Bruto Non Migas"
        verbose_name_plural = "Sumber Pertumbuhan Produk Domestik Regional Bruto Non Migas"


class TenagaKerja(models.Model):
    CHOICES = [
        ("LK", "Laki-Laki"),
        ("PR", "Perempuan")
    ]
    angkatan_kerja = models.FloatField(null=True)
    bekerja = models.FloatField(null=True)
    pengangguran = models.FloatField(null=True)
    bkn_angkatan_kerja = models.FloatField(null=True)
    sekolah = models.FloatField(null=True)
    urur_ruta = models.FloatField(null=True)
    lainnya = models.FloatField(null=True)
    gender = models.CharField(max_length=15, choices=CHOICES)

    def __str__(self):
        return str(self.tanggal)

    class Meta:
        verbose_name = "Ketenagakerjaan"
        verbose_name_plural = "Ketenagakerjaan"


class Kemiskinan(models.Model):
    ppdk_mskn = models.FloatField(null=True)
    p0 = models.FloatField(null=True)
    p1 = models.FloatField(null=True)
    p2 = models.FloatField(null=True)
    gk = models.FloatField(null=True)
    tanggal = models.DateField(null=True)

    def __str__(self):
        return str(self.tanggal)

    class Meta:
        verbose_name = "Kemiskinan"
        verbose_name_plural = "Kemiskinan"

# class ForeignTrade(models.Model):


class Ipm(models.Model):
    uhh = models.FloatField(null=True)
    rls = models.FloatField(null=True)
    hls = models.FloatField(null=True)
    ppp = models.FloatField(null=True)
    ipm = models.FloatField(null=True)
    pertumbuhan = models.FloatField(null=True)
    tanggal = models.DateField(null=True)

    def __str__(self):
        return str(self.tanggal)

    class Meta:
        verbose_name = "Indeks Pembangunan Manusia"
        verbose_name_plural = "Indeks Pembangunan Manusia"


class Inflasi(models.Model):
    sandang = models.FloatField(null=True)
    sembako = models.FloatField(null=True)
    perumahan = models.FloatField(null=True)
    kesehatan = models.FloatField(null=True)
    transportasi = models.FloatField(null=True)
    informasi = models.FloatField(null=True)
    rekreasi = models.FloatField(null=True)
    pendidikan = models.FloatField(null=True)
    penyedia_pangan = models.FloatField(null=True)
    perawatan_pribadi = models.FloatField(null=True)
    total_inflasi = models.FloatField(null=True)
    tanggal = models.DateField(null=True)

    @property
    def total_inflasi(self):
        total = self.sandang + self.sembako + self.perumahan + self.kesehatan + \
            self.transportasi + self.informasi + self.rekreasi + \
            self.pendidikan + self.penyedia_pangan + self.perawatan_pribadi
        return total

    def __str__(self):
        return str(self.tanggal)

    class Meta:
        verbose_name = "Inflasi"
        verbose_name_plural = "Inflasi"


class InflasiDod(models.Model):

    sandang = models.FloatField(null=True)
    sembako = models.FloatField(null=True)
    perumahan = models.FloatField(null=True)
    kesehatan = models.FloatField(null=True)
    transportasi = models.FloatField(null=True)
    informasi = models.FloatField(null=True)
    rekreasi = models.FloatField(null=True)
    pendidikan = models.FloatField(null=True)
    penyedia_pangan = models.FloatField(null=True)
    perawatan_pribadi = models.FloatField(null=True)
    total_inflasi = models.FloatField(null=True)
    tanggal = models.DateField(null=True)

    @property
    def total_inflasi(self):
        total = self.sandang + self.sembako + self.perumahan + self.kesehatan + \
            self.transportasi + self.informasi + self.rekreasi + \
            self.pendidikan + self.penyedia_pangan + self.perawatan_pribadi
        return total

    def __str__(self):
        return str(self.tanggal)

    class Meta:
        verbose_name = "Inflasi Date on Date"
        verbose_name_plural = "Inflasi Date on Date"


class InflasiYoy(models.Model):
    sandang = models.FloatField(null=True)
    sembako = models.FloatField(null=True)
    perumahan = models.FloatField(null=True)
    kesehatan = models.FloatField(null=True)
    transportasi = models.FloatField(null=True)
    informasi = models.FloatField(null=True)
    rekreasi = models.FloatField(null=True)
    pendidikan = models.FloatField(null=True)
    penyedia_pangan = models.FloatField(null=True)
    perawatan_pribadi = models.FloatField(null=True)
    total_inflasi = models.FloatField(null=True)
    tanggal = models.DateField(null=True)

    @property
    def total_inflasi(self):
        total = self.sandang + self.sembako + self.perumahan + self.kesehatan + self.transportasi + \
            self.informasi + self.rekreasi + self.pendidikan + \
            self.penyedia_pangan + self.perawatan_pribadi
        return total

    def __str__(self):
        return str(self.tanggal)

    class Meta:
        verbose_name = "Inflasi Year on Year"
        verbose_name_plural = "Inflasi Year on Year"


class PendudukLaki(models.Model):
    a = models.IntegerField(verbose_name='0-4 Tahun')
    b = models.IntegerField(verbose_name='5-9 Tahun')
    c = models.IntegerField(verbose_name='10-14 Tahun')
    d = models.IntegerField(verbose_name='15-19 Tahun')
    e = models.IntegerField(verbose_name='20-24 Tahun')
    f = models.IntegerField(verbose_name='25-29 Tahun')
    g = models.IntegerField(verbose_name='30-34 Tahun')
    h = models.IntegerField(verbose_name='35-39 Tahun')
    i = models.IntegerField(verbose_name='40-44 Tahun')
    j = models.IntegerField(verbose_name='45-49 Tahun')
    k = models.IntegerField(verbose_name='50-54 Tahun')
    l = models.IntegerField(verbose_name='55-59 Tahun')
    m = models.IntegerField(verbose_name='60-64 Tahun')
    n = models.IntegerField(verbose_name='65-69 Tahun')
    o = models.IntegerField(verbose_name='70-74 Tahun')
    p = models.IntegerField(verbose_name='75+ Tahun')
    # total = models.IntegerField(editable=False, null=True)
    tanggal = models.DateField(null=True)

    def total(self):
        total = self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h + \
            self.i + self.j + self.k + self.l + self.m + \
            self.n + self.o + self.p
        return total

    def __str__(self):
        return str(self.tanggal)


class PendudukPr(models.Model):
    a = models.IntegerField(verbose_name='0-4 Tahun')
    b = models.IntegerField(verbose_name='5-9 Tahun')
    c = models.IntegerField(verbose_name='10-14 Tahun')
    d = models.IntegerField(verbose_name='15-19 Tahun')
    e = models.IntegerField(verbose_name='20-24 Tahun')
    f = models.IntegerField(verbose_name='25-29 Tahun')
    g = models.IntegerField(verbose_name='30-34 Tahun')
    h = models.IntegerField(verbose_name='35-39 Tahun')
    i = models.IntegerField(verbose_name='40-44 Tahun')
    j = models.IntegerField(verbose_name='45-49 Tahun')
    k = models.IntegerField(verbose_name='50-54 Tahun')
    l = models.IntegerField(verbose_name='55-59 Tahun')
    m = models.IntegerField(verbose_name='60-64 Tahun')
    n = models.IntegerField(verbose_name='65-69 Tahun')
    o = models.IntegerField(verbose_name='70-74 Tahun')
    p = models.IntegerField(verbose_name='75+ Tahun')
    # total = models.IntegerField(editable=False, null=True)
    tanggal = models.DateField(null=True)

    def total(self):
        total = self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h + \
            self.i + self.j + self.k + self.l + self.m + \
            self.n + self.o + self.p
        return total

    def __str__(self):
        return str(self.tanggal)


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
    a = models.IntegerField(verbose_name='0-4 Tahun')
    b = models.IntegerField(verbose_name='5-9 Tahun')
    c = models.IntegerField(verbose_name='10-14 Tahun')
    d = models.IntegerField(verbose_name='15-19 Tahun')
    e = models.IntegerField(verbose_name='20-24 Tahun')
    f = models.IntegerField(verbose_name='25-29 Tahun')
    g = models.IntegerField(verbose_name='30-34 Tahun')
    h = models.IntegerField(verbose_name='35-39 Tahun')
    i = models.IntegerField(verbose_name='40-44 Tahun')
    j = models.IntegerField(verbose_name='45-49 Tahun')
    k = models.IntegerField(verbose_name='50-54 Tahun')
    l = models.IntegerField(verbose_name='55-59 Tahun')
    m = models.IntegerField(verbose_name='60-64 Tahun')
    n = models.IntegerField(verbose_name='65-69 Tahun')
    o = models.IntegerField(verbose_name='70-74 Tahun')
    p = models.IntegerField(verbose_name='75+ Tahun')
    # total = models.IntegerField(editable=False, null=True)
    tanggal = models.DateField(null=True)

    def total(self):
        total = self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h + \
            self.i + self.j + self.k + self.l + self.m + \
            self.n + self.o + self.p
        return total

    def __str__(self):
        return str(self.tanggal)


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
    a = models.IntegerField(verbose_name='0-4 Tahun')
    b = models.IntegerField(verbose_name='5-9 Tahun')
    c = models.IntegerField(verbose_name='10-14 Tahun')
    d = models.IntegerField(verbose_name='15-19 Tahun')
    e = models.IntegerField(verbose_name='20-24 Tahun')
    f = models.IntegerField(verbose_name='25-29 Tahun')
    g = models.IntegerField(verbose_name='30-34 Tahun')
    h = models.IntegerField(verbose_name='35-39 Tahun')
    i = models.IntegerField(verbose_name='40-44 Tahun')
    j = models.IntegerField(verbose_name='45-49 Tahun')
    k = models.IntegerField(verbose_name='50-54 Tahun')
    l = models.IntegerField(verbose_name='55-59 Tahun')
    m = models.IntegerField(verbose_name='60-64 Tahun')
    n = models.IntegerField(verbose_name='65-69 Tahun')
    o = models.IntegerField(verbose_name='70-74 Tahun')
    p = models.IntegerField(verbose_name='75+ Tahun')
    # total = models.IntegerField(editable=False, null=True)
    tanggal = models.DateField(null=True)

    def total(self):
        total = self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h + \
            self.i + self.j + self.k + self.l + self.m + \
            self.n + self.o + self.p
        return total

    def __str__(self):
        return str(self.tanggal)


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
    total_pend = models.IntegerField(null=True)

    def total_pend(self):
        total = self.pend_lk + self.pend_pr
        return total

    def __str__(self):
        return str(self.tanggal)

    class Meta:
        verbose_name = "Kota"
        verbose_name_plural = "Kota"
