import datetime

while True:

    bugün = datetime.date.today()
    simdi = datetime.datetime.now()

    dogumgunu = "2024-2-15 23:59:59"                                  #Doğum gününü tarihi.

    suanki_zaman = str(bugün) + " " + str(simdi.strftime("%H:%M:%S"))
    start = datetime.datetime.strptime(suanki_zaman,'%Y-%m-%d %H:%M:%S')
    ends = datetime.datetime.strptime(dogumgunu,'%Y-%m-%d %H:%M:%S')
    
    difference = ends - start
    difference_in_seconds = difference.total_seconds()
    print("Dogum gunune kalan saniye:",difference_in_seconds,end="\r") #Dijital olarak akar.