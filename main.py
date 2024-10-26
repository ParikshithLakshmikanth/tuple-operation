mytup = ()
print(mytup)

mytup = (1,2,3)
print(mytup)

mytup = (1,"hello",3.4)
print(mytup)

mytup = ("mouse",[8,4,6],(1,2,3))
print(mytup)

mytup = ("p","e","r","m","i","t")
print(mytup[0])
print(mytup[5])

mytup = ("mouse",[8,4,6],(1,2,3))
print(mytup[0][3])
print(mytup[1][1])

mytup = ("p","e","r","m","i","t")
print("Sliced:",mytup[1:4])

for i in mytup:
    print("hello",i)
