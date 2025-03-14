# ⚙️ DJANGO 

## 💡 Deskripsi
Untuk project app yang saya buat adalah sama seperti di video yang terlampir, yaitu membuat app yang berisikan berita dan artikel yang masih bisa dikembangkan lagi kedepannya


## 🪄 Cara Menjalankan
1.Buka Command Prompt (CMD) 

2.Masuk ke Folder Tempat Proyek Akan Dibuat
```bash
cd nama_folder
```

3.Buat Virtual Environment
```bash
py -m venv .venv
```

4.Aktifkan Virtual Environment
```shell
.venv\Scripts\activate
```

5.Install Django
```bash
pip install django
```

6.Lalu untuk membuat Migrationnya
```bash
python manage.py makemigrations
```

7.Selanjutnya kita tinggal migrate dengan command
```bash
python manage.py migrate
```

8.Terakhir tinggal menjalankan projectnya
```bash
python manage.py runserver
```