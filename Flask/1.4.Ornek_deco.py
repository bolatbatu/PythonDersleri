from flask import Flask, render_template, request

app = Flask(__name__)
klist=[["Ali","Ayse"],["Mehmet","Fatma"]]

@app.route('/kullanici_listesi')
def kullanici_listesi(): 
    return  render_template('kullanici.html', kullanicilar = klist )

@app.route("/kullanici_listesi/ekle",methods=['POST'])
def kullanici_ekle(): 
    ad=request.form.get("kullanici_adi")
    soyad=request.form.get("kullanici_soyadi")
    klist.append([ad,soyad])
    return render_template("kullanici.html", kullanicilar = klist)

if __name__ == '__main__':  
    app.run(debug=True)