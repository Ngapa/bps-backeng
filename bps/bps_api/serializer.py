from rest_framework import serializers
from bps.models import *


class InflasiSerializers(serializers.ModelSerializer):
    class Meta:
        model = Inflasi
        fields = '__all__'


class InflasiDodSerializers(serializers.ModelSerializer):
    class Meta:
        model = InflasiDod
        fields = '__all__'


class InflasiYoySerializers:
    model = InflasiYoy
    fields = '__all__'


class PdrbMigasSerializers(serializers.ModelSerializer):
    class Meta:
        model = PdrbMigas
        fields = '__all__'


class DistPdrbMigasSerializers(serializers.ModelSerializer):
    class Meta:
        model = DistribusiPdrbMigas
        fields = '__all__'


class LajuPertPdrbMigasSerializers(serializers.ModelSerializer):
    class Meta:
        model = LajuPertumbuhanPdrbMigas
        fields = '__all__'


class SumbPertPdrbMigasSerializers(serializers.ModelSerializer):
    class Meta:
        model = SumberPertumbuhanPdrbMigas
        fields = '__all__'


class PdrbNonMigasSerializers(serializers.ModelSerializer):
    class Meta:
        model = PdrbNonMigas
        fields = '__all__'


class DistPdrbNonMigasSerializers(serializers.ModelSerializer):
    class Meta:
        model = DistribusiPdrbNonMigas
        fields = '__all__'


class LajuPertPdrbNonMigasSerializers(serializers.ModelSerializer):
    class Meta:
        model = LajuPertumbuhanPdrbNonMigas
        fields = '__all__'


class SumbPertPdrbNonMigasSerializers(serializers.ModelSerializer):
    class Meta:
        model = SumberPertumbuhanPdrbMigas
        fields = '__all__'


class TenagaKerjaSerializers(serializers.ModelSerializer):
    class Meta:
        model = TenagaKerja
        fields = '__all__'


class KemiskinanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Kemiskinan
        fields = '__all__'


class IpmSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ipm
        fields = '__all__'


class KotaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Kota
        fields = '__all__'
