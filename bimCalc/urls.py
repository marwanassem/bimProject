from django.urls import path
from bimCalc.views import *

urlpatterns = [
    path('', index, name='index'),
    path('bim/', bim_cal, name='bim_cal'),
]