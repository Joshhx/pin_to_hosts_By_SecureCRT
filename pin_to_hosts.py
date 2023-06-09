# $language = "python"
# $interface = "1.0"
from datetime import datetime
import os

Now = datetime.now()
formatted = Now.strftime("%d%m%Y-%H%M%S")
dir="D:\Pines diarios\Fichero de Pines\/" + formatted + ".txt"
filas = crt.Screen.Rows
ip_source = '0.0.0.0'
gw_source = '192.168.1.1'

circuitos = []

crt.Screen.Synchronous = True

def continuar():
    resp = crt.Dialog.MessageBox( " Deseas continuar con la prueba? "," Prueba de Pines ",32|1)
    if int(resp) == 1:
        return True
        
def listaSedes():
    f = open("D:\Pines diarios\Script pines diarios\equipos", "r")
    if f.mode == 'r':
        fl = f.readlines()
    for x in fl:
        circuitos.append([x for x in x.split(";")])
    f.close()
    return circuitos

crt.Dialog.MessageBox("Se esta iniciando la prueba de pines a todas las sedes..!!! \
                    \n Advertencia: debe estar en bash $ para poder empezar la prueba")
if continuar():
    circuitos=listaSedes()#Funcion para meter a la variable circuitos el File de sedes en un lista
    crt.Screen.Send ("telnet " + ip_source + chr(13))
    crt.Screen.WaitForString("#")
    with open(dir, 'a') as fs:
        for i in range(len(circuitos)):
            crt.Screen.Send("ping " + circuitos[i][0] + " source " + gw_source + repeat 100" + chr(13))
            crt.Screen.WaitForString("mgseb-cecb#")
            cadena = crt.Screen.Get2(filas-1,0,filas-1,120)
            valor1 = cadena.find("min/avg/max =")
            valor2 = cadena.find(" ms")
            if valor1 == 0:
                captura1 = "KO"
            else:
                valor3 = (valor1+14)
                valor4 = (valor2 - valor3)
                captura1 = cadena[valor3:valor2]
                captura1 = captura1.replace("/",";")
            res=""      
            for j in range (len(circuitos[i])):
                if j <4:
                    res += circuitos[i][j]+";"
                else:
                    res+=str(captura1+"\n")
            fs.write(res)
    fs.close()
    preg = crt.Dialog.MessageBox( " Quieres abrir la carpeta "," La ejecucion de Pines ha finalizado correctamente...!!! ",32|1)
    if int(preg) == 1:
        os.startfile("D:\Pines diarios\Fichero de Pines\/")
    crt.Screen.Send ("exit"+chr(13))
    
else:
    crt.Dialog.MessageBox("Se ha cancelado la ejecucion del script...!!")
