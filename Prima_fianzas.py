import math
import numpy as np
import pdb
import pandas as pd
import datetime

#DataFrame con datos maestros 
file_2008=pd.read_csv("Datos_fianzas_2008.csv", encoding="iso-8859-1",skiprows=1)
file_2009=pd.read_csv("Datos_fianzas_2009.csv", encoding="iso-8859-1",skiprows=1)
file_2010=pd.read_csv("Datos_fianzas_2010.csv", encoding="iso-8859-1",skiprows=1)
file_2011=pd.read_csv("Datos_fianzas_2011.csv", encoding="iso-8859-1",skiprows=1)
file_2012=pd.read_csv("Datos_fianzas_2012.csv", encoding="iso-8859-1",skiprows=1)
file_2013=pd.read_csv("Datos_fianzas_2013.csv", encoding="iso-8859-1",skiprows=1)
file_2014=pd.read_csv("Datos_fianzas_2014.csv", encoding="iso-8859-1",skiprows=1)

#Separación de los Ramos para incluirlos como indices del DataFrame maestro
ramos_final=[]
ramos=[file_2008["Ramos"]]
previo=ramos.pop()
for i in range(18):
    ramos_final.append(previo[i])

#Separación de los indices para agruparlos en un DataFrame maestro
indi_2008=[file_2008["Indice"]]
indices_2008=[]
for i in range(18):
    ind=file_2008.loc[i,"Indice"]
    ind=ind.replace("%","")
    ind=ind.replace("-","0")
    indices_2008.append(float(ind)/100)
    
indi_2009=[file_2009["Indice"]]
indices_2009=[]
for i in range(18):
    ind=file_2009.loc[i,"Indice"]
    ind=ind.replace("%","")
    ind=ind.replace("-","0")
    indices_2009.append(float(ind)/100)

indi_2010=[file_2010["Indice"]]
indices_2010=[]
for i in range(18):
    ind=file_2010.loc[i,"Indice"]
    ind=ind.replace("%","")
    ind=ind.replace("-","0")
    indices_2010.append(float(ind)/100)
    
indi_2011=[file_2011["Indice"]]
indices_2011=[]
for i in range(18):
    ind=file_2011.loc[i,"Indice"]
    ind=ind.replace("%","")
    ind=ind.replace("-","0")
    indices_2011.append(float(ind)/100)
    
indi_2012=[file_2012["Indice"]]
indices_2012=[]
for i in range(18):
    ind=file_2012.loc[i,"Indice"]
    ind=ind.replace("%","")
    ind=ind.replace("-","0")
    indices_2012.append(float(ind)/100)
    
indi_2013=[file_2013["Indice"]]
indices_2013=[]
for i in range(18):
    ind=file_2013.loc[i,"Indice"]
    ind=ind.replace("%","")
    ind=ind.replace("-","0")
    indices_2013.append(float(ind)/100)
    
indi_2014=[file_2014["Indice"]]
indices_2014=[]
for i in range(18):
    ind=file_2014.loc[i,"Indice"]
    ind=ind.replace("%","")
    ind=ind.replace("-","0")
    indices_2014.append(float(ind)/100)
#Creación de DataFrame maestro

datos_maestros=pd.DataFrame({"2008":indices_2008,"2009": indices_2009, "2010":indices_2010, "2011":indices_2011, "2012":indices_2012, "2013":indices_2013, "2014":indices_2014}, index=ramos_final)

##Guardamos DataFrame como un archivo csv
datos_maestros.to_csv("Datos_fianzas_agregados.csv", sep=',')

def intentos(pregunta,opcion1,opcino2):
    contador =0
    tope=4
    valido=8
    while contador <tope:
        variable=input(pregunta).upper()
        if variable !=opcion1 and variable!=opcino2:
            print("Opción invalida")
            contador +=1
        else:
            contador=8
    if contador ==8:
        return variable
    else:
        raise ValueError("Opción invalida, número de intentos excedidos")
    
##Creación de funciónes auxiliares
def calculos(Ind,Ma,gadmi =.1, gadmi_min= 1000 ,gadq=.15, gadq_min=1500, mutil=.1,mutil_min=1000):
    Prima_Base = Ind*Ma
    m_gadmin=0
    m_gadq =0
    m_uti=0
    #pdb.set_trace()
    #Checar porque no esta tomando los montos minimos
    if gadmi*Prima_Base > gadmi_min:
        m_gadmin= gadmi*Prima_Base
    else:
        m_gadmi = gadmi_min
    if gadq*Prima_Base > gadq_min:
        m_gadq= gadq*Prima_Base
    else:
        m_gadq=gadq_min
    if mutil*Prima_Base > mutil_min:
        m_uti=mutil*Prima_Base
    else:
        m_uti=mutil_min
    Prima_Tarifa = Prima_Base + m_gadmin + m_gadq + m_uti
    return Prima_Tarifa

