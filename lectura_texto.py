"""Se crea previamente un archivo txt llamado temperatura que contiene:
Ene 13.8
Feb 15.2
Mar 17.4
Abr 21.4
May 24.7
Jun 27.3
Jul 27.9
Ago 27.9
Sep 26.3
Oct 23.7
Nov 19.1
Dic 15  
"""
#Este  programa leera los datos de un archivo txt para despues calcular el proomedio de temperaturas con esos datos


#Abrimos nuestro archivo txt que se guardara en la variable archivo 
archivo= open("temperatura.txt", "r")


#Variable que guardara la suma de las temperaturas
sumaT=0


#Bucle que leera el archivo para la suma
for renglon in archivo:
    datos=renglon.split()       #Separara la lista por meses - temperatura 
    
    mes=datos[0]                #los datos en el espacio [0] se guardaran en mes 

    temperatura=datos[1]       #los datos en el espacio[1] se guardaran en temperatura
    
    palabra= mes + "" + temperatura #en la variable palabra se guardara lo que se genere de mes
                                    #+ "" + lo que se genere en temperatura

    sumaT+=float(temperatura)       #covertimos los datos de temperatura a flotantes 

#cierre de archivo
archivo.close() 

#calcula el promedio 
promedio=sumaT/12

#imprime el resultado
print("El promedio es: ", promedio)

