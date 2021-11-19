a=int(input('masukan nilai a='))
b=int(input('masukan nilai b='))

#OR(|)
print("    ----OR----")
c=a|b
print('nilai a=',a, 'biner',format(a,'08b'))
print("nilai a=",b, "biner", format(b,'08b'))
print('-----------------------------|')
print("nilai a=",c, "biner", format(c,'08b'))

#AND(&)
print("\n    ----AND----")
c=a&b
print('nilai a=',a, 'biner',format(a,'08b'))
print("nilai a=",b, "biner", format(b,'08b'))
print('-----------------------------&')
print("nilai a=",c, "biner", format(c,'08b'))

#XOR(^)
print("\n    ----XOR----")
c=a^b
print('nilai a=',a, 'biner',format(a,'08b'))
print("nilai a=",b, "biner", format(b,'08b'))
print('-----------------------------^')
print("nilai a=",c, "biner", format(c,'08b'))

#NOT
print('\n    ----NOT----')
d=~a
print('nilai a=',a, 'biner',format(a,'08b'))
print('nilai d', d, 'biner',format(d,'08b'))
print('\n   -0 ke 1 dan 1 ke 0-')
#karena angka 0 tak betanda maka not adalah di balik mulai dai -1

# operasi biner dibalik 0 manjadi 1 vice versa
e=0b11111111
f=a^e
print('nilai a=',a, 'biner',format(a,'08b'))
print('-----------------------dibalik')
print('nilai f,',f,'biner',format(f,'08b'))


#SHIFT
#SHFIT RIGHT(>>)
print('\n    ---->>----')
d=a>>2
print('nilai a=',a, 'biner',format(a,'08b'))
print('nilai d', d, 'biner',format(d,'08b'))
#SHFIT LEFT(<<)
print('\n    ----<<----')
d=a<<2
print('nilai a=',a, 'biner',format(a,'08b'))
print('nilai d', d, 'biner',format(d,'08b'))
