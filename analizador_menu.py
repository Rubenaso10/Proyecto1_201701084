from graphviz import Digraph
from reportar_tokens import reportar
import copy
#from reportar_errores import reportar

class error_lexico ():
    def __init__ (self,numero_error,fila,columna,caracter, descripcion ):
        self.numero_error=numero_error
        self.fila =fila
        self.columna = columna
        self.caracter = caracter
        self.descripcion = descripcion

class tabla_tokens ():
    def __init__ (self,numero,lexema,fila,columna,token):
        self.numero=numero
        self.lexema = lexema
        self.fila = fila
        self.columna = columna
        self.token = token
        
class menu():
    def __init__(self,seccion,productos):
        self.seccion=seccion
        self.productos= productos


contenido=[]
lista_grafica=[] #para poder graficar
lista_errores=[] #manejar errores
contador_errores = 0 #manejar errores  
contador_tokens=0 #manejar tokens

lista_tokens=[]
lista_delimitadores = ["=",":","[","]",";","\'"]

def delimitadores(contenido_archivo):
    
    global contenido
    contenido.clear()
    global contador_errores
    global contador_tokens
    contador_filas =0
    
    for linea in contenido_archivo:
         cIndex = 0
         contador_filas+= 1     
         concatena=""
         line =linea.rstrip()
         cierre = False

         if linea != "\n":
            
            #dentro de un while cIndex < archivo:
            while cIndex < len(line):

            #Capturar el caracter 
                character = line[cIndex]
                if cierre==False:

            #Validacion (If) si el caracter es delimitador o caracter is space () 
                    if character in lista_delimitadores or character.isspace():
                    #Validar si hay elementos en concatena ( len el tamñao)
                        if len(concatena) >0:
                        #(Si hay enviar al analizador lexico)
                                
                            valido, tipo = lexico(concatena)

                            #if valido agregar tabla tokens
                            if valido:
                                contador_tokens+=1
                                token = tabla_tokens(contador_tokens,concatena,contador_filas,cIndex-1,tipo)    
                                lista_tokens.append(token)
                                
                            #else tabla errores 
                            else:
                                contador_errores+=1
                                error = error_lexico(contador_errores,contador_filas,cIndex-1,concatena,tipo)
                                lista_errores.append(error)
                                
                            #limpiar concatena
                            concatena = ""
                        if character == "\'":
                            cierre = True



                        #Enviar al analizador lexico el caracter
                        elif not character.isspace():
                            valido, tipo = lexico(character)

                            #if valido agregar tabla tokens
                            if valido:
                                contador_tokens+=1
                                token = tabla_tokens(contador_tokens,character,contador_filas,cIndex,tipo)    
                                lista_tokens.append(token)
                            #else tabla errores 
                            else:
                                contador_errores+=1
                                error = error_lexico(contador_errores,contador_filas,cIndex,character,tipo)
                                lista_errores.append(error)
                        cIndex+=1 
                #else: para concatenar
                    else:
                        concatena += character
                        cIndex+=1
                else:
                    if character=="\'":
                        contador_tokens+=1
                        token = tabla_tokens(contador_tokens,concatena,contador_filas,cIndex,"cadena" )   
                        lista_tokens.append(token)
                        cierre =False
                        concatena=""
                    else:
                        concatena+= character
                    cIndex+=1
    analizador(lista_tokens)  
  
    # print("estoy vivo",contenido[0])                 
    # for x in contenido[1]:
    #     print(x.seccion)  
              
    reportar(lista_tokens)
    reportar(lista_errores)
    # for x in lista_tokens:
    #     print (x.numero,x.lexema,x.fila,x.columna,x.token)   
    # print()
    # for y in lista_errores:
    #     print(y.numero_error,y.fila, y.columna, y.caracter, y.descripcion)


def lexico(palabra):
    estado_actual=0 # se queda


    cIndx = 0 #se queda

    Limit = len (palabra)#se queda

    token = ""

    while True:
        
        character = palabra[cIndx] #Se captura el caracter segun el contador de columna
        if estado_actual==0:
            #concatena ="" # limpia la variable concatena
            if character.isalpha():
                #concatena += character
                token = "identificador"
                estado_actual=1
                cIndx+=1
            elif character == ":" or character =="=" or character =="[" or character =="]" or character ==";":
                #contenido.append([character,"sym"])
                #cIndx +=1
                if character == ":":
                    return True, "dos puntos"
                if character == "=":
                    return True, "signo igual"
                if character == "[":
                    return True, "corchete de apertura"
                if character == "]":
                    return True, "corchete de cierre"
                if character == ";":
                    return True, "punto y coma"
                    
            elif character.isdigit():
                token="numero"
                #concatena += character
                estado_actual = 5
                cIndx+=1
            elif character== "\'":
                #concatena += character
                token="cadena"
                estado_actual= 2
                cIndx+=1
            else:
                cIndx +=1
                return False, "Caracter invalido "
                # error = errores(contador_errores,cIndx,character,"Caracter no válido")
                
                # lista_errores.append(error) # para usarlo en los errores 
                



        elif estado_actual ==1:
            if character.isalpha() or character.isdigit() or character=="_":
                
                #concatena += character
            
                cIndx+=1
                
            else:
                #contenido.append([concatena,"id"])
                estado_actual=0
                return False, "Identificador invalido "

        elif estado_actual== 5:
            if character.isdigit():
                #concatena += character
                cIndx+=1
            elif character==".":
                #concatena +=character
                estado_actual=6
                cIndx+=1


            else: #para usar en los errores
                cIndx +=1
                #error = errores(contador_errores,cIndx,character,"Caracter no válido")
                
                #lista_errores.append(error) # para usarlo en los errores 
                estado_actual=0
                return False, "Numero invalido "
        elif estado_actual ==6:
            
            if character.isdigit():
                #concatena += character
                cIndx +=1
            else:
                
                #contenido.append([concatena,"num"])
                estado_actual=0 
                return False, "Numero invalido "   
                # NO SE AUMENTO CON CINDX +=1 PORQUE SE IGNORA EL ELEMENTO QUE SE ESTA COMPARANDO EN ESTE ESTADO
        elif estado_actual == 2:
            if character== "\'":
                #concatena += character
                cIndx +=1
                #contenido.append([concatena,"str"])
                estado_actual=0
                #concatena =""
                return True,"cadena" 
            else:
                #concatena += character
                cIndx +=1
                
        
        if cIndx ==Limit:
            if estado_actual ==2:
                #contenido.append(concatena)
                return False , "cadena invalida"
            else:
                return True,token               
            break



