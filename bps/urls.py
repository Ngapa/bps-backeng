from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from bps.bps_api.views import *


urlpatterns = [
    path('inflasi/', InflasiApiViews.as_view()),
    path('inflasi_dod/', InflasiDodApiViews.as_view()),
    path('inflasi_yoy/', InflasiYoyApiViews.as_view()),
    path('pdrb_migas/', PdrbMigasApiViews.as_view()),
    path('dist_pdrb_migas/', DistPdrbMigasApiViews.as_view()),
    path('laju_pert_pdrb_migas/', LajuPertPdrbMigasApiViews.as_view()),
    path('sumb_pert_pdrb_migas/', SumbPertPdrbMigasApiViews.as_view()),
    path('pdrb_non_migas/', PdrbNonMigasApiViews.as_view()),
    path('dist_pdrb_non_migas/', DistPdrbNonMigasApiViews.as_view()),
    path('laju_pert_pdrb_non_migas/', LajuPertPdrbNonMigasApiViews.as_view()),
    path('sumb_pert_pdrb_non_migas/', SumbPertPdrbNonMigasApiViews.as_view()),
    path('kemiskinan/', KemiskinanApiViews.as_view()),
    path('tenagakerja/', TenagaKerjaApiViews.as_view()),
    path('ipm/', IpmApiViews.as_view()),
    path('kota/', KotaApiViews.as_view()),
]
