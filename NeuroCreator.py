from LexDrawio import *






def CreateNeuronenAndWeights(Diagramm):
       pass






file_path="NeuroTest.drawio"

Diagramm=ParseDiagramsFromXmlFile(file_path)

Diagramm=Diagramm["Test1"]


for block in Diagramm.blocks:

       block.PrintData()

for arrow in Diagramm.arrows:

       arrow.PrintData()
