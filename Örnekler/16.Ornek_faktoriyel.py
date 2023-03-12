number = int (input("sayıyı giriniz..."))
factorial = 1
i=1
if number >= 0:
  while i <= number:
      factorial*=i
      i+=1
  print("Girdiğiniz sayının faktöriyeli:",factorial)
else:
  print ("Negatif sayıların faktöriyeli olmaz!")
