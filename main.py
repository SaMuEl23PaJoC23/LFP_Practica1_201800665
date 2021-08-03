from Clase_Cargar_Archivo import Cargar_Archivo
opcion=0

ProcesosArchivo=Cargar_Archivo()

while opcion != 4:
    try:
        print("[-------------------------]")
        print("1). Cargar archivo")
        print("2). Mostrar reporte en consola")
        print("3). Exportar reporte")
        print("4). salir")
        opcion=int(input("opcion:"))
        print("[-------------------------]")

        if opcion == 1:
            
            rutaArchivo=ProcesosArchivo.Seleccionar_Archivo()
            ProcesosArchivo.Cargar_ArchivoLFP(rutaArchivo)

        elif opcion ==2:
            print("entro 2")

        elif opcion ==3:
            print("entro 3")
    except ValueError:
        print(">> !! Solo numeros ...!! <<")
    
print("finalizado...")