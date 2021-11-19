num_items=100
item_coins=1
n=2

jumlahbeli=50
num_coins=50

sisabarang=num_items-(jumlahbeli*item_coins)
sisauang=num_coins-(jumlahbeli*item_coins)
print(sisabarang)
print(sisauang)
if jumlahbeli>>num_items:
    print("Not enough items in the machine")
if num_coins<<item_coins:
    print("Not enough coins")
else:
    print(f"{rumus}")
