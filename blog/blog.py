from flask import Flask, render_template, request, redirect, session
from datetime import timedelta
import sqlite3

app = Flask(__name__)
app.secret_key = 'gizli_anakey'
app.permanent_session_lifetime = timedelta(days=1)

conn = sqlite3.connect('kullanici_veritabani.db', check_same_thread=False)
cursor = conn.cursor()

# Kullanıcı tablosunu oluştur
cursor.execute('''CREATE TABLE IF NOT EXISTS kullanicilar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kullanici_adi TEXT UNIQUE,
    sifre TEXT
)''')
conn.commit()

bloglar = {}

@app.route('/')
def index():
    if 'giris_ad' in session:
        return redirect('/blog')
    else:
        return redirect('/giris')

@app.route('/giris', methods=['GET', 'POST'])
def giris():
    if 'giris_ad' in session:
        return redirect('/blog')

    if request.method == 'POST':
        giris_ad = request.form.get('giris_ad')
        giris_sifre = request.form.get('giris_sifre')

        cursor.execute("SELECT * FROM kullanicilar WHERE kullanici_adi = ?", (giris_ad,))
        kullanici = cursor.fetchone()

        if kullanici and kullanici[2] == giris_sifre:
            session['giris_ad'] = giris_ad
            return redirect('/blog')

        return render_template('giris.html', hata_mesaji='Kullanıcı adı veya şifre hatalı.')

    return render_template('giris.html', hata_mesaji='')

@app.route('/kaydet', methods=['POST'])
def kaydet():
    ad = request.form.get('ad')
    sifre = request.form.get('kayit_sifre')

    try:
        cursor.execute("INSERT INTO kullanicilar (kullanici_adi, sifre) VALUES (?, ?)", (ad, sifre))
        conn.commit()
    except sqlite3.IntegrityError:
        return redirect('/giris')

    return redirect('/giris')

# Diğer sayfalar ve işlevler buraya eklenecek...

if __name__ == '__main__':
    app.run(debug=True)
