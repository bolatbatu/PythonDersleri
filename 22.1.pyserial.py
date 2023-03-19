import serial                               #Ardunio üzerindeki kodu byte olarak okuma.
ser = serial.Serial(port="COM3")            #COM3 cihazın takılı olduğu usb portu.(Bu portu aygıt yöneticisinden öğrenebilirsiniz.)
while 1 :                                   #while 1: ile while True: aynı anlama gelmektedir.
    print(ser.read())                       #Okumak için read(), line olarak yazıldıysa readline() yazılarak okunur.