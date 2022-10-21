from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from bps.models import *

# title name of admin page
admin.site.site_title = "BPS Admin"
admin.site.index_title = "BPS Admin"
admin.site.site_header = "BPS Admin"


"""
@admin.register(Kategori)
class KategoriModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Kategori
        fields = '__all__'
"""


@admin.register(Inflasi)
class InflasiModelAdmin(ImportExportModelAdmin):
    list_display = ("kategori", "tanggal")
    list_filter = ('kategori', 'tanggal')

    class Meta:
        model = Inflasi
        fields = '__all__'


@admin.register(Pdrb)
class PdrbModelAdmin(ImportExportModelAdmin):
    list_display = ("kategori", "tanggal")
    list_filter = ('kategori', 'tanggal')

    class Meta:
        model = Pdrb
        fields = '__all__'


@admin.register(Kemiskinan)
class KemiskinanModelAdmin(ImportExportModelAdmin):
    class Meta:
        model = Kemiskinan
        fields = '__all__'


@admin.register(TenagaKerja)
class TenagaKerjaModelAdmin(ImportExportModelAdmin):
    class Meta:
        model = TenagaKerja
        fields = '__all__'


@admin.register(Ipm)
class IpmModelAdmin(ImportExportModelAdmin):
    class Meta:
        model = Ipm
        fields = '__all__'


@admin.register(Penduduk)
class PendudukModelAdmin(ImportExportModelAdmin):
    list_display = ("tanggal", "jenis_kelamin")
    # list_filter = ('jenis_kelamin')

    class Meta:
        model = Penduduk
        fields = '__all__'


@admin.register(PendudukKecamatan)
class PendudukKecamatanModelAdmin(ImportExportModelAdmin):
    list_display = ("tanggal", "kec")
    # list_filter = ('kecamatan')

    class Meta:
        model = PendudukKecamatan
        fields = '__all__'


@admin.register(InflasiEnamKota)
class InflasiEnamKotaModelAdmin(ImportExportModelAdmin):
    list_display = ("nama_kota", "tanggal")
    list_filter = ('nama_kota', 'tanggal')

    class Meta:
        model = InflasiEnamKota
        fields = '__all__'


@admin.register(Ketimpangan)
class KetimpanganModelAdmin(ImportExportModelAdmin):
    class Meta:
        model = Ketimpangan
        fields = '__all__'