#Función que calcula el promedio de una lista
def prom_lista(ls):
    if type(ls)!= "list":
        raise ValueError("Esta función solo está definida para listas")
    n=len(ls)
    suma=sum(ls)
    mean=suma/n
    return mean

#Función que verifica la ortografía de los ramos escritos
def verificar(ramos):
    for ramo in ramos:
        for ramo_fin in ramos_final:
            ramo_prueba=ramo_fin.lower()
            if ramo.lower() ==ramo_prueba:
                ramos.remove(ramo)
                ramos.append(ramo_fin)
    return ramos

#Función que cambia como estan escritos los ramos para que coincidan totalmente con los indices del DataFrame
def corrección(ramos):
    iniciales=["fide","indi","cole","judi", "pena","no p","que ","admi","de o","de p","fisc","de a","cred","de s","de c","fina","otra"]
    ramos_prev=[]
    while len(ramos)>0:
        for ramo in ramos:
            for ini in iniciales:
                if ramo[0:4].lower()== ini:
                    ramos.remove(ramo)
                    ramos_prev.append(ini)
            if ramo in ramos:
                ramos.remove(ramo)
    for i in range(len(iniciales)):
        for ramo in range(len(ramos_prev)):
            if iniciales[i] in ramos_prev:
                ramos_prev.remove(iniciales[i])
                ramos_prev.append(ramos_final[i])
    ramos=ramos_prev
    return ramos

#Función en la cual se piden todos los inputs que se necesitas para calcular la Prima
def inputs():
    acc=0
    tipo_usuario=0
    datos_nuevos=0
    unica=0
    n_ramos=0
    año_inicial=0
    now = datetime.datetime.now()
    año_final=now.year
    año_final_datos=0
    diferencia=0
    estimar=0
    años=0
    MA=0
    ramos=[]
    archivos=[]
    incremento=0
    método_de_estimación=0
    tasa=0
    gadmin=0
    gadmin_min=0
    gadq=0
    gadq_min=0
    mutil=0
    mutil_min=0
    valores_prima=0
    guardar=0
    ruta_archivo=0

    tipo_usuario=intentos("Usuario final(U) o prestador de servicio(S)?","U","S")
    if tipo_usuario =="S":
        datos_nuevos=intentos("Desea introducir nuevos datos(N) o trabajar con los actuales(A)?","N","A")
    unica = intentos("Su poliza es para un solo ramo(S) o un podructo mixto(M)","S","M")
    if unica == "S":
        check=True
        while check==True:
            check= False
            ramos.append(input("para que ramo es su poliza? (ver opciones disponibles con R)"))
            if ramos[0]=="R" or ramos[0]== "r":
                print(f"Los ramos disponibles son {ramos_final}")
                ramos=[]
                check=True
    elif unica =="M":
        i=0
        n_ramos= int(input("Cuantos ramos tiene su poliza? "))
        for ramo in range(n_ramos):
            i+=1
            ramos.append(input(f"Cuales es el ramo {i} "))
    MA=int(input("Cual es el monto afianzado?"))
    if datos_nuevos=="N":
        print("Los archivos a cargar deben de estar en formato csv")
        año_inicial= int(input("Cual es el primer año para el cual desea cargar los datos?"))
        año_final_datos= int(input("Cual es el ultimo año para el cual desea cargar los datos?"))
        diferencia = año_final-año_final_datos
        if diferencia != 0:
            estimar= intentos(f"Desea estimar datos para los {diferencia} años faltantes?(S/N)","S","N")
            if estimar == "S":
                método_de_estimación= input("Mediante que metodo desea estimar los datos, estandar(E), Incremento lineal(L)o Incremento algebracico(A) ?").upper() 
                if método_de_estimación =="I":
                    incremento= input("Desea conservar la tendencia del incremento en los datos(C) o introducir un incremento(I)?").upper()
                    if incremento == "I":
                        porcentaje=float(input("introduzca incremento en porcentaje(solo el número)"))
                        tasa=porcentaje/100
                if método_de_estimación =="A":
                    tasa =float(input("A qué tasa desea que incrementen sus indicadores(solo números)?"))
        años = año_final_datos-año_inicial
        for año in range(años+1):
            i=0
            archivos.append(input(f"Introdusca la ruta del archivo correspondiente al año {año_inicial +i}"))
            i+=1
    if datos_nuevos =="A":
        diferencia =año_final-2014
        if diferencia >0:
            estimar=intentos("Se tienen datos del 2008 al 2014, desea estimar los datos para los años futuros faltantes?(S/N)","S","N")
            if estimar=="S":
                método_de_estimación= input("Mediante que metodo desea estimar los datos, estandar(E), Incremento lineal(L)o Incremento algebracico(A) ?").upper() 
                if método_de_estimación =="L":
                    incremento= input("Desea conservar la tendencia del incremento en los datos(C) o introducir un incremento(I)?").upper()
                    if incremento == "I":
                        porcentaje=float(input("introduzca incremento en porcentaje"))
                        tasa=porcentaje/100
                if método_de_estimación =="A":
                    tasa =float(input("A qué tasa desea que incrementen sus indicadores?"))
    if tipo_usuario=="S":
        valores_prima=intentos("Desea usar los valores estandar para el calculo de la prima(E) o usar distintos(D)?","E","D")
        if valores_prima=="D":
            gadmin=float(input("Introdusca el porcentaje correspondiente a gastos de administración (solo números en decimales)"))
            gadmin_min=float(input("Introdusca monto minimo correspondiente a gastos de administración "))
            gadq=float(input("Introdusca el porcentaje correspondiente a gastos de adquisición (solo números en decimales)"))
            gadq_min=float(input("Introdusca el monto minimo correspondiente a gastos de adquisición "))
            mutil=float(input("Introdusca el porcentaje correspondiente a utilidades (solo números en decimales)"))
            mutil_min=float(input("Introdusca el monto minimo correspondiente a utilidades "))
    ramos=corrección(ramos)
    diccionario={"tipo_usuario": tipo_usuario, "datos_nuevos":datos_nuevos,"ramos": ramos, "MA":MA, 
                 "año_inicial": año_inicial,"año_final": año_final, "año_final_datos" :año_final_datos,
                 "diferencia":diferencia,"archivos" :archivos, "estimar":estimar,"método_de_estimación":método_de_estimación,
                 "incremento":incremento,"tasa":tasa, "valores_prima":valores_prima,"gadmin":gadmin,"gadmin_min":gadmin_min,
                 "gadq":gadq,"gadq_min":gadq_min,"mutil":mutil,"mutil_min":mutil_min} 
    return diccionario

