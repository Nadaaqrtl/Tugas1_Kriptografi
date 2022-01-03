import os
from hashlib import *
from tkinter import Tk     
from tkinter.filedialog import askopenfilename

print("Pilih file yang ingin di enkripsi / dekripsi")


Tk().withdraw() 
filename = askopenfilename() 
print(filename)


Fin = filename
Fout = str(input("Masukan nama file baru (hasil enkripsi/dekripsi) : "))

Key = str(input("Masukkan Kunci (Key) : "))

ShaKey = sha256(Key.encode('utf-8')).digest()
print(filename)



with open(Fin, 'rb') as Fin:
    with open (Fout, 'wb') as Fout:
        i = 0
        while Fin.peek():
            c = ord(Fin.read(1))
            j = i % len(ShaKey)
            b = bytes([c^ShaKey[j]])
            Fout.write(b)
            i = i + 1
print("File telah dienkripsi/dekripsi !")

