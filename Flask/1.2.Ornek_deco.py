from flask import Flask , request

app= Flask(__name__)

Liste=['Ahmet','Veli','Ali']

@app.route('/')
def index():
    return'index'


@app.route('/login/<kullanici>', methods=['GET', 'POST'])
def login(kullanici):
    if request.method == 'POST':
        if kullanici in Liste:
            return"kullanici zaten kayıtlı"
        else:
            Liste.append(kullanici)
            kaydet(kullanici)    
    elif request.method == 'GET':
        if kullanici in Liste:
            return selamlar(kullanici)
        else:
            return 'kullanici bulunamadı'
    
@app.route('/kullanici_listesi')
def kullanici_listesi():
    return """<!DOCTYPE html>
<html>

   <head>
      <title>HTML Table</title>
   </head>
	
   <body>
      <table border = "1" width = "100%">
         
         <tr>
            <td>
               <table border = "1" width = "100%">
                  <tr>
                     <th>Name</th>
                     <th>Salary</th>
                  </tr>
                  <tr>
                     <td>Tugce</td>
                     <td>5000</td>
                  </tr>
               </table>
            </td>
         </tr>
         
      </table>
   </body>
	
</html>"""





def selamlar(isim):
    return'selamlar'+isim


def kaydet(isim):
    return isim+'kaydedildi'
if __name__ == '__main__':
    app.run(debug=True)
