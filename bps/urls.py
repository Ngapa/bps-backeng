from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from bps.bps_api.views import *


urlpatterns = [
    path('inflasi/', InflasiApiViews.as_view()),
    path('inflasikeseluruhan/', InflasiKeseluruhanApiViews.as_view()),
    path('inflasiyoy/', InflasiYoyApiViews.as_view()),
    path('inflasidod/', InflasiDodApiViews.as_view()),
    path('pdrb/', PdrbApiViews.as_view()),
    path('pdrbmigas/', PdrbMigasApiViews.as_view()),
    path('distpdrbmigas/', DistPdrbMigasApiViews.as_view()),
    path('lajupdrbmigas/', LajuPdrbMigasApiViews.as_view()),
    path('pdrbnonmigas/', PdrbNonMigasApiViews.as_view()),
    path('distpdrbnonmigas/', DistPdrbNonMigasApiViews.as_view()),
    path('lajupdrbnonmigas/', LajuPdrbNonMigasApiViews.as_view()),
    path('kemiskinan/', KemiskinanApiViews.as_view()),
    path('tenagakerja/', TenagaKerjaApiViews.as_view()),
    path('ipm/', IpmApiViews.as_view()),
    path('kota/', KotaApiViews.as_view()),
    path('kategori/', KategoriViews.as_view()),
]
