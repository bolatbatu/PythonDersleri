from flask import Flask , render_template

app= Flask(__name__)

@app.route('/')
def kullanici(name="batuhan"):
    return render_template("selamla.html", name=name)

if __name__ == "__main__":            #Eğer name ile main eşleşiyorsa burada çalışır. Fakat farklı bir yerden import edilerek çağırıldığında bu eşleşme gerçekleşmeyecek ve sadece fonskiyonu çekecek.
    app.run(debug=True) 