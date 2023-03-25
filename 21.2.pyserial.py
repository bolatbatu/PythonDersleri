import serial, time                          #Ardunio üzerine kod yazma.
arduino = serial.Serial("COM3",9600)         #COM usb'nin hangi porta takılı olduğunu göstermektedir.
time.sleep(2)
arduino.write(b"1")                          #Yazmak için write(b" ") şeklinde kullanılır.
arduino.close()                              #Kapatmak için kullanılır.