import webbrowser
from os import linesep
import analizador_menu


def reportar():
    #print(analizador_menu.contenido[0])
    report=open("menu_principal.html","w",5,"utf-8")
    report.write(
    "<!DOCTYPE html>"
    +"<html lang=\"en\">"
    +"<head>"
        +"<meta charset=\"UTF-8\">"
        +"<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">"
        +"<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">"
        +"<title>Document</title>"
        +"<h1>"+analizador_menu.contenido[0]+" </h1>"
        +"<style>"
            +"h1 { color: #f1f1ee;"
                +"opacity: 0.5; "
                +"font-style: oblique;"
                +"text-align: center;}"
        +"</style>"

        

        
    +"</head>"

    +"<body background=\"imagen1.jpg\"></body>"
    +"<body>")
    for x in analizador_menu.contenido[1]:

        report.write(

            "<h1>"+str(x.seccion)+"</h1>")
        for y in x.productos:
            report.write(
                "<table  align =\"center\">"
                    

                    +"<tbody style =\"background: #1e779b;opacity:0.6\">"
                    
                    
                    +"<tr>"
                    + "<td> "+str(y[1])+"</td>"
                        +"<td>"+str(y[2])+" </td>"
                        
                    +"</tr>"
                    +"<tr>"
                        +"<td>"+str(y[3])+" </td>"
                        
                        
                    +"</tr>"



                    +"</tbody>"
                +"</table>")

    report.write(
    "</body>"
    +"</html>"
    
    )
    webbrowser.open("menu_principal.html")
    
