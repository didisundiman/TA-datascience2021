# Deployment Model Random Forest Regression

## Deskripsi singkat

Repository ini berisi semua file yang dibutuhkan untuk melakukan deployment model Machine Learning dengan algoritma Random Forest Regression. Adapun model yang digunakan merupakan model untuk mengestimasi kinerja UMKM berdasarkan:

-   `KPL` atau Kapasitas kepemimpinan kewirausahaan berbasis pengetahuan pada UMKM.
-   `TPH` atau Tingkat penerapan dan integrasi teknologi dalam proses bisnis UMKM.
-   `AM` atau Kemampuan mekanisme adaptasi UMKM pada setiap perubahan di lingkungan bisnis.

#

## Sekilas mengenai input model

Agar dapat mengestimasi kinerja UMKM , data input model harus mengikuti format sebagai berikut:\
`[KPL, TPH, AM]`

Sebagai contoh:\
KPL: 60\
TPH: 78\
AM: 90\

Akan diubah menjadi:\
`[60, 78, 90]`

#

## Folder, file, dan kegunaannya

-   templates/
    -   index.html --> Berisi template website
-   app.py --> Berisi konfigurasi route untuk API
-   modelRFR.pkl --> Model Random Forest Regression yang sudah di-training
-   requirements.txt --> Berisi daftar dependency/package Python yang diperlukan untuk menjalankan API dan model Regresi Linier
