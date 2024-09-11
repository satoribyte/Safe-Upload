SafeUpload

SafeUpload adalah aplikasi web keren yang bikin upload file jadi gampang dan aman. Pake Dropzone.js buat manage file upload, plus ada filter buat nahan file-file yang bisa bikin server bermasalah.

Fitur Keren

- Upload Otomatis: File langsung keupload begitu loe seret atau pilih file.
- Filter File: Nolak file yang bisa berbahaya kayak .exe, .sh, .php, dan lain-lain.
- Desain Kekinian: Tampilan yang kece pake Tailwind CSS, cocok buat semua perangkat.
- Keamanan: Nahan file yang sering dipake buat nyerang.

Cara Instal

Untuk Windows, macOS, dan Linux

1. Kloning Repositori

   git clone https://github.com/satoribyte/Safe-Upload.git

2. Masuk ke Folder Proyek

   cd safeupload

3. Instalasi Dependensi

   Pastikan loe udah punya Python dan pip. Install Flask dengan:

   pip install Flask

4. Jalankan Aplikasi

   Start aplikasi dengan:

   python app.py

   Akses di http://localhost:6446.

Untuk Termux (Android)

1. Install Termux

   Download dan install Termux dari Google Play Store atau F-Droid.

2. Install Python dan Git di Termux

   Buka Termux dan ketik:

   pkg update
   pkg upgrade
   pkg install python git

3. Kloning Repositori

   git clone https://github.com/satoribyte/Safe-Upload.git

4. Masuk ke Folder Proyek

   cd safeupload

5. Instalasi Dependensi

   pip install Flask

6. Jalankan Aplikasi

   Start aplikasi dengan:

   python app.py

   Akses di http://localhost:6446.

Cara Pakai

1. Buka aplikasi di browser (misalnya, http://localhost:6446).
2. Seret file ke area Dropzone atau klik buat pilih file.
3. File bakal diupload otomatis, dan loe tetap di halaman yang sama.

Keuntungan

- Keamanan: Nahan file yang bisa ngerusak server.
- Mudah Dipakai: Tampilan yang user-friendly dan responsive.
- Otomatis: File diupload otomatis tanpa ribet.
- Desain Responsive: Tampilan bagus di semua ukuran layar.

Kelemahan

- Gak Ada Fitur Pembatalan: Sekali file ditambahkan, gak bisa dibatalin.
- Keamanan File Terbatas: Filtrasi cuma berdasarkan ekstensi; mungkin perlu pemindaian lebih lanjut.
- Penanganan Kesalahan Terbatas: Penanganan kesalahan masih basic; butuh perbaikan untuk pengalaman yang lebih oke.

Kontribusi

Mau bantu proyek ini?

1. Fork repositori ini.
2. Buat branch baru (git checkout -b feature-branch).
3. Lakukan perubahan dan commit (git commit -am 'Add new feature').
4. Push ke branch (git push origin feature-branch).
5. Buat pull request.

Lisensi

Proyek ini dilisensikan di bawah MIT License - cek file LICENSE buat info lebih lanjut.

Kontak

Ada pertanyaan atau butuh bantuan? Hubungi di satoribyte@gmail.com.
