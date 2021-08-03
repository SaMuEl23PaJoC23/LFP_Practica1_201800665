from Clase_Cargar_Archivo import Cargar_Archivo
opcion=0

CargarArchivo=Cargar_Archivo()

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
            print("archivo cargado: \n")
            CargarArchivo.Cargar_ArchivoLFP()

        elif opcion ==2:
            print("entro 2")

        elif opcion ==3:
            print("entro 3")
    except ValueError:
        print(">> !! Solo numeros ...!! <<")
    
print("finalizado...")