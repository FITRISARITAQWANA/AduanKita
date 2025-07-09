from django.db import models

class Aduan(models.Model):
    KATEGORI_CHOICES = [
        ('infrastruktur', 'Infrastruktur'),
        ('pelayanan', 'Pelayanan'),
        ('lingkungan', 'Lingkungan'),
        ('keamanan', 'Keamanan'),
        ('lainnya', 'Lainnya'),
    ]

    STATUS_CHOICES = [
        ('baru', 'Baru'),
        ('diproses', 'Diproses'),
        ('selesai', 'Selesai'),
    ]

    nama = models.CharField(max_length=100)
    kategori = models.CharField(max_length=50, choices=KATEGORI_CHOICES)
    isi = models.TextField()
    tanggal = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='baru')
    gambar = models.ImageField(upload_to='aduan_images/', blank=True, null=True)  # ✅ Ini yang benar

    def __str__(self):
        return self.nama