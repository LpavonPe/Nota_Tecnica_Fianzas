import math
import csv
import numpy as np
import pdb

def Nota_tec():
    x =0
    while x== 0: 
        x = input("Desea realizar una Nota tecnica(N) o solo obtener los calculos de la misma(C)?")
        if x == "N" or "n":
            with open("Datos _fianzas_2008.csv", newline='') as f:
                reader = csv.reader(f)
                n_row=0
                datos={}
                Ramos=[]                
                for row in reader: 
                    Ramos.append(row[0])
                Ramos.pop(0)
                for row in reader:
                    for i in row:
                        Columnas.append(row[i])
                for i in Ramos:
                    datos[i]={}
            pass
        elif x == "C" or "c":
            pass
        else:
            x=0
            print("Selección no reconocida, por favor ingrese N para nota tecnica o C para realizar los calculos")