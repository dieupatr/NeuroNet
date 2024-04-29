from LexDrawio import *
import pickle

import os
import sys


# Generate by AI
# Valid +

def create_folder(folder_name):
    try:
        os.makedirs(folder_name)
        
    except :
        pass

# Generate by AI
# Valid +

def pickle_dict(dictionary, filename):
    """
    Pickle a dictionary to a file.

    Parameters:
        dictionary (dict): The dictionary to pickle.
        filename (str): The name of the file to pickle to.
    """
    with open(filename, 'wb') as file:
        pickle.dump(dictionary, file)



#############################



def GenerateCode(DiagrammName):

    Code=f"""
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

Fucntions=$
       "lb":  lambda x :  LinearBool(x)
       , "b": lambda x:   Bias(x)
       , "id": lambda x:  Id(x)
       §
       

NeuronTypes=[ Type for Type in Fucntions]
#########################################

#Load Neurons
with open('Modell_{DiagrammName}/Neurons_{DiagrammName}.pkl', 'rb') as file:   Neurons = pickle.load(file)

#Load Arrows
with open('Modell_{DiagrammName}/Weights_{DiagrammName}.pkl', 'rb') as file:   Arrows = pickle.load(file)


def RunNetwork_{DiagrammName}(Input):

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
                     
       return Neurons

    """
    return (Code.replace("$","{")).replace("§","}")

    









def CreateNeuronenAndWeights(Diagramm, DiagrammName):

       NeuronsIdtoNr={   }
       Neurons={  }

       Weights={    }

       WeightArrows=[]

       for block in Diagramm.blocks:
              
              Id=block.Attr["id"]
              value=block.Attr["value"]
              Typ=block.Attr["style"][0]
              parent=block.Attr["parent"]

              if Typ=="ellipse" :

                     #Check Syntax

                     value=value.split(":")
                     
                     Nr=value[1]
                     NeuroTyp=value[0]

                     NeuronsIdtoNr[Id]=Nr
                     Neurons[Nr]=[NeuroTyp,    0]

              if Typ=="edgeLabel":

                  Tag="NoTrain"

                  if value=="w":
                      Tag="Train"
                      value="0"
                      
                  Weights[parent]=(value,Tag)

       for arrow in Diagramm.arrows:

              source=arrow.Attr["source"]
              target=arrow.Attr["target"]
              Id=arrow.Attr["id"]

              Tag=Weights[Id][1]
              Weight=Weights[Id][0]
              

              WeightsItem=[
                     
                     NeuronsIdtoNr[source] ,
                     NeuronsIdtoNr[target],
                     Weight,
                     Tag
                     

                     ]

              WeightArrows.append(  WeightsItem  )


       #Save Arrows and Neurons

       Root="Modell_"+DiagrammName

       create_folder(Root)

       pickle_dict(Neurons ,Root+"/Neurons_"+ DiagrammName+".pkl")

       pickle_dict(WeightArrows ,Root+"/Weights_"+ DiagrammName+".pkl")

       
       
                
def BuildNeuralNetworkModell(file_path, DiagrammName):

    Diagramm=ParseDiagramsFromXmlFile(file_path)
    Diagramm=Diagramm[DiagrammName]

    FileName="NeuroModell_"+DiagrammName+".py"

    create_folder("Modell_"+DiagrammName)
    CreateNeuronenAndWeights(Diagramm, DiagrammName)
    
    File=open(FileName,"w")
    File.write( GenerateCode(DiagrammName) )
    File.close(  )
                     

                     
              
       
file_path=sys.argv[1]
#"NeuroTest.drawio"
DiagrammName=sys.argv[2]
#"Test1"


BuildNeuralNetworkModell(file_path, DiagrammName)


















