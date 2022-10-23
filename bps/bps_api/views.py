from os import stat
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from bps.models import *
from bps.bps_api.serializer import *


class InflasiApiViews(APIView):

    def get(self, request, *args, **kwargs):
        inflasi = Inflasi.objects.all()
        serializer = InflasiSerializers(inflasi, many=True)
        return Response({"Inflasi": serializer.data}, status=status.HTTP_200_OK)


class InflasiKeseluruhanApiViews(APIView):
    def get(self, request, *args, **kwargs):
        inflasi = Inflasi.objects.filter(kategori="1")
        serializer = InflasiSerializers(inflasi, many=True)
        return Response({"Inflasi": serializer.data}, status=status.HTTP_200_OK)


class InflasiYoyApiViews(APIView):
    def get(self, *args, **kwargs):
        inflasi = Inflasi.objects.filter(kategori="2")
        serializer = InflasiSerializers(inflasi, many=True)
        return Response({"Inflasi Year on Year: ": serializer.data}, status=status.HTTP_200_OK)


class InflasiDodApiViews(APIView):
    def get(self, *args, **kwargs):
        inflasi = Inflasi.objects.filter(kategori="3")
        serializer = InflasiSerializers(inflasi, many=True)
        return Response({"Inflasi Date on Date: ": serializer.data}, status=status.HTTP_200_OK)


class InflasiPengeluaranApiViews(APIView):
    def get(self, *args, **kwargs):
        inflasi = InflasiKlmpkPengeluaran.objects.filter(kategori="2")
        serializer = InflasiPengeluaranSerializers(inflasi, many=True)
        return Response({"Inflasi: ": serializer.data}, status=status.HTTP_200_OK)


class PdrbApiViews(APIView):

    def get(self, request, *args, **kwargs):
        pdrb = Pdrb.objects.filter(
            kategori='4') | Pdrb.objects.filter(kategori='7')
        serializer = PdrbSerializers(pdrb, many=True)
        return Response({"PDRB": serializer.data}, status=status.HTTP_200_OK)


class DistPdrbApiViews(APIView):
    def get(self, request, *args, **kwargs):
        pdrb = Pdrb.objects.filter(
            kategori='5') | Pdrb.objects.filter(kategori='8')
        serializer = PdrbSerializers(pdrb, many=True)
        return Response({"PDRB": serializer.data}, status=status.HTTP_200_OK)


class LajuPdrbApiViews(APIView):
    def get(self, request, *args, **kwargs):
        pdrb = Pdrb.objects.filter(
            kategori='6') | Pdrb.objects.filter(kategori='7')
        serializer = PdrbSerializers(pdrb, many=True)
        return Response({"PDRB": serializer.data}, status=status.HTTP_200_OK)


class KemiskinanApiViews(APIView):

    def get(self, request, *args, **kwargs):
        pdrb = Kemiskinan.objects.all()
        serializer = KemiskinanSerializers(pdrb, many=True)
        return Response({"Kemiskinan": serializer.data}, status=status.HTTP_200_OK)


class TenagaKerjaApiViews(APIView):

    def get(self, request, *args, **kwargs):
        pdrb = TenagaKerja.objects.all()
        serializer = TenagaKerjaSerializers(pdrb, many=True)
        return Response({"Tenaga Kerja": serializer.data}, status=status.HTTP_200_OK)


class IpmApiViews(APIView):

    def get(self, request, *args, **kwargs):
        pdrb = Ipm.objects.all()
        serializer = IpmSerializers(pdrb, many=True)
        return Response({"IPM": serializer.data}, status=status.HTTP_200_OK)


class InflasiEnamKotaApiViews(APIView):
    def get(self, request, *args, **kwargs):
        inflasi = InflasiEnamKota.objects.all()
        serializer = InflasiEnamKotaSerializers(inflasi, many=True)
        return Response({"Inflasi": serializer.data}, status=status.HTTP_200_OK)


class KategoriViews(APIView):
    def get(self, request, *args, **kwargs):
        kategori = Kategori.objects.all()
        serializer = KategoriSerializers(kategori, many=True)
        return Response({'Kategori': serializer.data}, status=status.HTTP_200_OK)


class KetimpanganViews(APIView):
    def get(self, request, *args, **kwargs):
        ketimpangan = Ketimpangan.objects.all()
        serializer = KetimpanganSerializers(ketimpangan, many=True)
        return Response({'Ketimpangan': serializer.data}, status=status.HTTP_200_OK)


class PengangguranViews(APIView):
    def get(self, request, *args, **kwargs):
        pengangguran = Pengangguran.objects.all()
        serializer = PengangguranSerializers(pengangguran, many=True)
        return Response({'Ketimpangan': serializer.data}, status=status.HTTP_200_OK)


class PendudukViews(APIView):
    def get(self, request, *args, **kwargs):
        penduduk = Penduduk.objects.all()
        serializer = PendudukSerializers(penduduk, many=True)
        return Response({'Penduduk': serializer.data}, status=status.HTTP_200_OK)


class PendudukKecamatanViews(APIView):
    def get(self, request, *args, **kwargs):
        penduduk = PendudukKecamatan.objects.all()
        serializer = PendudukKecamatanSerializers(penduduk, many=True)
        return Response({'Penduduk': serializer.data}, status=status.HTTP_200_OK)
