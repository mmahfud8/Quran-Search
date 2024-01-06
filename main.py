# import library
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from sklearn.feature_extraction.text import TfidfVectorizer
from flask import Flask, render_template, request, url_for

# inisialisasi flask app
app = Flask(__name__, template_folder='templates')

# load dataset
df = pd.read_excel('clean_dataset_quran_stem.xlsx')
dataset_feature = df['ProcessedText'].astype(str)

# load model tf-idf
vectorizer = TfidfVectorizer()
corpus_vectorized = vectorizer.fit_transform(dataset_feature)

# Membuat objek stemmer bahasa Indonesia
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# Membuat fungsi untuk membersihkan teks
def clean_text(text):
  # Menghapus angka, tanda baca, dan spasi berlebih
  text = re.sub(r'\d+', '', text)
  text = re.sub(r'[^\w\s]', '', text)
  text = re.sub(r'\s+', ' ', text)
  # Mengubah semua huruf menjadi huruf kecil
  text = text.lower()
  # Mengembalikan teks yang sudah dibersihkan
  return text

# Membuat fungsi untuk melakukan stemming
def stem_text(text):
  # Memecah teks menjadi kata-kata
  words = nltk.word_tokenize(text)
  # Melakukan stemming untuk setiap kata
  stemmed_words = [stemmer.stem(word) for word in words]
  # Menggabungkan kata-kata yang sudah distem menjadi teks
  stemmed_text = ' '.join(stemmed_words)
  # Mengembalikan teks yang sudah distem
  return stemmed_text

# fungsi untuk menampilkan hasil terbaik
def show_best_results(dataset, scores_array, top_n=20):
    sorted_indices = scores_array.argsort()[::-1]
    results = []
    for position, idx in enumerate(sorted_indices[:top_n]):
        row = dataset.iloc[idx]
        arabic = row["arabic"]
        indonesian = row["indonesian"]
        ayat = row["ayat"]
        nama_surat = row["nama_surat"]
        score = scores_array[idx]
        if score > 0:
            results.append((arabic, indonesian, nama_surat, ayat))
        else:
            break
    return results

# fungsi untuk menghitung skor tf-idf
def run_tfidf(query):
    clean_input = clean_text(query)
    steam_input = stem_text(clean_input)
    query_vectorized = vectorizer.transform([steam_input])
    scores = query_vectorized.dot(corpus_vectorized.transpose())
    scores_array = scores.toarray()[0]
    return scores_array

# route untuk halaman utama
@app.route("/", methods=["GET", "POST"])
def index():
    # Jika metode permintaan adalah GET, tampilkan laman html tanpa hasil
    if request.method == "GET":
        return render_template("index.html")
    # Jika metode permintaan adalah POST, ambil data dari form dan jalankan fungsi TF-IDF
    elif request.method == "POST":
        # Ambil query dan top_n dari form
        query = request.form.get("query")
        # Jalankan fungsi TF-IDF dan dapatkan array skor
        scores_array = run_tfidf(query)
        # Tampilkan hasil terbaik dengan menggunakan fungsi show_best_results
        results = show_best_results(df, scores_array)
        # Render laman html dengan hasil
        return render_template("index.html", results=results)

# jalankan app
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)