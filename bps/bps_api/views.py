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


class InflasiYoyApiViews(APIView):
    def get(self, *args, **kwargs):
        inflasi = Inflasi.objects.filter(kategori="Inflasi YoY")
        serializer = InflasiSerializers(inflasi, many=True)
        return Response({"Inflasi Year on Year: ": serializer.data}, status=status.HTTP_200_OK)


class InflasiDodApiViews(APIView):
    def get(self, *args, **kwargs):
        inflasi = Inflasi.objects.filter(kategori="Inflasi DoD")
        serializer = InflasiSerializers(inflasi, many=True)
        return Response({"Inflasi Date on Date: ": serializer.data}, status=status.HTTP_200_OK)


class PdrbApiViews(APIView):

    def get(self, request, *args, **kwargs):
        pdrb = Pdrb.objects.all()
        serializer = PdrbSerializers(pdrb, many=True)
        return Response({"PDRB": serializer.data}, status=status.HTTP_200_OK)


class PdrbMigasApiViews(APIView):
    def get(self, request, *args, **kwargs):
        pdrb = Pdrb.objects.filter(kategori='PDRB Migas')
        serializer = PdrbSerializers(pdrb, many=True)
        return Response({"PDRB": serializer.data}, status=status.HTTP_200_OK)


class DistPdrbMigasApiViews(APIView):
    def get(self, request, *args, **kwargs):
        pdrb = Pdrb.objects.filter(kategori='Distribusi PDRB Migas')
        serializer = PdrbSerializers(pdrb, many=True)
        return Response({"PDRB": serializer.data}, status=status.HTTP_200_OK)


class LajuPdrbMigasApiViews(APIView):
    def get(self, request, *args, **kwargs):
        pdrb = Pdrb.objects.filter(kategori='Laju Pertumbuhan PDRB Migas')
        serializer = PdrbSerializers(pdrb, many=True)
        return Response({"PDRB": serializer.data}, status=status.HTTP_200_OK)


class PdrbNonMigasApiViews(APIView):
    def get(self, request, *args, **kwargs):
        pdrb = Pdrb.objects.filter(kategori='PDRB Non Migas')
        serializer = PdrbSerializers(pdrb, many=True)
        return Response({"PDRB": serializer.data}, status=status.HTTP_200_OK)


class DistPdrbNonMigasApiViews(APIView):
    def get(self, request, *args, **kwargs):
        pdrb = Pdrb.objects.filter(kategori='Distribusi PDRB Non Migas')
        serializer = PdrbSerializers(pdrb, many=True)
        return Response({"PDRB": serializer.data}, status=status.HTTP_200_OK)


class LajuPdrbNonMigasApiViews(APIView):
    def get(self, request, *args, **kwargs):
        pdrb = Pdrb.objects.filter(kategori='Laju Pertumbuhan PDRB Non Migas')
        serializer = PdrbSerializers(pdrb, many=True)
        return Response({"PDRB": serializer.data}, status=status.HTTP_200_OK)


class KemiskinanApiViews(APIView):

    def get(self, request, *args, **kwargs):
        pdrb = Kemiskinan.objects.all()
        serializer = KemiskinanSerializers(pdrb, many=True)
        return Response({"PDRB": serializer.data}, status=status.HTTP_200_OK)


class TenagaKerjaApiViews(APIView):

    def get(self, request, *args, **kwargs):
        pdrb = TenagaKerja.objects.all()
        serializer = TenagaKerjaSerializers(pdrb, many=True)
        return Response({"PDRB": serializer.data}, status=status.HTTP_200_OK)


class IpmApiViews(APIView):

    def get(self, request, *args, **kwargs):
        pdrb = Ipm.objects.all()
        serializer = IpmSerializers(pdrb, many=True)
        return Response({"PDRB": serializer.data}, status=status.HTTP_200_OK)


class KotaApiViews(APIView):

    def get(self, request, *args, **kwargs):
        kota = Kota.objects.all()
        serializer = KotaSerializers(kota, many=True)
        return Response({"Kota": serializer.data}, status=status.HTTP_200_OK)
