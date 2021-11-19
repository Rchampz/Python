class Hero:#Templete
    pass

hero1=Hero()#Object/instance(instantiate)
hero2=Hero()
hero3=Hero()

hero1.name = 'axe'
hero1.health= 100

hero2.name ='sven'
hero2.health= 200

hero3.name='tutu'
hero3.health=400

print(hero3.__dict__)
print(hero2.name)
print(hero1.health)
print(hero1)