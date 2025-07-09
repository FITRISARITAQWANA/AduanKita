from django.shortcuts import render, redirect
from django.db.models import Count
from django.core.paginator import Paginator
from .models import Aduan
from .forms import AduanForm

# Halaman Beranda
def beranda(request):
    total_aduan = Aduan.objects.count()
    jumlah_per_kategori = (
        Aduan.objects.values('kategori')
        .annotate(jumlah=Count('id'))
        .order_by('-jumlah')
    )
    tips = {
        "Jaga Kebersihan": "Buang sampah pada tempatnya.",
        "Laporkan Masalah": "Sampaikan aduan Anda lewat website ini.",
        "Gunakan Fasilitas Umum dengan Bijak": "Rawat fasilitas agar bisa dinikmati bersama."
    }
    return render(request, 'pengaduan/beranda.html', {
        'total_aduan': total_aduan,
        'jumlah_per_kategori': jumlah_per_kategori,
        'tips': tips
    })

# Halaman Daftar Aduan
def daftar_aduan(request):
    kategori_filter = request.GET.get('kategori')
    aduan_list = Aduan.objects.all().order_by('-tanggal')

    if kategori_filter:
        aduan_list = aduan_list.filter(kategori=kategori_filter)

    paginator = Paginator(aduan_list, 5)  # 5 aduan per halaman
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    kategori_list = Aduan.KATEGORI_CHOICES
    return render(request, 'pengaduan/daftar_aduan.html', {
        'page_obj': page_obj,
        'kategori_filter': kategori_filter,
        'kategori_list': kategori_list
    })

# Halaman Tambah Aduan
def tambah_aduan(request):
    if request.method == 'POST':
        form = AduanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('daftar_aduan')
    else:
        form = AduanForm()
    return render(request, 'pengaduan/tambah_aduan.html', {'form': form})

# Halaman Statistik Aduan
def statistik_aduan(request):
    data = (
        Aduan.objects.values('kategori')
        .annotate(jumlah=Count('id'))
        .order_by('-jumlah')
    )
    return render(request, 'pengaduan/statistik.html', {'data': data})

# Halaman Riwayat Pengaduan
def riwayat_aduan(request):
    aduan = Aduan.objects.all().order_by('-tanggal')  # bisa difilter berdasarkan user nanti
    return render(request, 'pengaduan/riwayat.html', {'aduan': aduan})

# Halaman Tentang Kami
def tentang_kami(request):
    return render(request, 'pengaduan/tentang_kami.html')

# Halaman Kontak
def kontak(request):
    return render(request, 'pengaduan/kontak.html')