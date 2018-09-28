Sentiment Analysis

Requirement :
- Python 2.7
- numpy
- sklearn
- nltk
- flask
- etc

Cara kerja :
- Jalankan menggunakan command line/terminal dengan mengetikkan "python app.py".
- Buka postman.
- Ganti method ke POST.
- Isikan alamat : localhost:8900/predict.
- Pada tab body isikan text pada kolom key dan teks yang akan di prediksi pada kolom value.
- Masih pada tab body tab body isikan model pada kolom key dan isikan 'forest' atau 'tree' pada kolom value
- Proses ini akan menampilkan hasil sentimen dan masing-masing bobotnya dalam bentuk json.

Hasil analisa :
- Akurasi Random Forest : 62.5 %
- Akurasi Decision Tree : 50 %
