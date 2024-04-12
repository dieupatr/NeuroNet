from LexDrawio import *
import pickle

import os



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
                     Neurons[Nr]=(NeuroTyp,1)

              if Typ=="edgeLabel":

                     Weights[parent]=value

       for arrow in Diagramm.arrows:

              source=arrow.Attr["source"]
              target=arrow.Attr["target"]
              Id=arrow.Attr["id"]

              WeightsItem=(
                     
                     NeuronsIdtoNr[source] ,
                     NeuronsIdtoNr[target],
                     Weights[Id]

                     )

              WeightArrows.append(  WeightsItem  )


       #Save Arrows and Neurons

       Root="Modell_"+DiagrammName

       create_folder(Root)

       pickle_dict(Neurons ,Root+"/Neurons_"+ DiagrammName+".pkl")

       pickle_dict(WeightArrows ,Root+"/Arrows_"+ DiagrammName+".pkl")

       
       

              


       
       print(Neurons)
       print(WeightArrows)

                     

                     
                     

                     

                     
              
       






file_path="NeuroTest.drawio"
DiagrammName="Test1"

Diagramm=ParseDiagramsFromXmlFile(file_path)

Diagramm=Diagramm[DiagrammName]

CreateNeuronenAndWeights(Diagramm, DiagrammName)


