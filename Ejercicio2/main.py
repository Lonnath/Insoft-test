import array
import random
empresas =["ECOPETROL", "GRUPO-EXITO", "GRUPO-EPM", "ORGANIZACION-TERPEL", "GRUPO-NUTRESA"]
tablaFinal = {}
profesion =["INGENIERO SOFTWARE", "ALBAÑIL", "CONDUCTOR VEHICULO PESADO", "DISEÑADOR GRAFICO", "REDACTOR", "ESTILISTA", "AMA DE CASA"]
nombres = {"Luis", "Juan", "Pedro"," María", "Alberto", "Gabriel", "Oscar", "Carlota", "Ximena", "Patricia"}
apellidos = ["Osorio", "Serna", "Menjura", "Zapata", "Idárraga", "Lara", "Jaramillo", "Zamora", "Ocampo", "Victoria"]
nombresCompletos = []
countPer = 0
countFor = 2
while countFor > 0:
    countFor-=1
    for nombre in nombres:
        count = len(apellidos)-1
        while count > 0:
            tmponombre = nombre +" "+apellidos[count-1]+" "+apellidos[count]
            if tmponombre in nombresCompletos:
                print("AAA")
                for nombreTmp in nombres:
                    tmpNombre = nombre +" "+nombreTmp+" "+apellidos[count-1]+" "+apellidos[count]
                    if tmpNombre not in nombresCompletos:
                        print("ENTRA")
                        nombresCompletos.append(tmpNombre)
                        tablaFinal["identificacion"+str(countPer)] = str(random.randint(600000, 1700000000))
                        tablaFinal["nombre"+str(countPer)]=tmpNombre
                        tablaFinal["empresa"+str(countPer)] = empresas[random.randint(0,4)]
                        tablaFinal["telefono"+str(countPer)] = str(random.randint(3000000000, 4000000000))
                        tablaFinal["profesion"+str(countPer)] = profesion[random.randint(0, 6)]
                        countPer+=1
                        count-=1
            else:  
                nombresCompletos.append(tmponombre)
                tablaFinal["identificacion"+str(countPer)] = str(random.randint(600000, 1700000000))
                tablaFinal["nombre"+str(countPer)]= tmponombre
                tablaFinal["empresa"+str(countPer)] = empresas[random.randint(0,4)]
                tablaFinal["telefono"+str(countPer)] = str(random.randint(3000000000, 4000000000))
                tablaFinal["profesion"+str(countPer)] = profesion[random.randint(0, 6)]
                countPer+=1
                count-=1
for dato in tablaFinal:
   print(dato + " - "+ tablaFinal[dato])