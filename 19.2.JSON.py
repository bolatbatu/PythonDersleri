import json

#19.4.data.json üzerine veri yazdık.

#json içine altaki veriyi yazmak için kullandık.
data={
    "name":"john",
    "age": 30,
    "address":
    {
        "street":"123 main st",
        "city":"New York"
    }
}

with open("19.4.data.json","w") as f:                    #Dosya yoksa oluşturur, varsa üzerine yazar.
    json.dump(data, f)                                   #Data yazmak için kullanılan komut.