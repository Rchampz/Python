import math

#keliling lingkaran
print(5*"-","Luas Lingkaran",5*"-")
r = float(input("jari-jari lingkaran\t:"))
luas = math.pi*r*r
hasilluas=f"Luas Lingkaran \t\t:{luas:.2f}"
print(hasilluas)

#keliling persegi
print(5*"-","Luas persegi panjang",5*"-")
a=float(input("panjang persegi \t:"))
b=float(input('lebar persegi \t\t:'))
luasp=a*b
hluasp=f"Luas Persegi Panjang \t:{luasp:.2f}"
print(hluasp)