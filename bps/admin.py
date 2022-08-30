from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from bps.models import *

# title name of admin page
admin.site.site_title = "BPS Admin"
admin.site.index_title = "BPS Admin"
admin.site.site_header = "BPS Admin"


@admin.register(Inflasi)
class InflasiModelAdmin(ImportExportModelAdmin):
    # list_display = ("tanggal", "kategori")
    # list_filter = ('kategori')

    class Meta:
        model = Inflasi
        fields = '__all__'


@admin.register(Pdrb)
class PdrbModelAdmin(ImportExportModelAdmin):
    # list_display = ("tanggal", "kategori")
    # list_filter = ('kategori')

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
    # list_display = ("tanggal", "jenis_kelamin")
    # list_filter = ('jenis_kelamin')

    class Meta:
        model = Penduduk
        fields = '__all__'


@admin.register(PendudukKecamatan)
class PendudukKecamatanModelAdmin(ImportExportModelAdmin):
    # list_display = ("tanggal", "kecamatan", "jenis_kelamin")
    # list_filter = ('kecamatan')

    class Meta:
        model = PendudukKecamatan
        fields = '__all__'


@admin.register(Kota)
class KotaModelAdmin(ImportExportModelAdmin):
    class Meta:
        model = Kota
        fields = '__all__'
