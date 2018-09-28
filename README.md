Sentiment Analysis

Requirement :
- Python 2.7
- numpy
- sklearn
- nltk
- flask
- etc

Cara kerja API:
- Jalankan menggunakan command line/terminal dengan mengetikkan "python app.py".
- Buka postman.
- Ganti method ke POST.
- Isikan alamat : localhost:8900/predict.
- Pada tab body isikan text pada kolom key dan teks yang akan di prediksi pada kolom value.
- Masih pada tab body tab body isikan model pada kolom key dan isikan 'forest' atau 'tree' pada kolom value
- Proses ini akan menampilkan hasil sentimen dan masing-masing bobotnya dalam bentuk json.

Cara kerja Jupyter :
- buka file .ipynb melalui google colab
- buat folder dataset pada direktori google drive
- upload pos.txt dan neg.txt ke folder tersebut
- data akan di gabungkan semuanya dan diberi label
- kemudian di split dengan ratio 80:20
- setelah itu akan dilakukan preprocesing : lowering, remove punctuation, tokenize, stopword removal dan stemming
- setelahnya akan dihitung tf-idf nya dan menghasilkan fitur yang akan digunakan untuk proses training
- proses training akan menghasilkan model, akurasi dan confusion matrix
- model akan disimpan dalam file .pkl

Hasil analisa :
- Akurasi Random Forest : 62 %
- Akurasi Decision Tree : 50 %
- Akurasi Random forest lebih tinggi karena jumlah tree yang lebih banyak dan tiap pembuatan tree dilakukan dengan data yang dipilih secara random. Hasil dari decision tree akan dijadikan candidate untuk dilakukan majority vote dalam menentukan hasil akhir prediksi.
- Untuk meningkatkan akurasi bisa dilakukan dengan melakukan optimasi fitur atau dengan seleksi fitur
