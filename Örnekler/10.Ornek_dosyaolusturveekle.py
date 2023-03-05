import os
import shutil


try:
    os.mkdir("veriler")
except FileExistsError:
    print("Halen varolan bir dosya oluşturulamaz:")

for i in range(1,101):
    with open(f"veriler/veri_{i}.txt","w") as f:
        f.write(f"veri_{i}")

try:
    os.mkdir(r"C:\Users\batu_\set")
except FileExistsError:
    print("Halen varolan bir dosya oluşturulamaz:")

try:
    os.mkdir(r"C:\Users\batu_\set\train")
except FileExistsError:
    print("Halen varolan bir dosya oluşturulamaz:")

try:
    os.mkdir(r"C:\Users\batu_\set\test")
except FileExistsError:
    print("Halen varolan bir dosya oluşturulamaz:")

for i in range(1,81):
    shutil.copy(f"C:/Users/batu_/Desktop/Python_Lessons/veriler/veri_{i}.txt",r"C:\Users\batu_\set\train")

for i in range(81,101):
    shutil.copy(f"C:/Users/batu_/Desktop/Python_Lessons/veriler/veri_{i}.txt",r"C:\Users\batu_\set\test")