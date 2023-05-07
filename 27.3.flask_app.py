from flask import Flask,request
app = Flask(__name__)

liste= ["ahmet","mehmet","ali","veli"]

@app.route("/")
def index():
    return "index"

@app.route("/login/<kullanici>", methods=["GET","POST"])
def login(kullanici):
    if request.method == "POST":
        if kullanici in liste:
            return "Kullanıcı zaten kayıtlı"
        else:
            liste.append(kullanici)
            kaydet(kullanici)
    elif request.method=="GET":
        if kullanici in liste:
            return selamla(kullanici)
        else:
            return "kullanıcı kayıtlı değil"
@app.route("/liste")
def liste():
    return"table, th, td { border: 1px solid white; border-collapse: collapse; }th, td { background-color: #96D4D4; }"

def selamla(isim):
    return "selam" + isim
def kaydet(isim):
    return isim + "kaydedildi"
if __name__ == "__main__":
    app.run(debug=True)

