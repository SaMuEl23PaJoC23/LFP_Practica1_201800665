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
            print("\n!!Carga exitosa de archivo...!!")
            time.sleep(2)
            return RutaArchivo

        else:
            print(">> Archivo no seleccionado <<")
            time.sleep(2)
            return ""


    def Cargar_ArchivoLFP(self,ruta):
        archivoLFP=open(ruta)
        texto=archivoLFP.read()
        archivoLFP.close()

        print(texto)