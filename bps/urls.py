from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from bps.bps_api.views import *


urlpatterns = [
    path('inflasi/', InflasiApiViews.as_view()),
    path('pdrb/', PdrbApiViews.as_view()),
    path('kemiskinan/', KemiskinanApiViews.as_view()),
    path('tenagakerja/', TenagaKerjaApiViews.as_view()),
    path('ipm/', IpmApiViews.as_view()),
    path('kota/', KotaApiViews.as_view()),
]
