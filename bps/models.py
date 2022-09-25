from django.db import models
# Create your models here.


class Kategori(models.Model):
    nama = models.CharField(
        max_length=100, verbose_name="Nama", null=True, blank=True)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = "Kategori"


class Pdrb(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, null=True)
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
    total_pdrb = models.FloatField(
        verbose_name="Total", null=True, blank=True)
    tanggal = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.tanggal)

    class Meta:
        verbose_name = "Produk Domestik Regional Bruto"
        verbose_name_plural = "Produk Domestik Regional Bruto"


class TenagaKerja(models.Model):
    CHOICES = [
        ("LK", "Laki-Laki"),
        ("PR", "Perempuan")
    ]
    angkatan_kerja = models.FloatField(null=True, blank=True)
    bekerja = models.FloatField(null=True, blank=True)
    pengangguran = models.FloatField(null=True, blank=True)
    bkn_angkatan_kerja = models.FloatField(null=True, blank=True)
    sekolah = models.FloatField(null=True, blank=True)
    urur_ruta = models.FloatField(null=True, blank=True)
    lainnya = models.FloatField(null=True, blank=True)
    gender = models.CharField(max_length=15, choices=CHOICES)
    tanggal = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.tanggal)

    class Meta:
        verbose_name = "Ketenagakerjaan"
        verbose_name_plural = "Ketenagakerjaan"


class Kemiskinan(models.Model):
    ppdk_mskn = models.FloatField(null=True, blank=True)
    p0 = models.FloatField(null=True, blank=True)
    p1 = models.FloatField(null=True, blank=True)
    p2 = models.FloatField(null=True, blank=True)
    gk = models.FloatField(null=True, blank=True)
    tanggal = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.tanggal)

    class Meta:
        verbose_name = "Kemiskinan"
        verbose_name_plural = "Kemiskinan"


class Ipm(models.Model):
    uhh = models.FloatField(null=True, blank=True)
    rls = models.FloatField(null=True, blank=True)
    hls = models.FloatField(null=True, blank=True)
    ppp = models.FloatField(null=True, blank=True)
    ipm = models.FloatField(null=True, blank=True)
    pertumbuhan = models.FloatField(null=True, blank=True)
    tanggal = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.tanggal)

    class Meta:
        verbose_name = "Indeks Pembangunan Manusia"
        verbose_name_plural = "Indeks Pembangunan Manusia"


class Inflasi(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, null=True)
    sembako = models.FloatField(null=True, blank=True)
    sandang = models.FloatField(null=True, blank=True)
    perumahan = models.FloatField(null=True, blank=True)
    perlengkapan = models.FloatField(null=True, blank=True)
    kesehatan = models.FloatField(null=True, blank=True)
    transportasi = models.FloatField(null=True, blank=True)
    informasi = models.FloatField(null=True, blank=True)
    rekreasi = models.FloatField(null=True, blank=True)
    pendidikan = models.FloatField(null=True, blank=True)
    penyedia_pangan = models.FloatField(null=True, blank=True)
    perawatan_pribadi = models.FloatField(null=True, blank=True)
    total_inflasi = models.FloatField(null=True, blank=True)
    tanggal = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.tanggal)

    class Meta:
        verbose_name = "Inflasi"
        verbose_name_plural = "Inflasi"


class Penduduk(models.Model):
    CHOICES = [
        ("LK", "Laki-Laki"),
        ("PR", "Perempuan")
    ]
    jenis_kelamin = models.CharField(max_length=15, choices=CHOICES)
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
    total = models.IntegerField(null=True, blank=True)
    tanggal = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.tanggal)

    class Meta:
        verbose_name = "Penduduk"
        verbose_name_plural = "Penduduk"


class PendudukKecamatan(models.Model):
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
    CHOICES = [
        ("LK", "Laki-Laki"),
        ("PR", "Perempuan")
    ]
    kec = models.CharField(verbose_name='Kecamatan',
                           choices=KECAMATAN, max_length=35, default='Dayeuhluhur')
    jenis_kelamin = models.CharField(max_length=15, choices=CHOICES)
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
    total = models.IntegerField(null=True, blank=True)
    tanggal = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.tanggal)

    class Meta:
        verbose_name = "Penduduk Kecamatan"
        verbose_name_plural = "Penduduk Kecamatan"


class Kota (models.Model):
    nama_kota = models.CharField(max_length=50)
    inflasi = models.ForeignKey(
        Inflasi, related_name='inflasi_kota', on_delete=models.CASCADE)
    pdrb_migas = models.ForeignKey(
        Pdrb, related_name='pdrb_kota', on_delete=models.CASCADE)
    pend = models.ForeignKey(
        Penduduk, related_name="penduduk_kota", on_delete=models.CASCADE)
    pend_kec = models.ForeignKey(
        PendudukKecamatan, related_name="penduduk_kecamatan", on_delete=models.CASCADE)
    tanggal = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.tanggal)

    class Meta:
        verbose_name = "Kota"
        verbose_name_plural = "Kota"
