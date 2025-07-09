from django.urls import path
from . import views

urlpatterns = [
    path('', views.beranda, name='beranda'),
    path('aduan/', views.daftar_aduan, name='daftar_aduan'),
    path('aduan/tambah/', views.tambah_aduan, name='tambah_aduan'),
    path('statistik/', views.statistik_aduan, name='statistik'),
    path('riwayat/', views.riwayat_aduan, name='riwayat_aduan'),
    path('tentang/', views.tentang_kami, name='tentang_kami'),
    path('kontak/', views.kontak, name='kontak'),
]