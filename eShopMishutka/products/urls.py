from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^uslugi', views.uslugi),
    re_path(r'^usluga_klyauza', views.usluga_klyauza),
    re_path(r'^usluga_vzyat_izmorom', views.usluga_vzyat_izmorom),
    re_path(r'^usluga_predstavlenie', views.usluga_predstavlenie),
    re_path(r'^usluga_geroi_smi', views.usluga_geroi_smi),
]
