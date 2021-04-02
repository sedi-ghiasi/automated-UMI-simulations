import Rhino
import rhinoscriptsyntax as rs
import json
import sys
import warnings
from csv import reader
import time
warnings.filterwarnings("ignore")


bldgs=rs.ObjectsByLayer('umi::Buildings')
print(len(bldgs))
rs.SelectObjects(bldgs[:])

with open("D:\Modelsw18.csv", 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    l = list(csv_reader)

for i in  range(15,17) :    
    col_number = 23
    temp = l[i][col_number]
    print(temp)
    col_number = 20
    name= l[i][col_number]

    print(name)
    rs.Command("UmiSetBuildingSetting S T " +'"'+ temp +'"')
    #rs.Command("_-SaveAs" +" " +'"'+OutputPath+ '"')
    for W in xrange(5):
        Rhino.RhinoApp.SetCommandPrompt(str(W))
        time.sleep(1)
    #rs.Command("_Save")
    #for z in xrange(30):
        #Rhino.RhinoApp.SetCommandPrompt(str(z))
        #time.sleep(1)
    
    rs.Command("_-UmiSimulateEnergy"+ " ")
        #rs.Command("_-UmiSimulateEnergy" )    
    for F in xrange(1*60):
         Rhino.RhinoApp.SetCommandPrompt(str(F))
         time.sleep(1)
    #rs.Command("_Save" +'"' + name + '"')
    #Save(str(name))
    #Save(path+str(name))
    rs.Command("_Save")
    for s in xrange(15):
        Rhino.RhinoApp.SetCommandPrompt(str(s))
        time.sleep(1)    
    rs.Command("_-UmiBundleSaveAs " + '"' + name + ".umi" + '"')
 


