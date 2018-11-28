import math
import csv
import numpy as np
import pdb


def Nota_tec():
    x =0
    y =0
    tipo_usuario=0
    datos_nuevos=0
    while x== 0:
        while tipo_usuario== 0: #Meter un interruptor para este while
            tipo_usuario=input("Usuario final(U) o prestador de servicio(S)?").upper()
            if tipo_usuario == "U":
                x="C"
            elif tipo_usuario == "S":
                x = input("Desea realizar una Nota tecnica(N) o solo obtener los calculos de la misma(C)?").upper()
            else:
                print("Selección no reconocida")
                tipo_usuario =0
        if x == "N":
            while datos_nuevos ==0:
                datos_nuevos= input("Desea introducir nuevos datos estadisticos(N) o trabajar con los actuales(A)?").upper()
                if datos_nuevos == "N":
                    unica= input("Su poliza es para un solo ramo(S) o un podructo mixto(M)").upper()
                    ramos=[]
                    if unica == "S":
                        ramos.append(input("para que ramo es su poliza? (ver opciones disponibles con R)"))
                    elif unica =="M":
                        i=0
                        n_ramos= int(input("Cuantos ramos tiene su poliza?"))
                        for ramo in range(n_ramos +1):
                            i+=1
                            ramos.append(input(f"Cuales es el ramo {i}"))
                    elif unica== "R" or "r":
                        #sacar los ramos disponibles en el df
                        pass
                    MA=int(input("Cual es el monto afianzado?"))
                    print("los datos deben de estar en formato csv para poder ser cargados correctamente")
                    año_inicial= int(input("Cual es el primer año para el cual desea cargar los datos?"))
                    año_final= int(input("Hasta que año desea que incluyan sus calculos"))
                    año_final_datos= int(input("Cual es el ultimo año para el cual desea cargar los datos?"))
                    diferencia = año_final-año_final_datos
                    if diferencia != 0:
                        estimar= input(f"Desea estimar datos para los {diferencia} años faltantes?(S/N)").upper()
                        if estimar == "S":
                            años_datos = año_final_datos-año_inicial
                            archivos=[]
                            años = año_final_datos-año_inicial
                            metodo_de_estimación= input("Mediante que metodo desea estimar los datos, estandar(E), Incremento lineal(L)o Incremento algebracico(A) ?").upper() 
                            for año in range(años+1):
                                i=0
                                archivos.append(input(f"Introdusca la ruta del archivo correspondiente al año {año_inicial +i}"))
                                i+=1
                            for archivo in archivos:
                                datos_año = pd.read_csv(archivo, encoding="iso-8859-1")
                            #Crear df maetro extrallendo datos de los archivos e incluyendo solo los ramos relevantes
                            if metodo_de_estimación =="E":
                                for año in range(diferencia+1):
                                    #Sacar media de los estimadores de los ramos del df
                                    #Sacar desviacion estandar
                                    #meter la media mas dos desviaciones
                                    pass
                                pass
                            elif metodo_de_estimación == "I":
                                incremento= input("Desea conservar la tendencia del incremento en los datos(C) o introducir un incremento(I)?").upper()
                                if incremento =="C":
                                    for año in range(diferencia+1):
                                        #calcular incremento de los datos y replicarlo
                                        pass
                                pass
                            elif metodo_de_estimación == "A":
                                incremento= int(input("que porcentaje desea que incrementos los datos anualmente?"))
                                porcentaje = incremento / 100
                                #meter los datos estimados en el df
                                pass
                        elif estimar == "N":
                            años = año_final_datos-año_inicial
                            archivos=[]
                            for año in range(años+1):
                                i=0
                                archivos.append(input(f"Introdusca la ruta del archivo correspondiente al año {año_inicial +i}"))
                                i+=1
                            #corregir como meter los archivos
                            for archivo in archivos:
                                datos_año = pd.read_csv(archivo, encoding="iso-8859-1")
                    else:
                        pass
                    
                        pass
                elif datos_nuevos == "A":
                    años=[2008,2009,2010,2011,2012,2013,2014]
                    estimar_actuales=input("Se tienen datos del 2008 al 2014, desea estimar los datos restantes?(S/N)").upper()
                    if estimar_actuales == "S":
                        metodo_estimacon = input("Mediante que metodo desea estimar los datos, estandar(E), Incremento lineal(L)o Incremento algebracico(A) ?").upper()
                        pass
                    elif estimar_actuales == "N":
                        for año in años:
                            datos_año = pd.read_csv(f"Datos _fianzas_{año}.csv", encoding="iso-8859-1")
                elif datos_nuevos == "I":
                    print("se cuentan con datos de los años 2008 al 2014")
                    datos_2008 = pd.read_csv("Datos _fianzas_2008.csv", encoding="iso-8859-1")
                    print("los datos cargados tienen esta forma")
                    datos_2008.head()
                    datos_nuevos=0
                else:
                    datos_nuevos =0
                    print("Selección no reconocida, por favor ingrese N para trabajar con nuevos datos, A para trabajar con los datos actuales o I para obtener información sobre los datos actuales")
        
        elif x == "C" :
            if tipo_usuario == "S":
                datos_servicio=input("Desea usar los datos actuales(A) o cargar nuevos(N)?")
                #Meter cargador de nuevos datos
            unica= input("Su poliza es para un solo ramo(S) o un podructo mixto(M)").upper()
            ramos=[]
            if unica == "S":
                ramos.append(input("para que ramo es su poliza? (ver opciones disponibles con R)"))
            elif unica =="M":
                i=0
                n_ramos= int(input("Cuantos ramos tiene su poliza?"))
                for ramo in range(n_ramos +1):
                    i+=1
                    ramos.append(input(f"Cuales es el ramo {i}"))
            elif unica== "R" or "r":
                #sacar los ramos disponibles en el df
                pass
            MA=int(input("Cual es el monto afianzado?"))
            #Cargar indice o indices
            if tipo_usuario =="U":
                prima_tarifa=calculos(ind,MA)
                guardar =input("Desea guardar el monto en un documento(S/N)?").upper()
                if guardar == "S":
                    #Crear documento y meter la prima de tarifa
                    print(f"Su prima por un monto asegurado de ${MA} es de {prima_tarifa}, esto representa un {prima_tarifa/MA}% ")
        else:
            x=0 ## Meter un interruptor para este while
            tipo_usuario=0
            intentos+=1
            print("Selección no reconocida, por favor ingrese N para nota tecnica o C para realizar los calculos")
    return pass #incluir que nos va a regresar la función
 

def calculos(Ind,Ma,gadmi =.1, gadmi_min= 1000 ,gadq=.15, gadq_min=1500, mutil=.1,mutil_min=1000):
    Prima_Base = Ind*Ma
    m_gadmin=0
    m_gadq =0
    m_uti=0
    #Checar porque no esta tomando los montos minimos
    if gadmi*Prima_Base > gadmi_min:
        m_gadmin= gadmi*Prima_Base
    else:
        m_gadmi = gadmi_min
    if m_gadq*Prima_Base > gadq_min:
        m_gadq= m_gadq*Prima_Base
    else:
        m_gadq=gadq_min
    if m_uti*Prima_Base > mutil_min:
        m_uti=mutil_min
    Prima_Tarifa = Prima_Base + m_gadmin + m_gadq + m_uti
    return Prima_Tarifa