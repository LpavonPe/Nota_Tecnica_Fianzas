import math
import csv
import numpy as np
import pdb

def Nota_tec():
    x =0
    y =0
    datos_nuevos=0
    while x== 0: 
        x = input("Desea realizar una Nota tecnica(N) o solo obtener los calculos de la misma(C)?")
        if x == "N" or "n":
            while datos_nuevos ==0:
                datos_nuevos= input("Desea introducir nuevos datos estadisticos(N) o trabajar con los actuales(A)?")
                if datos_nuevos == "N" or "n":
                    print("los datos deben de estar en formato csv para poder ser cargados correctamente")
                    año_inicial= int(input("Cual es el primer año para el cual desea cargar los datos?"))
                    año_final= int(input("Hasta que año desea que incluyan sus calculos"))
                    año_final_datos= int(input("Cual es el ultimo año para el cual desea cargar los datos?"))
                    diferencia = año_final-año_final_datos
                    if diferencia != 0:
                        estimar= input(f"Desea estimar datos para los {diferencia} años faltantes?(S/N)")
                        if estimar == "S" or "s":
                            años_datos = año_final_datos-año_inicial
                            archivos=[]
                            años = año_final_datos-año_inicial
                            for año in range(años+1):
                                i=0
                                archivos[año]=input(f"Introdusca la ruta del archivo correspondiente al año {año_inicial +i}")
                                #archivos[año].replace("\","/")
                                i+=1
                            años_agregados= len(archivos)
                            correcto= input(f"Agrego {años_agregados} archivos, es correcto?(S/N)")
                            if correcto == "S" or "s":
                                for archivo in archivos:
                                    for año in range(años +1):
                                        datos_año = pd.read_csv(archivo, encoding="iso-8859-1")
                            año_final_estimado=input("Hasta que año desea estimar los datos?")
                            metodo_de_estimación= input("Mediante que metodo desea estimar los datos, estandar(E), ...") 
                            pass
                        elif estimar == "N" or "n":
                            años = año_final_datos-año_inicial
                            archivos=[]
                            for año in range(años+1):
                                i=0
                                archivos[año]=input(f"Introdusca la ruta del archivo correspondiente al año {año_inicial +i}")
                                #archivos[año].replace("\","/")
                                i+=1
                            años_agregados= len(archivos)
                            correcto= input(f"Agrego {años_agregados} archivos, es correcto?(S/N)")
                            if correcto == "S" or "s":
                                for archivo in archivos:
                                    for año in range(años +1):
                                        datos_año = pd.read_csv(archivo, encoding="iso-8859-1")
                                            
                    
                        pass
                elif datos_nuevos == "A" or "a":
                    años=[2008,2009,2010,2011,2012,2013,2014]
                    estimar_actuales=input("Se tienen datos del 2008 al 2014, desea estimar los datos restantes?(S/N)")
                    if estimar_actuales == "S" or "s":
                        metodo_estimacon = input("Mediante que metodo desea estimar los datos, ...")
                        pass
                    elif estimar_actuales == "N" or "n":
                        for año in años:
                            datos_año = pd.read_csv(f"Datos _fianzas_{año}.csv", encoding="iso-8859-1")
                elif datos_nuevos == "I" or "i":
                    print("se cuentan con datos de los años 2008 al 2014")
                    datos_2008 = pd.read_csv("Datos _fianzas_2008.csv", encoding="iso-8859-1")
                    print("los datos cargados tienen esta forma")
                    datos_2008.head()
                    datos_nuevos=0
                else:
                    datos_nuevos =0
                    print("Selección no reconocida, por favor ingrese N para trabajar con nuevos datos, A para trabajar con los datos actuales o I para obtener información sobre los datos actuales")
        
        elif x == "C" or "c":
            pass
        else:
            x=0
            print("Selección no reconocida, por favor ingrese N para nota tecnica o C para realizar los calculos")