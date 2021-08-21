from io import open
from tkinter import *
from tkinter import filedialog
import time

class Cargar_Archivo():

    def Seleccionar_Archivo(self):
        windowRoot=Tk()
        RutaArchivo=filedialog.askopenfilename(title="Archivo a cargar")
        windowRoot.mainloop()
        if RutaArchivo != "":
            print("\n!!Carga exitosa de archivo...!!\n")
            time.sleep(3)
            return RutaArchivo

        else:
            print("\n>> Archivo no seleccionado <<\n")
            time.sleep(3)
            return ""


    def Cargar_ArchivoLFP(self,ruta):
        archivoLFP=open(ruta)
        TextoArchivo=archivoLFP.readlines()
        archivoLFP.close()

        separar=0
        nuevo=[]
        enviar=[]
        posicion=0

        for linea in TextoArchivo:

            for caracter in linea:
                if "," == caracter:
                    separar+=1

            if separar>1:
                separar=0
                nuevo=linea.split(",")

                for e1 in nuevo:
                    if e1 != "" and e1 !="\n":
                        enviar.append(e1)
                nuevo=[]
            else:
                if "}" in linea:
                    nuevo=linea.split(",")

                    for e1 in nuevo:
                        if e1 != "" and e1 !="\n":
                            enviar.append(e1)
                    nuevo=[]
                enviar.append(linea)
                separar=0        
        
        return enviar