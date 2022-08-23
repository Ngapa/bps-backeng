from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from bps.models import *

# title name of admin page
admin.site.site_title = "BPS Admin"
admin.site.index_title = "BPS Admin"
admin.site.site_header = "BPS Admin"


@admin.register(Inflasi)
class InflasiModelAdmin(ImportExportModelAdmin):
    class Meta:
        model = Inflasi
        fields = '__all__'


@admin.register(InflasiDod)
class InflasiDodModelAdmin(ImportExportModelAdmin):
    class Meta:
        model = InflasiDod
        fields = '__all__'


@admin.register(InflasiYoy)
class InflasiYoyModelAdmin(ImportExportModelAdmin):
    class Meta:
        model = InflasiYoy
        fields = '__all__'


@admin.register(PdrbMigas)
class PdrbMigasModelAdmin(ImportExportModelAdmin):
    class Meta:
        model = PdrbMigas
        fields = '__all__'


@admin.register(DistribusiPdrbMigas)
class DistribusiPdrbMigasModelAdmin(ImportExportModelAdmin):
    class Meta:
        model = DistribusiPdrbMigas
        fields = '__all__'


@admin.register(LajuPertumbuhanPdrbMigas)
class LajuPertumbuhanPdrbMigasModelAdmin(ImportExportModelAdmin):
    class Meta:
        model = LajuPertumbuhanPdrbMigas
        fields = '__all__'


@admin.register(SumberPertumbuhanPdrbMigas)
class SumberPertumbuhanPdrbMigasModelAdmin(ImportExportModelAdmin):
    class Meta:
        model = SumberPertumbuhanPdrbMigas
        fields = '__all__'


@admin.register(PdrbNonMigas)
class PdrbNonMigasModelAdmin(ImportExportModelAdmin):
    class Meta:
        model = PdrbNonMigas
        fields = '__all__'


@admin.register(DistribusiPdrbNonMigas)
class DistribusiPdrbNonMigasModelAdmin(ImportExportModelAdmin):
    class Meta:
        model = DistribusiPdrbNonMigas
        fields = '__all__'


@admin.register(LajuPertumbuhanPdrbNonMigas)
class LajuPertumbuhanPdrbNonMigasModelAdmin(ImportExportModelAdmin):
    class Meta:
        model = LajuPertumbuhanPdrbNonMigas
        fields = '__all__'


@admin.register(SumberPertumbuhanPdrbNonMigas)
class SumberPertumbuhanPdrbNonMigasModelAdmin(ImportExportModelAdmin):
    class Meta:
        model = SumberPertumbuhanPdrbNonMigas
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


@admin.register(Kota)
class KotaModelAdmin(ImportExportModelAdmin):
    class Meta:
        model = Kota
        fields = '__all__'
