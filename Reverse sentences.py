str1="jojo JELEK"
print(f"input \t\t\t:{str1}")
spasi=""
for i in str1.split():
    spasi+=i[::-1]+" "
out=spasi[-2::-1].swapcase()
print(f"output reverse and swap :{out}")
#print(f"swapcase :{swap}")
#rev=(swap[::-3])
#print(f"reversed :{rev}")
#swap=str1.swapcase()


