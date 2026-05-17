# T7-Week12: Dashboard Visualisasi Data Penjualan Supermarket

## Identitas Mahasiswa
- **Nama:** Rifky Akbar Utomo Putra
- **NIM:** F1D02310149
- **Kelas:** D

## Deskripsi Singkat
Proyek ini adalah aplikasi *dashboard* desktop berbasis antarmuka grafis **PySide6**. Aplikasi ini bertugas mengolah dan memvisualisasikan data mentah penjualan supermarket menggunakan pustaka **Pandas** (untuk pemrosesan data tabular) dan **Matplotlib** (untuk pembuatan grafik interaktif). Proyek ini dibuat terstruktur dengan memisahkan modul antarmuka utama, *data loader*, dan *chart widget*.

## Informasi Dataset (Kaggle)
- **Sumber Dataset:** [Supermarket Sales Dataset (Kaggle)](https://www.kaggle.com/datasets/faresashraf1001/supermarket-sales)
- **Penjelasan Dataset:** Dataset ini berisi catatan transaksi historis dari perusahaan supermarket yang memiliki 3 cabang berbeda (Alex, Giza, Cairo) selama periode 3 bulan.
- **Makna Kolom Utama pada Dataset:**
  - `Invoice ID`: Nomor identifikasi unik untuk setiap struk/transaksi pembayaran.
  - `Branch`: Lokasi cabang supermarket tempat transaksi terjadi.
  - `City`: Kota tempat cabang supermarket tersebut berada.
  - `Customer type`: Kategori pelanggan (*Member* atau *Normal*).
  - `Product line`: Kategori barang/produk yang dibeli (misal: *Electronic accessories, Food and beverages, Health and beauty*).
  - `Unit price`: Harga satuan dari produk yang dibeli (dalam USD).
  - `Quantity`: Jumlah barang yang dibeli dalam satu transaksi tersebut.
  - `Sales`: Total harga/pendapatan kotor dari transaksi.
  - `Payment`: Metode pembayaran yang digunakan pelanggan (*Cash, Credit card, E-wallet*).

## Fitur Utama
1. **Tampilan Data Tabular:** Menampilkan sekumpulan data secara langsung di dalam antarmuka `QTableWidget` dengan desain responsif.
2. **Visualisasi Terintegrasi:** Menampilkan dua jenis grafik Matplotlib (Bar Chart & Pie Chart) yang menyatu langsung di dalam *window* PySide6 (tidak membuka *window* terpisah).
3. **Filter Interaktif:** Fitur penyaringan (*filtering*) data berdasarkan Cabang (*Branch*). Grafik, ringkasan angka, dan tabel otomatis diperbarui secara *real-time* saat filter diubah.
4. **Export Chart:** Tombol khusus untuk menyimpan visualisasi grafik Matplotlib ke dalam format file `.png`.

## Hasil Screenshot Aplikasi

**1. Tampilan Utama Dashboard (Menampilkan Data 'All')**
> Tampilan default saat aplikasi baru dibuka.
![Dashboard Utama](ss_utama.png)

**2. Fitur Filter Interaktif (Contoh: Menampilkan Cabang Cairo)**
> Grafik, tabel, dan total ringkasan otomatis berubah menyesuaikan data dari cabang Cairo saja.
![Filter Cabang](ss_filter.png)

**3. Fitur Export Chart ke PNG**
> Notifikasi keberhasilan saat menekan tombol Export.
![Export Sukses](ss_export.png)