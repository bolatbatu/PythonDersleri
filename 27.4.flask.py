

from flask import Flask, request

app = Flask(__name__)

# listeyi oku
def read_list():
    with open("list.txt", "r") as f:
        return f.read().splitlines()

# listeye isim ekle
@app.route("/add", methods=["POST"])
def add_name():
    name = request.form["name"]
    with open("list.txt", "a") as f:
        f.write(name + "\n")
    return "OK"

# listeden isim çıkart
@app.route("/remove", methods=["POST"])
def remove_name():
    name = request.form["name"]
    names = read_list()
    if name in names:
        names.remove(name)
        with open("list.txt", "w") as f:
            f.write("\n".join(names))
        return "OK"
    else:
        return "Name not found in list"

# listeyi görüntüle
@app.route("/list")
def view_list():
    names = read_list()
    return "<br>".join(names)

if __name__ == "__main__":
    app.run()

#curl -d "name=John Doe" -X POST http://127.0.0.1:5000/remove

#curl -d "name=Jane Doe" -X POST http://127.0.0.1:5000/add
