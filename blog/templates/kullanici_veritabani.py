import sqlite3

# Veritabanına bağlan
conn = sqlite3.connect('kullanici_veritabani.db', check_same_thread=False)
cursor = conn.cursor()

# Kullanıcı tablosunu oluştur
cursor.execute('''CREATE TABLE IF NOT EXISTS kullanicilar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kullanici_adi TEXT UNIQUE,
    sifre TEXT
)''')
conn.commit()

# Veritabanı bağlantısını kapat
conn.close()
