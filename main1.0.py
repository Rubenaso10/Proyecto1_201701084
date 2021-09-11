import os
import easygui as eg

from colorama import init
from colorama import Fore, Back, Style
from graphviz import Digraph
from analizador_menu import delimitadores
from analizador_menu import lexico

import menu_principal


contenido_archivo=[]

init(autoreset = True)


def cargarArchivo():
    global contenido_archivo
    contenido_archivo.clear()
    extension = ["*.py","*.lfp"]

    archivo = eg.fileopenbox(msg="Abrir archivo",title="Control: Practica Lenguajes",default='',filetypes=extension)
    efe = open (archivo,"r",5,"utf-8")                       
    for linea in efe.readlines():
        contenido_archivo.append(linea)
        #print(Fore.RED+linea.rstrip())
        
        #print(datos)
    efe.close()
    delimitadores(contenido_archivo)

    
   
    
   # init(autoreset=True)
    

      
    
def funciones():
    funcion = True
    while funcion:
        
        
        print ( "\t1  -Cargar menú" + " \U0001F4C4")
        print (Fore.LIGHTYELLOW_EX+"\t2 -Cargar orden"+ "\U0001F4E4")
        print (Fore.CYAN +"\t3 -Generar menú"+"  \U0001F37D")
        print (Fore.RED+"\t4 -Generar factura"+ " \U0001F4C7")
        print (Fore.GREEN+"\t5 -Generar árbol"+ " \U0001F333")
        print (Fore.MAGENTA+"\t6 -Salir"+ "\U0001F44B")

        

        opcion = input("Ingrese opcion---->   ")
        if  opcion=="1":
            cargarArchivo()

        elif opcion=="2":
            pass
            
        elif opcion =="3":
            menu_principal.reportar()
        elif opcion =="4":
            pass
        elif opcion =="5":
            pass
        elif opcion == "6":
            break
             
        else:
            print("")
            input("No ha pulsado ninguna opción correcta, pulse enter para regresar al menú principal")
            

funciones()

    
	
	


    