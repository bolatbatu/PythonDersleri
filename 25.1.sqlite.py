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

def kayit_table():
    conn = sqlite3.connect('25.2.lite.db')

    name = input("Adinizi girin: ")
    surname = input("Soyad girin: ")
    age = input("Yaşinizi girin: ")
    email = input("Mail girin: ")
    password = input("Şifre girin: ")

    conn.execute("INSERT INTO users (name, surname, age, email, password) VALUES (?, ?, ?, ?, ?)", (name,surname,age,email,password))
    conn.commit()
    conn.close()
        
def kullanici_girisi():
    conn = sqlite3.connect("25.2.lite.db")
    while True:
        name = input("Adinizi girin: ")
        password = input("Parolanizi girin: ")

        cursor = conn.execute("SELECT * FROM users WHERE name = ? AND password = ?", (name, password))
        row = cursor.fetchone()
        
        if row is None:
            print("Kullanici adi veya parola yanliş. Tekrar deneyin.")
        else:
            print("Giriş başarili. Hoş geldiniz, ", row[1],row[2])
            break
        conn.close()
while True:
    secim =int(input("""
    1*Kayit
    2*Giriş
    """))
    
    while True:
        if secim == 1:
            print("Kaydinizin yapilmasi için istenilen bilgileri doldurunuz.")
            kayit_table()
            break
        elif secim == 2:
            kullanici_girisi()
            break
        