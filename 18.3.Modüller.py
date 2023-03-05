import datetime
#tarihler arasındaki fark
tarih1 = datetime.date(2023,3,1)
tarih2 = datetime.date(2023,3,4)

fark= tarih2-tarih1
print("iki tarih arasındaki fark:",fark.days,"gün")
#tarihe gün ekleme
tarih = datetime.date(2023,3,4)
yeni_tarih = tarih + datetime.timedelta(days=7)
print("Tarihe 7 gün eklenince",yeni_tarih)

tarih3=datetime.date(2023,3,4)
print("Tarih formati:",tarih3.strftime("%d/%m/%Y"))

zaman=datetime.time(12,30,45)
print("zaman formatı:",zaman.strftime("%H:%M:%S"))

tarih_ve_zaman = datetime.datetime.now()
print("Tarih ve saat formati:",tarih_ve_zaman.strftime("%d/%m/%Y %H:%M:%S"))