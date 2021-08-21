class Mostrar_En_Consola():

#----para el metodo quicksort-------
    def particion(self,notas):
        pivote = notas[0]
        menores=[]
        mayores=[]
        for i in range(1, len(notas)):
            if notas[i] < pivote:
                menores.append(notas[i])
            else:
                mayores.append(notas[i])

        return menores, pivote, mayores

    def quicksort(self,notas):
        if len(notas)< 2:
            return notas
        menores, pivote, mayores = self.particion(notas)

        return self.quicksort(menores) + [pivote] + self.quicksort(mayores)

#----------------------------------


    def Mostrar_Reporte(self,Texto):
        TextoArchivo=Texto
        nombreCurso=""
        siguienteLinea=0
        banderaCurso=False
        banderaAlumnos=False
        alumnos=[]
        Reportar=[]

        CantOrden=0
        for i in TextoArchivo:
            if ">" not in i:
                CantOrden+=1

        while siguienteLinea < len(TextoArchivo):  #Se extre el nombre del curso del arreglo llamado TextoArchivo
            if banderaCurso==False:
                nombreCurso=TextoArchivo[0]
                nombreCurso=nombreCurso.replace("=","")
                nombreCurso=nombreCurso.replace("{","")
                nombreCurso=nombreCurso.replace("\n","")
                nombreCurso=nombreCurso.replace(" ","")
                banderaCurso=True
                Reportar.append(nombreCurso)   #Se agrega el nombre a la lista Reportar
            
            elif banderaAlumnos == False and siguienteLinea > 0:
                completo1=False
                siguienteLetra=0
                alumno=""
                insertarGuion=False

                while True:
                    if TextoArchivo[siguienteLinea][siguienteLetra] != "\t" and TextoArchivo[siguienteLinea][siguienteLetra] != "<" and TextoArchivo[siguienteLinea][siguienteLetra] != " " and completo1 == False:
                        while completo1 == False:   #Se extrae cada alumno almacenado en el arreglo TextoArchivo
                            alumno+=TextoArchivo[siguienteLinea][siguienteLetra]                   
                            
                            if " " in alumno and insertarGuion == False:
                                alumno=alumno.replace(" ","_")
                                insertarGuion=True

                            elif ";" in alumno:
                                completo1=True

                            siguienteLetra+=1

                    elif completo1 == True:
                        break

                    else:
                         siguienteLetra+=1

                alumno=alumno.replace("\"","")
                alumno=alumno.replace(";","")
                alumno=alumno.replace(" ","")
                alumnos.append(alumno)  #lista con alumnos

                nota=""
                while ">" not in nota:  #Se extrae las notas de cada alumno
                    nota+=TextoArchivo[siguienteLinea][siguienteLetra]
                    siguienteLetra+=1

                nota=nota.replace(" ","")
                nota=nota.replace(">","")
                alumnos.append(float(nota)) #Lista con notas

                if siguienteLinea == len(TextoArchivo)-CantOrden:
                    banderaAlumnos=True   

            else:
                Reportar.append(alumnos)   #Se agrega los alumnos y sus notas al arreglo Reportar
                ordenamientos=[]
                siguienteLetra=0
                completo2=False
                paso=0

                #TextoArchivo[-1]=TextoArchivo[-1].replace("}","")
                

                """while completo2 == False: 
                    completo3=False
                    ordenamiento=""
                    while completo3==False:
                        ordenamiento+=TextoArchivo[siguienteLinea][siguienteLetra]
                        siguienteLetra+=1
                        paso+=1
                        
                        if "," in ordenamiento or paso==len(TextoArchivo[-1]):
                            completo3=True
                    ordenamiento=ordenamiento.replace(" ","")
                    ordenamiento=ordenamiento.replace(",","")
                    ordenamientos.append(ordenamiento)  #lista de ordenamientos

                    if paso==len(TextoArchivo[-1]):
                        completo2=True"""
                while True:

                    if siguienteLinea != len(TextoArchivo):
                        ordenamiento=TextoArchivo[siguienteLinea]
                        ordenamiento=ordenamiento.replace(" ","")
                        ordenamiento=ordenamiento.replace("}","")
                        ordenamiento=ordenamiento.replace("\t","")
                        if ordenamiento not in ordenamientos:
                            ordenamientos.append(ordenamiento)
                        siguienteLinea+=1
                
                    else:
                        break
                    

            siguienteLinea+=1

#-----------Se extraen solo las notas-------------------
        auxNotas1=[]
        auxNotas2=[]
        alumnosOrdenados=[]
        siguiente=1
        while True:
            auxNotas1.append(alumnos[siguiente])
            siguiente+=2
            if siguiente>= len(alumnos):
                break
        
