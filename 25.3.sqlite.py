import sqlite3

def create_table():
    conn = sqlite3.connect("25.2.lite.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT,
        surname TEXT,
        age INTEGER,
        email TEXT,
        password TEXT
        )""")
    conn.commit()
    conn.close()

def kayit_ekle():
    name = input("Adinizi girin: ")
    surname = input("Soyad girin: ")
    age = input("Yaşinizi girin: ")
    email = input("Mail girin: ")
    password = input("Şifenizi giriniz:")
    conn = sqlite3.connect("25.2.lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, surname, age, email, password) VALUES (?, ?, ?, ?, ?)", (name,surname,age,email,password))
    conn.commit()
    conn.close()

def giris_yap():
    email = input("E-mail adresinizi giriniz:")
    password = input("Şifrenizi giriniz:")
    conn = sqlite3.connect("25.2.lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email = ?", (email,))
    data = cur.fetchone()
    if data [5] == password:
        print(f"Giriş başarılı! {data[1]} {data[2]}")
    else:
        print("Giriş başarısız.")
    conn.commit()
    conn.close()

giris_yap()