#delimitadores("C:\\Users\\Rubenaso10\\Desktop\\[LFP]Tarea2_201701084\\entrada_tarea3.txt")
# def graficar ():
    
#      contador = 0
    
#      grafo = Digraph(format='png', name='Grafo')
#      grafo.attr(rankdir='TB', size='8,5')

#      grafo.node(str(contador+1))
#      contador+=1

#      for n in lista_tokens:
#          if n.tipo == "identificador":
#             grafo.node(str(contador+1),n)
        
#          grafo.edge(str(1),str(contador+1))
#          contador+=1
        
        

#      grafo.render(view=True)
    

#dirArchivo = input(" ::: Ingresa la ruta: ")
#lexico(dirArchivo)
#for x in contenido:
 #  print(x)
#print(contenido)
def analizador(tokens):
    restaurante_seccion=[]
    
    productos=[]
    objeto_temporal = None

    variable="" #variable para graficar
    lista_graficar=[] #lista que ira tomando valores y despues se usara para graficar
    ronda =0
    cIndx =0
    contador_secciones=0 # contador para guardar secciones en lista_graficar
    global contenido
    while True:
       # print(cIndx,ronda)
        if ronda == 0:
           # print(tokens[cIndx].token)
            if  tokens[cIndx].token=="cadena" :
                
                ronda=4
                cIndx+=1
            elif tokens[cIndx].token=="corchete de apertura":
                ronda = 6
                cIndx +=1
                print()
            elif tokens [cIndx].token=="identificador":
                ronda = 1
                cIndx +=1
        elif ronda == 1:
            if tokens[cIndx].token=="signo igual":
                ronda=2
                cIndx+=1
        elif ronda == 4:
            if tokens[cIndx].token=="dos puntos":
                if objeto_temporal != None:

                    restaurante_seccion.append(copy.deepcopy(objeto_temporal))
                    objeto_temporal=None
                #secciones.append(tokens [cIndx-1].lexema)
                objeto_temporal= menu(tokens [cIndx-1].lexema,[])
                #print("Nombre de sección---->"+ tokens [cIndx-1].lexema  )
                
                #lista_graficar.append(tokens [cIndx-1].lexema) # lista para graficar nodos 
                
                ronda=0
                cIndx+=1
        
        elif ronda == 6:
            if tokens [cIndx].token=="identificador":
                productos.append(tokens[cIndx].lexema)
                #print("Identificador---->"+ tokens[cIndx].lexema)
            ronda = 7
            cIndx+=2

        elif ronda ==7:
            #print("ronda serresiete")
            if tokens[cIndx].token=="cadena":
                productos.append(tokens[cIndx].lexema)
                #print("nombre--->"+tokens[cIndx].lexema)
            ronda =8
            cIndx+=2
        
        elif ronda ==8:
            if tokens [cIndx].token=="numero":
                productos.append("{0:.2f}".format(float(tokens [cIndx].lexema)))
                #print ("precio--->","{0:.2f}".format(float(tokens [cIndx].lexema)))
            ronda =9
            cIndx +=2

        elif ronda == 9:
            #print("ronda noeve")
            if tokens [cIndx].token == "cadena":
                productos.append(tokens[cIndx].lexema)
                objeto_temporal.productos.append(productos.copy())
                productos.clear()

               # print("descripción--->"+tokens[cIndx].lexema)
            ronda =0
            cIndx +=2

        elif ronda ==2:
            #print("ronda 2")
            if tokens [cIndx].token== "cadena":
                contenido.append(tokens[cIndx].lexema)
                #print("Nombre de restaurante--->"+ tokens[cIndx].lexema)
                variable= tokens[cIndx].lexema #para graficar
                #print(variable) #Para graficar
            cIndx +=1
            ronda=0
        
        if cIndx == len(tokens):
            break
    if objeto_temporal != None:

        restaurante_seccion.append(copy.deepcopy(objeto_temporal))
        objeto_temporal=None
    contenido.append(restaurante_seccion)
#    graficar(variable,lista_graficar)   

#analizador()












    







#numeroT ="11."
#numeroD = float(numeroT)
#print ("{0:.2f}".format(numeroD))
                
                    