#--------------Se genera el ordenamiento de nombre y notas con metodo ascendente--------
        auxNotas2=self.quicksort(auxNotas1)

        siguienteAlumno=1
        siguienteNota=0

        while True:
            if alumnos[siguienteAlumno]==auxNotas2[siguienteNota]:   #Se comparan las notas
                if alumnos[siguienteAlumno-1] not in alumnosOrdenados:
                    alumnosOrdenados.append(alumnos[siguienteAlumno-1]) #Se agrega el nombre
                    alumnosOrdenados.append(alumnos[siguienteAlumno])   #Se agrega la nota
                    siguienteNota+=1
                    siguienteAlumno=1
                    if siguienteNota == len(auxNotas2):
                        break
                else:
                    siguienteAlumno+=2
            else:
                siguienteAlumno+=2
#----------------------Para la funcion: Mostrar reporte--------------------------------------------
        print("[---------------REPORTE--------------]")
        
        print("\nNombre del curso: ",nombreCurso)
        totalAlumnos=int(len(alumnosOrdenados)/2)
        print("Cantidad de alumnos:",totalAlumnos)
        Reportar.append(totalAlumnos)

        print("Alumnos pertenecientes al curso")
        print("---------------------------------")
        print("  alumno    -    nota")
        print("------------------------")
        i=0
        j=1
        while True:
            print(j,"). ",alumnos[i]," - ",alumnos[i+1])
            i+=2
            j+=1
            if i >= len(alumnos):
                break
        print("\n")

        for TipoOrden in ordenamientos:
            if TipoOrden=="ASC":
                print("\n\n ordenamiento: ASC - Ascendente")
                print("alumno    -    nota")
                print("------------------------")
                i=0
                listaASC=["listaASC"]
                while True:
                    print(alumnosOrdenados[i]+" - "+str(alumnosOrdenados[i+1]))
                    listaASC.append(alumnosOrdenados[i])
                    listaASC.append(alumnosOrdenados[i+1])                    

                    i+=2
                    if i >= len(alumnosOrdenados):
                        break
                Reportar.append(listaASC)


            elif TipoOrden =="DESC":
                print("\n\n ordenamineto: DESC - Descendente")
                print("alumno    -    nota")
                print("------------------------")
                i=len(alumnosOrdenados)-1
                listaDESC=["listaDESC"]
                while True:
                    print(alumnosOrdenados[i-1]+" - "+str(alumnosOrdenados[i])) 
                    listaDESC.append(alumnosOrdenados[i-1])
                    listaDESC.append(alumnosOrdenados[i])

                    i-=2
                    if i <= 0:
                        break  
                Reportar.append(listaDESC)

            elif TipoOrden == "AVG":
                print("\n\n Tipo: AVG - Promedio de las notas")
                promedio=0
                sumatoria=0
                i=1
                listaAVG=["listaAVG"]
                while True:
                    sumatoria+=alumnosOrdenados[i]
                    i+=2
                    if i>=len(alumnosOrdenados):
                        break
                promedio=round(float(sumatoria/totalAlumnos),2)
                print("El promedio es:",promedio)
                listaAVG.append(promedio)
                Reportar.append(listaAVG)
            
            elif TipoOrden == "MIN":
                print("\n\nTipo: MIN - Nota minima")
                print("Nota minima entre estudiantes: ",alumnosOrdenados[1])
                listaMIN=["listaMIN",alumnosOrdenados[1]]
                Reportar.append(listaMIN)
            
            elif TipoOrden == "MAX":
                print("\n\nTipo: MAX - Nota maxima")
                print("Nota maxima entre estudiantes: ",alumnosOrdenados[-1])
                listaMAX=["listaMAX",alumnosOrdenados[-1]]
                Reportar.append(listaMAX)

            
            elif TipoOrden == "APR":
                print("\n\nTipo: APR - Estudiantes Aprobados")
                CantAprobados=0
                i=1
                listaAPR=["listaAPR"]
                while True:
                    if alumnosOrdenados[i] >= 61:
                        CantAprobados+=1
                    i+=2
                    if i >= len(alumnosOrdenados):
                        break
                print("Cantidad de Estudiantes Aprobados: ", CantAprobados)
                listaAPR.append(CantAprobados)
                Reportar.append(listaAPR)
            
            elif TipoOrden == "REP":
                print("\n\nTipo: REP - Estudiantes Reprobados")
                CantReprobados=0
                i=1
                listaREP=["listaREP"]
                while True:
                    if alumnosOrdenados[i] < 61:
                        CantReprobados+=1
                    i+=2
                    if i >= len(alumnosOrdenados):
                        break
                print("Cantidad de Estudiantes Reprobados: ", CantReprobados)
                listaREP.append(CantReprobados)
                Reportar.append(listaREP)

        print("\n")
        
        return Reportar #Retorna todos los datos a reportar