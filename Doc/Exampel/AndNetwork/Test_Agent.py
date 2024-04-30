from NeuroModell_Test2 import RunNetwork_Test2


Inp=[1,0]
Neurons=RunNetwork_Test2(Inp)
y=Neurons["4"][1]

print(Neurons)

print("Die Augabe ist: "+str(y) )



