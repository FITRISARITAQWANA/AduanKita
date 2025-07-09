from django.contrib import admin
from .models import Aduan

# Konfigurasi tampilan model Aduan di halaman admin
class AduanAdmin(admin.ModelAdmin):
    list_display = ['nama', 'kategori', 'tanggal', 'status']  # kolom yang akan ditampilkan
    list_filter = ['kategori', 'status']                      # filter sidebar
    search_fields = ['nama', 'isi']                           # kolom pencarian

# Registrasi model ke admin
admin.site.register(Aduan, AduanAdmin)