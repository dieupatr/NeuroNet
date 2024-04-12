
import pickle

# Activation functions
def LinearBool(x):

       if x>=0 :
              return 1
       else:
              return 0
def Bias(x):

       return 1

def Id(x):
       return x

###########

Fucntions={
       "lb":  lambda x :  LinearBool(x)
       , "b": lambda x:   Bias(x)
       , "id": lambda x:  Id(x)
       }
       

NeuronTypes=[ Type for Type in Fucntions]
#########################################

#Load Neurons
with open('Neurons_Test1.pkl', 'rb') as file:   Neurons = pickle.load(file)

#Load Arrows
with open('Arrows_Test1.pkl', 'rb') as file:   Arrows = pickle.load(file)


def RunNetwork_Test1(Input):

       NumNeurons=len(Neurons)

       for i in range( NumNeurons ):

              neuron=Neurons[ str(i+1) ]
              
              Type=neuron[0].lower()
              value=neuron[1]
              NumNeuron=i+1

              #Input neuron
              
              if Type=="i":
                     Neurons[ str(i+1) ][1]=Input[i]
                     continue

              ######

              if Type in NeuronTypes :

                     net=0

                     #Iterate over all connections

                     for arrow in  Arrows:

                            source=arrow[0]
                            target=arrow[1]
                            weight=float(arrow[2])


                            if target==str(NumNeuron):

                                   
                                   x=float(Neurons[ source ][1])
                                   net=net+x*weight

                     #Compute activiation funcion

                     value=Fucntions[Type](net)

                     Neurons[ str(i+1) ][1]=value
                     continue


    