##Función principal que calcula la priba basado en los inputs dados

def Prima_fianzas():
    """
    Calcula una prima de tarifa para una fianza, dando la opción de meter todos los parámetros
    e inclusó los archivos estadisticos.

    Parameters
    ----------
    No usa ningún parametro pues todos los pide al usuario

    Returns
    -------
    Regresa la prima de tarifa de la fianza especificada
    """
    
    variables=inputs()
    datos=datos_maestros
    indices_usuario=[]
    indice=0
    if variables["tipo_usuario"]=="U":
        for i in range(len(variables["ramos"])):
            indices_usuario.append(datos.loc[variables["ramos"][i]].mean())
        indice=sum(indices_usuario)
        Prima=calculos(indice,variables["MA"])
        porcentaje= Prima/variables["MA"]
        return (f"Su prima es de ${Prima}, lo que representa un {porcentaje}% de su monto afianzado"), Prima
    if variables["tipo_usuario"]=="S":
        if variables["datos_nuevos"]=="N":
            cargador_archivos_csv(variables["archivos"])
    ramos=variables["ramos"]
    if variables["estimar"]=="N":
        for i in range(len(variables["ramos"])):
            indices_usuario.append(datos.loc[variables["ramos"][i]].mean())
        indice=sum(indices_usuario)    
    if variables["estimar"]=="S":
        if variables["método_de_estimación"]=="E":
            indices_usuario=[]
            desviaciones=[]
            for i in range(len(variables["ramos"])):
                indices_usuario.append(datos.loc[variables["ramos"][i]].mean())
                desviaciones.append(datos.loc[variables["ramos"][i]].std())
            indice=sum(indices_usuario)+2*sum(desviaciones)  ##datos estimados
        elif variables["método_de_estimación"]=="L":
            if variables["incremento"]=="C":
                indices_usuario=[]
                tasa=(((datos.loc["Fidelidad","2014"]-datos.loc["Fidelidad","2008"])/5)/datos.loc["Fidelidad","2008"])
                for i in range(len(variables["ramos"])):
                    indices_usuario.append(datos.loc[variables["ramos"][i]].mean())
                indice=sum(indices_usuario)*((1+tasa)**variables["diferencia"])
            else:
                tasa=variables["tasa"]
                indices_usuario=[]
                for i in range(len(variables["ramos"])):
                    indices_usuario.append(datos.loc[variables["ramos"][i]].mean())
                indice=sum(indices_usuario)*((1+tasa)**variables["diferencia"])
        elif variables["método_de_estimación"]=="A":
            tasa=variables["tasa"]
            indices_usuario=[]
            for i in range(len(variables["ramos"])):
                indices_usuario.append(datos.loc[variables["ramos"][i]].mean())
            indice=sum(indices_usuario)*(tasa*variables["diferencia"])
    
    if variables["valores_prima"]=="E":
        Prima=calculos(indice,variables["MA"])
        porcentaje=Prima/variables["MA"]
        
    elif variables["valores_prima"]=="D":
        Prima=calculos(indice,variables["MA"],variables["gadmin"],variables["gadmin_min"],variables["gadq"],variables["gadq_min"],variables["mutil"],variables["mutil_min"])
        porcentaje=Prima/variables["MA"]
        
    return (f"Su prima es de ${Prima}, lo que representa un {porcentaje} % de su monto afianzado"), Prima
                

