from rest_framework import serializers
from bps.models import *


class InflasiSerializers(serializers.ModelSerializer):
    class Meta:
        model = Inflasi
        fields = '__all__'


class PdrbSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pdrb
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
        

class KategoriSerializers(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'


class KotaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Kota
        fields = '__all__'
