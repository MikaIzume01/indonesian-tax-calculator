# Kalkulator Pajak Indonesia (PPh 21 TER & PPN 2026)

Aplikasi web interaktif berbasis Python Flask untuk membantu perhitungan perpajakan di Indonesia sesuai dengan ketentuan dan regulasi terbaru tahun **2026**.

## 🚀 Fitur Utama
1. **Kalkulator PPh Pasal 21 (TER - Tarif Efektif Rata-Rata):**
   - Mengacu pada **PP No. 58 Tahun 2023** & **PMK No. 168 Tahun 2023**.
   - Matriks lengkap Kategori A (TK/0, TK/1, K/0), Kategori B (TK/2, TK/3, K/1, K/2), dan Kategori C (K/3).
   - Penanganan edge case komprehensif: Pegawai Tetap, Pegawai Tidak Tetap / Freelance (DPP 50%), dan PPh Final Pesangon (PP 68/2009).
   - Akumulasi Tunjangan, Bonus, serta Natura / Kenikmatan (Fasilitas Kantor).

2. **Kalkulator Rekonsiliasi SPT Masa PPN (12%):**
   - Menyesuaikan tarif PPN **12%** sesuai amanat UU Harmonisasi Peraturan Perpajakan (UU HPP) dan PMK No. 131 Tahun 2024.
   - Rekonsiliasi otomatis antara DPP Penjualan (Keluaran) dan DPP Pembelian (Masukan) untuk menentukan posisi Kurang Bayar, Lebih Bayar, atau Nihil.

3. **Panduan Pengguna Interaktif:**
   - Dilengkapi kotak panduan dan petunjuk pengisian di setiap halaman modul untuk memudahkan auditor atau praktisi akuntansi pemula.

## 🛠️ Teknologi yang Digunakan
- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3 (Modern Flexbox/Grid, Responsive Layout, Custom UI/UX)
- **Database / State Management:** Local session & calculation handler

## ⚙️ Cara Menjalankan Aplikasi
1. Pastikan Python sudah terinstal di komputer Anda.
2. Install dependensi yang diperlukan:
   ```bash
   pip install flask pandas openpyxl
   ```
3. Jalankan aplikasi:
   ```bash
   python tax_calculator_app/app.py
   ```
4. Buka browser dan akses: `http://127.0.0.1:5002`
