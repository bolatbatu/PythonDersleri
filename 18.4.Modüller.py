import datetime
import time

while True:

    bugün = datetime.date.today()
    simdi = datetime.datetime.now()

    YKS = datetime.date(2023,6,17)
    YKS2 = datetime.time(10,0,0)

    suanki_zaman = str(bugün) + " " + str(simdi.strftime("%H:%M:%S"))
    start = datetime.datetime.strptime(suanki_zaman,'%Y-%m-%d %H:%M:%S')

    YKS3 = str(YKS) + " " + str(YKS2.strftime("%H:%M:%S"))
    ends = datetime.datetime.strptime(YKS3, '%Y-%m-%d %H:%M:%S')
    


#Toplam kalan süreyi saniyeye çevirip
    """difference = ends - start
    difference_in_seconds = difference.total_seconds()
    print("Kalan saniye:",difference_in_seconds)"""

    last = ends-start
    month = ((last).days)//30
    day = ((last).days)%30
    seconds = ((ends-start).seconds)%60
    hours = last.seconds//3600
    minute = last.seconds%3600//60
    print(month, "Ay",day,"Gün",hours,":",minute,":",seconds)
    time.sleep(1)