import pickle





#Load Neurons
with open('Neurons_Test1.pkl', 'rb') as file:   Neurons = pickle.load(file)

#Load Arrows
with open('Arrows_Test1.pkl', 'rb') as file:   Arrows = pickle.load(file)



print(Neurons)
print(Arrows)




def RunNetwork_Test1(Input):

       NumNeurons=len(Neurons)

       for i in range( NumNeurons ):

              neuron=Neurons[ str(i+1) ]

              print(neuron)


Input=[]
RunNetwork_Test1(Input)
