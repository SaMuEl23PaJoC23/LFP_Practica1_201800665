class ReporteHTML():

    def Reporte_HTML(self,reportar):#0-nombreCurso, 1-ArregloEstudiantes(sinModificar), 2-totalAlumnos, 3-listaASC, 4-listaDESC, 5-listaAVG, 6-listaMIN, 7-listaMAX, 8-listaAPR, 9-listaREP
        reporte=open("ReporteWeb.html","w")
        reporte.write("<!DOCTYPE html>\n")
        reporte.write("<html>\n")
        reporte.write("<head>\n")
        reporte.write("<title>Reporte Web</title>\n")
        reporte.write("</head>\n")
        reporte.write("<body background="+"bosque.jpg"+">\n")

        reporte.write("<table align="+"center"+">\n")
        reporte.write("<tr>\n")
        reporte.write("<td bgcolor="+"\"black\""+">\n")
        reporte.write("<h1 align="+"center"+"><font color="+"\"orange\""+">REPORTE DE NOTAS</font></h1>\n")
        reporte.write("</td>\n")
        reporte.write("</tr>\n")
        reporte.write("</table>\n")

        
        reporte.write("<h2 align="+"center"+"><font color="+"white"+">Total de alumnos: "+str(reportar[2])+"</font></h2>\n")

        reporte.write("<table bgcolor="+"white"+" align="+"center"+" border="+"2"+">\n")

        reporte.write("<tr align="+"center"+">\n")
        reporte.write("<td bgcolor="+"\"yellow\""+"><b><font size="+"\"4\""+">NOMBRE DEL CURSO: </font></b></td>\n")
        reporte.write("<td><b><font size="+"\"4\""+">"+reportar[0]+" </font></b></td>\n")
        reporte.write("</tr>\n")

        reporte.write("<tr align="+"center"+">\n")
        reporte.write("<td bgcolor="+"\"aqua\""+"><b><font size="+"4"+">Nombre Alumno</font></b></td>\n")
        reporte.write("<td bgcolor="+"\"aquamarine\""+"><b><font size="+"4"+">Nota</font></b></td>\n")
        reporte.write("</tr>\n")

        #Aqui van los alumnos tal y como aparecen en el archivo de entrada
        siguiente=0
        while siguiente != len(reportar[1]):
            reporte.write("<tr align="+"center"+">\n")
            reporte.write("<td>"+reportar[1][siguiente]+"</td>\n")
            if reportar[1][siguiente+1] < 61:
                reporte.write("<td><font color="+"red"+">"+str(reportar[1][siguiente+1])+"</font></td>\n")
            else:
                reporte.write("<td><font color="+"blue"+">"+str(reportar[1][siguiente+1])+"</font></td>\n")
            siguiente+=2
            reporte.write("</tr>\n")
        reporte.write("</table>\n")

        reporte.write("<h3 align="+"center"+"><font color="+"white"+">ORDENAMIENTOS</font></h3>\n")
        siguienteOrdenamiento=3
        while True:
            TipoOrdenamiento=reportar[siguienteOrdenamiento][0]

            if TipoOrdenamiento=="listaASC":    #lista Ascendente
                reporte.write("<table bgcolor="+"white"+" align="+"center"+" border="+"2"+">\n")
                reporte.write("<tr align="+"center"+">\n")
                reporte.write("<td bgcolor="+"\"yellow\""+" colspan="+"2"+"><b><font size="+"4"+">ASCENDENTE</font></b></td>\n")
                reporte.write("</tr>\n")

                reporte.write("<tr align="+"center"+">\n")
                reporte.write("<td bgcolor="+"\"aqua\""+"><b><font size="+"4"+">Nombre Alumno</font></b></td>\n")
                reporte.write("<td bgcolor="+"\"aquamarine\""+"><b><font size="+"4"+">Nota</font></b></td>\n")
                reporte.write("</tr>\n")

                siguiente=1
                while siguiente < len(reportar[siguienteOrdenamiento]):
                    reporte.write("<tr align="+"center"+">\n")
                    reporte.write("<td>"+reportar[siguienteOrdenamiento][siguiente]+"</td>\n")
                    if reportar[siguienteOrdenamiento][siguiente+1] < 61:
                        reporte.write("<td><font color="+"red"+">"+str(reportar[siguienteOrdenamiento][siguiente+1])+"</font></td>\n")
                    else:
                        reporte.write("<td><font color="+"blue"+">"+str(reportar[siguienteOrdenamiento][siguiente+1])+"</font></td>\n")
                    siguiente+=2
                    reporte.write("</tr>\n")
                reporte.write("</table>\n")

            elif TipoOrdenamiento=="listaDESC": #Lista Descendente
                reporte.write("<table bgcolor="+"white"+" align="+"center"+" border="+"2"+">\n")
                reporte.write("<tr align="+"center"+">\n")
                reporte.write("<td bgcolor="+"\"yellow\""+" colspan="+"2"+"><b><font size="+"4"+">DESCENDENTE</font></b></td>\n")
                reporte.write("</tr>\n")

                reporte.write("<tr align="+"center"+">\n")
                reporte.write("<td bgcolor="+"\"aqua\""+"><b><font size="+"4"+">Nombre Alumno</font></b></td>\n")
                reporte.write("<td bgcolor="+"\"aquamarine\""+"><b><font size="+"4"+">Nota</font></b></td>\n")
                reporte.write("</tr>\n")

                siguiente=1
                while siguiente < len(reportar[siguienteOrdenamiento]):
                    reporte.write("<tr align="+"center"+">\n")
                    reporte.write("<td>"+reportar[siguienteOrdenamiento][siguiente]+"</td>\n")
                    if reportar[siguienteOrdenamiento][siguiente+1] < 61:
                        reporte.write("<td><font color="+"red"+">"+str(reportar[siguienteOrdenamiento][siguiente+1])+"</font></td>\n")
                    else:
                        reporte.write("<td><font color="+"blue"+">"+str(reportar[siguienteOrdenamiento][siguiente+1])+"</font></td>\n")
                    siguiente+=2
                    reporte.write("</tr>\n")
                reporte.write("</table>\n")
            
            elif TipoOrdenamiento=="listaAVG": #Lista promedio
                reporte.write("<table bgcolor="+"white"+" align="+"center"+" border="+"2"+">\n")
                reporte.write("<tr align="+"center"+">\n")
                reporte.write("<td bgcolor="+"\"yellow\""+" colspan="+"2"+"><b><font size="+"4"+">PROMEDIO DE NOTAS</font></b></td>\n")
                reporte.write("</tr>\n")

                reporte.write("<tr align="+"center"+">\n")
                reporte.write("<td><b><font size="+"4"+">"+str(reportar[siguienteOrdenamiento][1])+"</font></b></td>\n")
                reporte.write("</tr>\n")

            elif TipoOrdenamiento=="listaMIN": #Lista nota minima
                reporte.write("<table bgcolor="+"white"+" align="+"center"+" border="+"2"+">\n")
                reporte.write("<tr align="+"center"+">\n")
                reporte.write("<td bgcolor="+"\"yellow\""+" colspan="+"2"+"><b><font size="+"4"+">NOTA MINIMA</font></b></td>\n")
                reporte.write("</tr>\n")

                reporte.write("<tr align="+"center"+">\n")
                reporte.write("<td><b><font size="+"4"+">"+str(reportar[siguienteOrdenamiento][1])+"</font></b></td>\n")
                reporte.write("</tr>\n")

            elif TipoOrdenamiento=="listaMAX": #Lista nota maxima
                reporte.write("<table bgcolor="+"white"+" align="+"center"+" border="+"2"+">\n")
                reporte.write("<tr align="+"center"+">\n")
                reporte.write("<td bgcolor="+"\"yellow\""+" colspan="+"2"+"><b><font size="+"4"+">NOTA MAXIMA</font></b></td>\n")
                reporte.write("</tr>\n")

                reporte.write("<tr align="+"center"+">\n")
                reporte.write("<td><b><font size="+"4"+">"+str(reportar[siguienteOrdenamiento][1])+"</font></b></td>\n")
                reporte.write("</tr>\n")

            elif TipoOrdenamiento=="listaAPR": #Lista aprobados
                reporte.write("<table bgcolor="+"white"+" align="+"center"+" border="+"2"+">\n")
                reporte.write("<tr align="+"center"+">\n")
                reporte.write("<td bgcolor="+"\"yellow\""+" colspan="+"2"+"><b><font size="+"4"+">Estudiantes Aprobados</font></b></td>\n")
                reporte.write("</tr>\n")

                reporte.write("<tr align="+"center"+">\n")
                reporte.write("<td><b><font size="+"4"+">"+str(reportar[siguienteOrdenamiento][1])+"</font></b></td>\n")
                reporte.write("</tr>\n")

            elif TipoOrdenamiento=="listaREP": #Lista reprobados
                reporte.write("<table bgcolor="+"white"+" align="+"center"+" border="+"2"+">\n")
                reporte.write("<tr align="+"center"+">\n")
                reporte.write("<td bgcolor="+"\"yellow\""+" colspan="+"2"+"><b><font size="+"4"+">Estudiantes Reprobados</font></b></td>\n")
                reporte.write("</tr>\n")

                reporte.write("<tr align="+"center"+">\n")
                reporte.write("<td><b><font size="+"4"+">"+str(reportar[siguienteOrdenamiento][1])+"</font></b></td>\n")
                reporte.write("</tr>\n")
            
            siguienteOrdenamiento+=1

            if siguienteOrdenamiento == len(reportar):
                break
        reporte.write("</html>\n")
        
        reporte.close()
        