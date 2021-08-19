from Clase_Cargar_Archivo import Cargar_Archivo
from Clase_Mostrar import Mostrar_En_Consola
from Clase_ReporteHTML import ReporteHTML
import webbrowser as wb
import time
opcion=0

ProcesosArchivo=Cargar_Archivo()
Mostrar=Mostrar_En_Consola()
GenerarReporte=ReporteHTML()
DatosReportar=""
rutaArchivo=""
while opcion != 4:
    try:
        print("[----------------MENU----------------]")
        print("1). Cargar archivo")
        print("2). Mostrar reporte en consola")
        print("3). Exportar reporte")
        print("4). salir")
        opcion=int(input("opcion:"))
        print("[------------------------------------]")

        if opcion == 1:
            rutaArchivo=ProcesosArchivo.Seleccionar_Archivo()
            if rutaArchivo != "":
                Texto=ProcesosArchivo.Cargar_ArchivoLFP(rutaArchivo)
        elif opcion == 2:
            if rutaArchivo != "":
                print("\n>> Procesando Archivo...<<\n")
                time.sleep(3)
                DatosReportar=Mostrar.Mostrar_Reporte(Texto)
                time.sleep(3)
            else:
                DatosReportar=""
                print("\n>> Primero debe seleccionar un archivo<<\n")
                time.sleep(3)

        elif opcion == 3:
            if DatosReportar != "":
                GenerarReporte.Reporte_HTML(DatosReportar)
                print("\n>> Archivo generado exitosamente<<\n")
                time.sleep(3)
                wb.open_new("ReporteWeb.html")
            else:
                print("\n>> Primero debe mostrar el reporte en -consola- <<\n")
                time.sleep(3)
    except SyntaxError:
        print(">> !! Solo numeros !! <<")
    
print("finalizado...")