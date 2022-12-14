from email.policy import default
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
    tpak = models.FloatField(null=True, blank=True)
    tkk = models.FloatField(null=True, blank=True)
    tpt = models.FloatField(null=True, blank=True)
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


class InflasiKlmpkPengeluaran(models.Model):
    sembako = models.FloatField(
        verbose_name="Makanan, Minuman, Tembakau", null=True, blank=True)
    sandang = models.FloatField(
        verbose_name="Pakaian dan Alas Kaki", null=True, blank=True)
    perumahan = models.FloatField(
        verbose_name="Perumahan, Air, Listrik, BB Lain", null=True, blank=True)
    perlengkapan = models.FloatField(
        verbose_name="Perlengkapan, Pemeliharaan Rutin Rumah Tangga", null=True, blank=True)
    kesehatan = models.FloatField(
        verbose_name="Kesehatan", null=True, blank=True)
    transportasi = models.FloatField(
        verbose_name="Transportasi", null=True, blank=True)
    informasi = models.FloatField(
        verbose_name="Informasi, Komunikasi, Keuangan", null=True, blank=True)
    rekreasi = models.FloatField(
        verbose_name="Rekreasi, Olahraga, Budaya", null=True, blank=True)
    pendidikan = models.FloatField(
        verbose_name="Pendidikan", null=True, blank=True)
    penyedia_pangan = models.FloatField(
        verbose_name="Penyedia Makanan Minuman / Restoran", null=True, blank=True)
    perawatan_pribadi = models.FloatField(
        verbose_name="Perawatan Pribadi, Jasa Lainnya", null=True, blank=True)
    total_inflasi = models.FloatField(
        verbose_name="Total Inflasi", null=True, blank=True)
    tanggal = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.tanggal)

    class Meta:
        verbose_name = "Inflasi Kelompok Pengeluaran"
        verbose_name_plural = "Inflasi Kelompok Pengeluaran"


class Inflasi(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, null=True)
    sembako = models.FloatField(
        verbose_name="Makanan, Minuman, Tembakau", null=True, blank=True)
    sandang = models.FloatField(
        verbose_name="Pakaian dan Alas Kaki", null=True, blank=True)
    perumahan = models.FloatField(
        verbose_name="Perumahan, Air, Listrik, BB Lain", null=True, blank=True)
    perlengkapan = models.FloatField(
        verbose_name="Perlengkapan, Pemeliharaan Rutin Rumah Tangga", null=True, blank=True)
    kesehatan = models.FloatField(
        verbose_name="Kesehatan", null=True, blank=True)
    transportasi = models.FloatField(
        verbose_name="Transportasi", null=True, blank=True)
    informasi = models.FloatField(
        verbose_name="Informasi, Komunikasi, Keuangan", null=True, blank=True)
    rekreasi = models.FloatField(
        verbose_name="Rekreasi, Olahraga, Budaya", null=True, blank=True)
    pendidikan = models.FloatField(
        verbose_name="Pendidikan", null=True, blank=True)
    penyedia_pangan = models.FloatField(
        verbose_name="Penyedia Makanan Minuman / Restoran", null=True, blank=True)
    perawatan_pribadi = models.FloatField(
        verbose_name="Perawatan Pribadi, Jasa Lainnya", null=True, blank=True)
    total_inflasi = models.FloatField(
        verbose_name="Total Inflasi", null=True, blank=True)
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
    kec = models.CharField(verbose_name='Kecamatan',
                           choices=KECAMATAN, max_length=35, default='Dayeuhluhur')
    lk = models.IntegerField(null=True, blank=True)
    pr = models.IntegerField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    rasio_jk = models.FloatField(null=True, blank=True)
    tanggal = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.tanggal)

    class Meta:
        verbose_name = "Penduduk Kecamatan"
        verbose_name_plural = "Penduduk Kecamatan"


class InflasiEnamKota (models.Model):
    KOTA = [
        ("cilacap", "Cilacap"),
        ("purwokerto", "Purwokerto"),
        ("kudus", "Kudus"),
        ("surakarta", "Surakarta"),
        ("semarang", "Semarang"),
        ("tegal", "Tegal"),
        ("nasional", "Nasional"),
    ]
    nama_kota = models.CharField(
        max_length=50, choices=KOTA, default="cilacap")
    mtom = models.FloatField(null=True, blank=True, verbose_name="M-to-M")
    ytod = models.FloatField(null=True, blank=True, verbose_name="Y-to-D")
    ytoy = models.FloatField(null=True, blank=True, verbose_name="Y-to-Y")
    tanggal = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.tanggal)

    class Meta:
        verbose_name = "Inflasi Enam Kota"
        verbose_name_plural = "Inflasi Enam Kota"


class Ketimpangan(models.Model):
    CHOICES = [
        ("rendah", "Rendah"),
        ("sedang", "Sedang"),
        ("tinggi", "Tinggi"),
    ]

    pddk = models.CharField(verbose_name="Penduduk",
                            choices=CHOICES, default="rendah", max_length=30)
    jumlah = models.FloatField(null=True, blank=True)
    tanggal = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.tanggal)

    class Meta:
        verbose_name_plural = "Ketimpangan"


class Pengangguran(models.Model):
    tanggal = models.DateField()
    tpak = models.FloatField(verbose_name="TPAK", null=True, blank=True)
    tpt = models.FloatField(verbose_name="TPT", null=True, blank=True)

    def __str__(self):
        return str(self.tanggal)

    class Meta:
        verbose_name_plural = "Pengangguran"
