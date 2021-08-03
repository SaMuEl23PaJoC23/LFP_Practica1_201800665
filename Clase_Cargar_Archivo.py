from io import open

class Cargar_Archivo():

    def Cargar_ArchivoLFP(self):
        archivoLFP=open("prueba.lfp")
        texto=archivoLFP.read()
        archivoLFP.close()

        print(texto)