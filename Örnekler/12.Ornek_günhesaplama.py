import datetime
import time

while True:

    bugün = datetime.date.today()
    simdi = datetime.datetime.now()

    YKS = "2023-6-17 10:15:00"

    suanki_zaman = str(bugün) + " " + str(simdi.strftime("%H:%M:%S"))
    start = datetime.datetime.strptime(suanki_zaman,'%Y-%m-%d %H:%M:%S')
    ends = datetime.datetime.strptime(YKS,'%Y-%m-%d %H:%M:%S')
    
    print(ends-start)
    time.sleep(1)