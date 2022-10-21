from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from bps.bps_api.views import *


urlpatterns = [
    path('inflasi/', InflasiApiViews.as_view()),
    path('inflasikeseluruhan/', InflasiKeseluruhanApiViews.as_view()),
    path('inflasipengeluaran/', InflasiPengeluaranApiViews.as_view()),
    path('inflasiyoy/', InflasiYoyApiViews.as_view()),
    path('inflasidod/', InflasiDodApiViews.as_view()),
    path('pdrb/', PdrbApiViews.as_view()),
    path('distpdrb/', DistPdrbApiViews.as_view()),
    path('lajupdrb/', LajuPdrbApiViews.as_view()),
    path('kemiskinan/', KemiskinanApiViews.as_view()),
    path('tenagakerja/', TenagaKerjaApiViews.as_view()),
    path('ipm/', IpmApiViews.as_view()),
    path('inflasi_kota/', InflasiEnamKotaApiViews.as_view()),
    path('kategori/', KategoriViews.as_view()),
    path('ketimpangan/', KetimpanganViews.as_view()),
    path('penduduk/', PendudukViews.as_view()),
    path('pendudukkecamatan/', PendudukKecamatanViews.as_view()),
]
