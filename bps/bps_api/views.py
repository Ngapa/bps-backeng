from django.http import HttpResponse
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


class InflasiDodApiViews(APIView):

    def get(self, request, *args, **kwargs):
        inflasi = Inflasi.objects.all()
        serializer = InflasiSerializers(inflasi, many=True)
        return Response({"Inflasi": serializer.data}, status=status.HTTP_200_OK)


class InflasiYoyApiViews(APIView):

    def get(self, request, *args, **kwargs):
        inflasi = Inflasi.objects.all()
        serializer = InflasiSerializers(inflasi, many=True)
        return Response({"Inflasi": serializer.data}, status=status.HTTP_200_OK)


class PdrbMigasApiViews(APIView):

    def get(self, request, *args, **kwargs):
        pdrb = PdrbMigas.objects.all()
        serializer = PdrbMigasSerializers(pdrb, many=True)
        return Response({"PDRB": serializer.data}, status=status.HTTP_200_OK)


class DistPdrbMigasApiViews(APIView):

    def get(self, request, *args, **kwargs):
        pdrb = DistribusiPdrbMigas.objects.all()
        serializer = DistPdrbMigasSerializers(pdrb, many=True)
        return Response({"PDRB": serializer.data}, status=status.HTTP_200_OK)


class LajuPertPdrbMigasApiViews(APIView):

    def get(self, request, *args, **kwargs):
        pdrb = LajuPertumbuhanPdrbMigas.objects.all()
        serializer = LajuPertPdrbMigasSerializers(pdrb, many=True)
        return Response({"PDRB": serializer.data}, status=status.HTTP_200_OK)


class SumbPertPdrbMigasApiViews(APIView):

    def get(self, request, *args, **kwargs):
        pdrb = LajuPertumbuhanPdrbMigas.objects.all()
        serializer = SumbPertPdrbMigasSerializers(pdrb, many=True)
        return Response({"PDRB": serializer.data}, status=status.HTTP_200_OK)


class PdrbNonMigasApiViews(APIView):

    def get(self, request, *args, **kwargs):
        pdrb = PdrbNonMigas.objects.all()
        serializer = PdrbNonMigasSerializers(pdrb, many=True)
        return Response({"PDRB": serializer.data}, status=status.HTTP_200_OK)


class DistPdrbNonMigasApiViews(APIView):

    def get(self, request, *args, **kwargs):
        pdrb = DistribusiPdrbNonMigas.objects.all()
        serializer = DistPdrbNonMigasSerializers(pdrb, many=True)
        return Response({"PDRB": serializer.data}, status=status.HTTP_200_OK)


class LajuPertPdrbNonMigasApiViews(APIView):

    def get(self, request, *args, **kwargs):
        pdrb = LajuPertumbuhanPdrbNonMigas.objects.all()
        serializer = LajuPertPdrbNonMigasSerializers(pdrb, many=True)
        return Response({"PDRB": serializer.data}, status=status.HTTP_200_OK)


class SumbPertPdrbNonMigasApiViews(APIView):

    def get(self, request, *args, **kwargs):
        pdrb = LajuPertumbuhanPdrbNonMigas.objects.all()
        serializer = SumbPertPdrbNonMigasSerializers(pdrb, many=True)
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
