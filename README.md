AduanKita

AduanKita adalah sebuah aplikasi web berbasis Django yang memungkinkan masyarakat untuk menyampaikan berbagai bentuk pengaduan terkait pelayanan publik. Aplikasi ini dikembangkan dalam rangka tugas kuliah untuk mengimplementasikan algoritma pemrograman lanjutan melalui pengembangan website dinamis.


---

📌 Fitur Utama

Tambah aduan publik (dengan gambar opsional)

Daftar aduan yang disusun secara dinamis

Statistik aduan berdasarkan kategori/status

Riwayat aduan yang dikirim

Halaman Tentang Kami & Kontak



---

🧱 Struktur Folder Proyek

aduankita/
├── pengaduan/                # Aplikasi utama
│   ├── migrations/           # File migrasi database
│   ├── static/               # File CSS, JS, gambar statis
│   ├── templates/
│   │   └── pengaduan/        # Template HTML
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py              # Form input pengguna
│   ├── models.py             # Struktur database
│   ├── urls.py
│   └── views.py              # Logika utama aplikasi
├── aduankita/                # Konfigurasi proyek Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3                # Database lokal
└── manage.py


---

⚙️ Cara Instalasi dan Menjalankan Aplikasi

1. Clone repository:



git clone https://github.com/username/aduankita.git
cd aduankita

2. Aktifkan virtual environment (opsional tapi disarankan):



python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. Install dependensi:



pip install -r requirements.txt

4. Jalankan migrasi database:



python manage.py migrate

5. Jalankan server lokal:



python manage.py runserver

6. Akses aplikasi di browser:



http://127.0.0.1:8000/


---

🔄 Alur & Logika Aplikasi

Data aduan disimpan di database SQLite

User dapat mengisi form aduan, memilih kategori, dan mengunggah gambar

Data dikirim melalui POST dan diproses oleh views.py

Template HTML menggunakan Bootstrap 5 dan animasi (animate.css)

Gambar disimpan di folder media/

Statistik dihitung berdasarkan query set ke model Aduan



---

📷 Tampilan Antarmuka

Tampilan sederhana dan profesional menggunakan Bootstrap:

Navbar responsif

Form input terstruktur

Tabel daftar aduan dengan badge status

Pagination dan filter kategori



---

👤 Pengembang

Nama: Fitri Sari Taqwana

Universitas: Hamzanwadi

Mata Kuliah: Algoritma Pemrograman Lanjutan



---

🔗 Link Penting

📂 GitHub Repo: https://github.com/fitrisaritaqwana/aduankita

🌐 Demo Website (jika tersedia): https://aduankita-demo.vercel.app



---

> "Aduan Anda, Aspirasi Kami!" — AduanKita Team



