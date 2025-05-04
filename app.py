from flask import Flask, render_template, request
import pandas as pd
from label import get_sentiment

app = Flask(__name__, static_folder="Gambar visualisasi")


@app.route('/')
def index():
    # Load data terbaru
    df = pd.read_csv('komentar_dengan_sentimen.csv')

    # Hitung statistik
    total = len(df)
    positif = len(df[df['sentimen'] == 'Positif'])
    netral = len(df[df['sentimen'] == 'Netral'])
    negatif = len(df[df['sentimen'] == 'Negatif'])
    sedih = len(df[df['sentimen'] == 'Sedih'])
    marah = len(df[df['sentimen'] == 'Marah'])
    takut = len(df[df['sentimen'] == 'Takut'])

    data_komentar = list(zip(df['komentar'], df['sentimen']))

    return render_template(
        'index.html',
        total=total,
        positif=positif,
        netral=netral,
        negatif=negatif,
        sedih=sedih,
        marah=marah,
        takut=takut,
        data_komentar=data_komentar
    )

@app.route('/analisis', methods=['POST'])
def analisis():
    komentar = request.form['komentar']
    sentimen = get_sentiment(komentar)

    # Tambahkan komentar baru ke file CSV
    new_row = pd.DataFrame([[komentar, sentimen]], columns=['komentar', 'sentimen'])
    new_row.to_csv('komentar_dengan_sentimen.csv', mode='a', header=False, index=False)

    # Load data terbaru
    df = pd.read_csv('komentar_dengan_sentimen.csv')

    # Hitung statistik
    total = len(df)
    positif = len(df[df['sentimen'] == 'Positif'])
    netral = len(df[df['sentimen'] == 'Netral'])
    negatif = len(df[df['sentimen'] == 'Negatif'])
    sedih = len(df[df['sentimen'] == 'Sedih'])
    marah = len(df[df['sentimen'] == 'Marah'])
    takut = len(df[df['sentimen'] == 'Takut'])

    data_komentar = list(zip(df['komentar'], df['sentimen']))

    return render_template(
        'index.html',
        total=total,
        positif=positif,
        netral=netral,
        negatif=negatif,
        sedih=sedih,
        marah=marah,
        takut=takut,
        data_komentar=data_komentar,
        sentimen=sentimen
    )
if __name__ == '__main__':
    print("Flask server dimulai!")
    app.run(debug=True)

