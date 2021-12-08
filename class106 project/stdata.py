import csv 
import numpy as np

def getdata(datapath):
    marks =[]
    daysavailable=[]

    with open (datapath)as cvfile:
        cvreader=csv.DictReader(cvfile)
        for row in cvreader:
            marks.append(float(row['Size of TV']))
            daysavailable.append(float(row['	Average time spent watching TV']))
    return{'x':marks,'y':daysavailable} 

def cof(datasource):
    correlation=np.corrcoef(datasource['x'],datasource ['y']) 
    print("Correlation between Marks In Percentage and Days Present :-  \n--->",correlation[0,1])
def setup():
    datapath="sm.csv"
    datasource=getdata(datapath)
    cof(datasource)    


setup()  