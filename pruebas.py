import csv
import datetime

from presupuesto import Presupuesto
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from  tkinter.messagebox import *

import tkinter as tk
import tkinter.ttk as ttk



#1 Crear la app
#2 itulo de la app
#3. en formato de cadena, indica las dimensiones
#4. tamaño minimo y maximo de la ventana
#5 tamaño de filas y columnas
#6. crea los tabs (4: encuesta, entrevista, grupo focal, resumen)
#7 crea el objeto presupuesto, instancia la clase presupuesto
#8 variables iniciales para que  los elementos de la clase presupuesto entrevista, grupo focal y encuesta sean false 
#9 funciones inciales: que cuando el valor del borton sea 0, entrevista, grupo focal o encuesta sean false
#10 crea botonos para añadir los botones que activan o desactivan encuestas, entrevistas y grupos focales
#11  tab grupo focal
##11.1 variables de grupo focal
##11.2 funciones de grupo focal
##11.3 botones de grupo focal
##12.1 variables de entrevista
##12.2 funciones de entrevista
##12.3 botones de entrevista
##13.1 variables de encuesta
##13.2 funciones de encuesta
##13.3 botones de encuesta


#1 Crear la app
app= Tk()



#14 seccion resumen

#variables
resumenProyecto=StringVar()
resumenProyecto.set("")

botonesDeGrupoFocal=[]
botonesDeGrupoEntrevista=[]
botonesDeGrupoEncuesta=[]
botonesDeGrupoSitioWeb=[]
#2 Titulo de la app
app.title("Planifica proyecto")
#3. en formato de cadena, indica las dimensiones
#app.geometry("300x700")

#4. tamaño minimo y maximo de la ventana
#app.minsize(width=300,height=700)
#app.maxsize(height=1500,width=600)

#5 tamaño de filas y columnas
app.grid_columnconfigure(index=0,minsize=60,weight=4,uniform="60")
app.grid_columnconfigure(index=1,minsize=60,weight=3,uniform="60")
app.grid_columnconfigure(index=2,minsize=60,weight=2,uniform="60")
app.grid_columnconfigure(index=3,minsize=60,weight=1,uniform="60")
app.grid_columnconfigure(index=4,minsize=60,weight=0,uniform="60")

for i in range(0,13,1):
    app.grid_rowconfigure(index=i,minsize=1,uniform="1",weight=2)


#6. crea los tabs

parent=ttk.Notebook(master=app)
tab1=Frame(app)
tab2=Frame(app)
tab3=Frame(app)
tab4=Frame(app)
tab5=Frame(app)
parent.add(child=tab1,text="Agrega encuesta")
parent.add(child=tab2,text="Agrega entrevistas")
parent.add(child=tab3,text="Agrega grupos focales")
parent.add(child=tab4,text="Agrega sitio web")
parent.add(child=tab5,text="Resumen proyecto")
parent.grid(column=0,row=0,columnspan=5, rowspan=10)




#7 crea el objeto presupuesto
miPresupuesto=Presupuesto()


#8 variables iniciales

conEncuesta=DoubleVar()
conEncuesta.set(0)

conEntrevista=DoubleVar()
conEntrevista.set(0)

conGrupoFocal=DoubleVar()
conGrupoFocal.set(0)

conSitioWeb=DoubleVar()
conSitioWeb.set(0)

#9 funciones inciales
def agregarEncuesta(self):
    if conEncuesta.get()==0.0:
        miPresupuesto.encuesta=False
        for i in  botonesDeGrupoEncuesta:
                i.configure(state=DISABLED)
        #egf_1.configure(state=DISABLED)
        #egf_4.configure(state=DISABLED)
    else:
        for i in  botonesDeGrupoEncuesta:
            i.configure(state=NORMAL)

        
def agregarEntrevista(self):
    if conEntrevista.get()==0.0:
        miPresupuesto.entrevista=False
        for i in  botonesDeGrupoEntrevista:
                i.configure(state=DISABLED)
        #egf_1.configure(state=DISABLED)
        #egf_4.configure(state=DISABLED)
    else:
        for i in  botonesDeGrupoEntrevista:
            i.configure(state=NORMAL)
        #egf_1.configure(state=NORMAL)
        #egf_4.config
        
 
 
       
def agregarGrupoFocal(self):
   
    if conGrupoFocal.get()==0.0:
        miPresupuesto.grupoFocal=False
        for i in  botonesDeGrupoFocal:
            i.configure(state=DISABLED)
        #egf_1.configure(state=DISABLED)
        #egf_4.configure(state=DISABLED)
    else:
        for i in  botonesDeGrupoFocal:
            i.configure(state=NORMAL)
        #egf_1.configure(state=NORMAL)
        #egf_4.configure(state=NORMAL)


def agregarSitioWeb(self):
       
    if conSitioWeb.get()==0.0:
        miPresupuesto.sitioWeb=False
        for i in  botonesDeGrupoSitioWeb:
            i.configure(state=DISABLED)
        #egf_1.configure(state=DISABLED)
        #egf_4.configure(state=DISABLED)
    else:
        for i in  botonesDeGrupoSitioWeb:
            i.configure(state=NORMAL)
        #egf_1.configure(state=NORMAL)
        #egf_4.configure(state=NORMAL)

#10 crea botonos para añadir elementos
l1=tk.Label(master=tab1,text="Agregar encuesta al proyecto: No=0, Sí=1")
s1= tk.Scale(master=tab1, orient="horizontal",from_=False, to=True,length=50,bigincrement=1,variable=conEncuesta, command=agregarEncuesta)
l1.grid(column=0,row=3,columnspan=3)
s1.grid(column=4,row=3)

l2=tk.Label(master=tab2,text="Agregar entrevistas al proyecto: No=0, Sí=1")
s2= tk.Scale(master=tab2, orient="horizontal",from_=False, to=True,length=50,bigincrement=1,variable=conEntrevista, command=agregarEntrevista)
l2.grid(column=0,row=3,columnspan=3)
s2.grid(column=4,row=3)

l3=tk.Label(master=tab3,text="Agregar grupos focales al proyecto: No=0, Sí=1")
s3= tk.Scale(master=tab3, orient="horizontal",from_=False, to=True,length=50,bigincrement=1,variable=conGrupoFocal, command=agregarGrupoFocal)
l3.grid(column=0,row=3,columnspan=3)
s3.grid(column=4,row=3)


l4=tk.Label(master=tab4,text="Agregar Sitio web: No=0, Sí=1")
s4= tk.Scale(master=tab4, orient="horizontal",from_=False, to=True,length=50,bigincrement=1,variable=conSitioWeb, command=agregarSitioWeb)
l4.grid(column=0,row=3,columnspan=3)
s4.grid(column=4,row=3)



#11  tab grupo focal
##11.1 variables de grupo focal
gf_cuantos=DoubleVar()
gf_cuantos.set(4),
gf_minutos=DoubleVar()
gf_minutos.set(45),
gf_asistentes=DoubleVar()
gf_asistentes.set(6),
gf_porcentajeValido=DoubleVar()
gf_porcentajeValido.set(.75),
gf_factorDeTranscripcion=DoubleVar()
gf_factorDeTranscripcion.set(4),
gf_costoDirectorMinuto=DoubleVar()
gf_costoDirectorMinuto.set(5.178),
gf_costoRelatorMinuto=DoubleVar()
gf_costoRelatorMinuto.set(1.852),
gf_material=DoubleVar()
gf_material.set(200)
gf_resumen=StringVar()
gf_detalle=StringVar()

#11.2 FUnciones de grupo focal
def agregaGrupoFocal(): 
    miPresupuesto.GrupoFocal(cuantos=gf_cuantos.get(),minutos=	gf_minutos.get(),asistentes=	gf_asistentes.get(),porcentajeValido=gf_porcentajeValido.get(),factorDeTranscripcion=	gf_factorDeTranscripcion.get(),
                costoDirectorMinuto=	gf_costoDirectorMinuto.get(),costoRelatorMinuto=	gf_costoRelatorMinuto.get(),material=gf_material.get())
    miPresupuesto.grupoFocal.resumen()
    miPresupuesto.grupoFocal.detalle()
    gf_detalle.set(miPresupuesto.grupoFocal.midetalle)
    x=gf_detalle.get()
    print(gf_detalle.get())
    egf_9.delete(1.0,END)
    egf_9.insert(END,x)
    miPresupuesto.costoProyecto()
    resumenProyecto.set(miPresupuesto.texto)
    w=resumenProyecto.get()
    print(resumenProyecto.get())
    resumen1.delete(1.0,END)
    resumen1.insert(END,w)
    


##11.3 botones y etiquetas de grupo focal
lgf_1=tk.Label(master=tab3,text="Cuántos grupos focales")
egf_1= Entry(master=tab3,textvariable=gf_cuantos, state=DISABLED)
lgf_1.grid(column=1, columnspan=3, row=4,sticky=N)
egf_1.grid(column=4, columnspan=1, row=4,sticky=N)

lgf_2=tk.Label(master=tab3,text="Minutos de duración")
egf_2= Entry(master=tab3,textvariable=gf_minutos, state=DISABLED)
lgf_2.grid(column=1, columnspan=3, row=5,sticky=N)
egf_2.grid(column=4, columnspan=1, row=5,sticky=N)

lgf_3=tk.Label(master=tab3,text="Número de asistentes")
egf_3= Entry(master=tab3,textvariable=gf_asistentes, state=DISABLED)
lgf_3.grid(column=1, columnspan=3, row=6,sticky=N)
egf_3.grid(column=4, columnspan=1, row=6,sticky=N)

lgf_0=tk.Label(master=tab3,text="Gasto en material por grupo focal")
egf_0= Entry(master=tab3,textvariable=gf_material, state=DISABLED)
lgf_0.grid(column=1, columnspan=3, row=7,sticky=N)
egf_0.grid(column=4, columnspan=1, row=7,sticky=N)


lgf_extra=tk.Label(master=tab3,text="No modificar lo siguiente",fg="red")
lgf_extra.grid(column=1, columnspan=3, row=8,sticky=N)


lgf_4=tk.Label(master=tab3,text="Porcentaje de tiempo efectivo")
egf_4= Entry(master=tab3,textvariable=gf_porcentajeValido,foreground="red", state=DISABLED)
lgf_4.grid(column=1, columnspan=3, row=9,sticky=N)
egf_4.grid(column=4, columnspan=1, row=9,sticky=N)

lgf_5=tk.Label(master=tab3,text="Minutos de transcripciòn por minuto de audio")
egf_5= Entry(master=tab3,textvariable=gf_factorDeTranscripcion,foreground="red", state=DISABLED)
lgf_5.grid(column=1, columnspan=3, row=10,sticky=N)
egf_5.grid(column=4, columnspan=1, row=10,sticky=N)


lgf_6=tk.Label(master=tab3,text="Costo por minuto del coordinador del grupo focal")
egf_6= Entry(master=tab3,textvariable=gf_costoDirectorMinuto,foreground="red", state=DISABLED)
lgf_6.grid(column=1, columnspan=3, row=11,sticky=N)
egf_6.grid(column=4, columnspan=1, row=11,sticky=N)

lgf_7=tk.Label(master=tab3,text="Costo por minuto del relator-transcriptor del grupo focal")
egf_7= Entry(master=tab3,textvariable=gf_costoRelatorMinuto,foreground="red", state=DISABLED)
lgf_7.grid(column=1, columnspan=3, row=12,sticky=N)
egf_7.grid(column=4, columnspan=1, row=12,sticky=N)

egf_8= Button(master=tab3,text="Añadir grupos focales", state=DISABLED, command=agregaGrupoFocal)
egf_8.grid(column=2, columnspan=1, row=14,sticky=N)

egf_9= Text(master=tab3,foreground="red", state="normal")
egf_9.grid(column=0, columnspan=10, row=16, rowspan=3,sticky=NE)


botonesDeGrupoFocal.append(egf_0)
botonesDeGrupoFocal.append(egf_1)
botonesDeGrupoFocal.append(egf_2)
botonesDeGrupoFocal.append(egf_3)
botonesDeGrupoFocal.append(egf_4)
botonesDeGrupoFocal.append(egf_5)
botonesDeGrupoFocal.append(egf_6)
botonesDeGrupoFocal.append(egf_7)
botonesDeGrupoFocal.append(egf_8)




#12 Paràmetros de Entrevista
#12.1 VARIABLES ENTREVISTA
ev_minutos=DoubleVar()
ev_minutos.set(45)
ev_cuantas=DoubleVar()
ev_cuantas.set(12)
ev_costoMinuto=DoubleVar()
ev_costoMinuto.set(1.7009)
ev_minutosPorItem=DoubleVar()
ev_minutosPorItem.set(6)
ev_resumen=StringVar()
ev_detalle=StringVar()

#12.2 funciones
def agregaEntrevista():
    miPresupuesto.Entrevista(minutos=ev_minutos.get(),cuantas=ev_cuantas.get(),costoMinuto=ev_costoMinuto.get(),minutosPorItem=ev_minutosPorItem.get())
    miPresupuesto.entrevista.resumen()
    miPresupuesto.entrevista.detalle()
    ev_detalle.set(miPresupuesto.entrevista.midetalle)
    y=ev_detalle.get()
    print(ev_detalle.get())
    eev_6.delete(1.0,END)
    eev_6.insert(END,y)
    miPresupuesto.costoProyecto()
    resumenProyecto.set(miPresupuesto.texto)
    w=resumenProyecto.get()
    print(resumenProyecto.get())
    resumen1.delete(1.0,END)
    resumen1.insert(END,w)


#12.3 botones
lev_1=tk.Label(master=tab2,text="Cuántas entrevistas")
eev_1= Entry(master=tab2,textvariable=ev_cuantas, state=DISABLED)
lev_1.grid(column=1, columnspan=3, row=4,sticky=N)
eev_1.grid(column=4, columnspan=1, row=4,sticky=N)

lev_2=tk.Label(master=tab2,text="Minutos por  entrevista")
eev_2= Entry(master=tab2,textvariable=ev_minutos, state=DISABLED)
lev_2.grid(column=1, columnspan=3, row=5,sticky=N)
eev_2.grid(column=4, columnspan=1, row=5,sticky=N)

lev_extra=tk.Label(master=tab2,text="No modificar lo siguiente",fg="red")
lev_extra.grid(column=1, columnspan=3, row=7,sticky=N)


lev_3=tk.Label(master=tab2,text="Costo por minuto")
eev_3= Entry(master=tab2,textvariable=ev_costoMinuto, state=DISABLED,foreground="red")
lev_3.grid(column=1, columnspan=3, row=9,sticky=N)
eev_3.grid(column=4, columnspan=1, row=9,sticky=N)

lev_4=tk.Label(master=tab2,text="Minutos por  item")
eev_4= Entry(master=tab2,textvariable=ev_minutosPorItem, state=DISABLED,foreground="red")
lev_4.grid(column=1, columnspan=3, row=10,sticky=N)
eev_4.grid(column=4, columnspan=1, row=10,sticky=N)

eev_5= Button(master=tab2,text="Añadir entrevistas", state=DISABLED, command=agregaEntrevista)
eev_5.grid(column=2, columnspan=1, row=12,sticky=N)

eev_6= Text(master=tab2,foreground="red", state="normal")
eev_6.grid(column=0, columnspan=10, row=14, rowspan=3,sticky=NE)

botonesDeGrupoEntrevista.append(eev_1)
botonesDeGrupoEntrevista.append(eev_2)
botonesDeGrupoEntrevista.append(eev_3)
botonesDeGrupoEntrevista.append(eev_4)
botonesDeGrupoEntrevista.append(eev_5)



#13 ENCUESTA
# 13.1 Variables encuesta
em_tamanoMuestra=DoubleVar()
em_tamanoMuestra.set(500)
em_resumen=StringVar()
em_resumen.set("")
em_detalle=StringVar()
em_detalle.set("")
# parametros fijos
em_costoReactivo=DoubleVar()
em_costoReactivo.set(0.6)
em_pagoMinimo=DoubleVar()
em_pagoMinimo.set(50)
em_viaticosPorDia=DoubleVar()
em_viaticosPorDia.set(50)
em_costoDisenoCuestionario=DoubleVar()
em_costoDisenoCuestionario.set(7142)
em_costoMuestreo=DoubleVar()
em_costoMuestreo.set(28571)
em_costoInforme=DoubleVar()
em_costoInforme.set(2143)
em_pagoHORAsupervisor=DoubleVar()
em_pagoHORAsupervisor.set(240,)
em_maximoReactivosHumanamentePosibles=DoubleVar()
em_maximoReactivosHumanamentePosibles.set(400)
em_preguntasPorMinuto=DoubleVar()
em_preguntasPorMinuto.set(2.3)
em_costoProjectManager=DoubleVar()
em_costoProjectManager.set(8000)

#parametros variables

em_cuantasVecesSeHaraLaEncuesta=DoubleVar()
em_cuantasVecesSeHaraLaEncuesta.set(1)
em_tasaDepreciacionPorRepeticion=DoubleVar()
em_tasaDepreciacionPorRepeticion.set(.05)
em_numeroDeRectivos=DoubleVar()
em_numeroDeRectivos.set(50)
em_diasDeOperativo=DoubleVar()
em_diasDeOperativo.set(5)
em_minutosDeDesplazamientoEntreViviendas=DoubleVar()
em_minutosDeDesplazamientoEntreViviendas.set(10)
em_horasJornadaDiaria=DoubleVar()
em_horasJornadaDiaria.set(4)

# 13.2 funciones

def agregaEncuesta():
    miPresupuesto.Encuesta(tamanoMuestra=em_tamanoMuestra.get())
    miPresupuesto.encuesta.parametrosFijos(costoReactivo=em_costoReactivo.get(),pagoMinimo=em_pagoMinimo.get(),viaticosPorDia=em_viaticosPorDia.get(),costoDisenoCuestionario=em_costoDisenoCuestionario.get(),costoMuestreo=em_costoMuestreo.get(),costoInforme=em_costoInforme.get(), pagoHORAsupervisor=em_pagoHORAsupervisor.get(),maximoReactivosHumanamentePosibles=em_maximoReactivosHumanamentePosibles.get(),preguntasPorMinuto=em_preguntasPorMinuto.get(),costoProjectManager=em_costoProjectManager.get())
    miPresupuesto.encuesta.parametrosVariables(cuantasVecesSeHaraLaEncuesta=em_cuantasVecesSeHaraLaEncuesta.get(),tasaDepreciacionPorRepeticion= em_tasaDepreciacionPorRepeticion.get(),numeroDeRectivos=em_numeroDeRectivos.get(),diasDeOperativo=em_diasDeOperativo.get(),minutosDeDesplazamientoEntreViviendas=em_minutosDeDesplazamientoEntreViviendas.get(),horasJornadaDiaria=em_horasJornadaDiaria.get())
    miPresupuesto.encuesta.planifica()
    miPresupuesto.encuesta.detalle()
    miPresupuesto.encuesta.resumen()

    em_detalle.set(miPresupuesto.encuesta.midetalle)
    z=em_detalle.get()
    print(em_detalle.get())
    eem_17.delete(1.0,END)
    eem_17.insert(END,z)
    miPresupuesto.costoProyecto()
    
    resumenProyecto.set(miPresupuesto.texto)
    w=resumenProyecto.get()
    print(resumenProyecto.get())
    resumen1.delete(1.0,END)
    resumen1.insert(END,w)






#13.3 botones
lem_1=tk.Label(master=tab1,text="Cuántos cuestionarios")
eem_1= Entry(master=tab1,textvariable=em_tamanoMuestra, state=DISABLED)
lem_1.grid(column=1, columnspan=3, row=4,sticky=N)
eem_1.grid(column=4, columnspan=1, row=4,sticky=N)

lem_2=tk.Label(master=tab1,text="Cuántos reactivos")
eem_2= Entry(master=tab1,textvariable=em_numeroDeRectivos, state=DISABLED)
lem_2.grid(column=1, columnspan=3, row=5,sticky=N)
eem_2.grid(column=4, columnspan=1, row=5,sticky=N)

lem_3=tk.Label(master=tab1,text="Cuántos días de operativo")
eem_3= Entry(master=tab1,textvariable=em_diasDeOperativo, state=DISABLED)
lem_3.grid(column=1, columnspan=3, row=6,sticky=N)
eem_3.grid(column=4, columnspan=1, row=6,sticky=N)

lem_4=tk.Label(master=tab1,text="Minutos para desplazarse entre viviendas")
eem_4= Entry(master=tab1,textvariable=em_minutosDeDesplazamientoEntreViviendas, state=DISABLED)
lem_4.grid(column=1, columnspan=3, row=7,sticky=N)
eem_4.grid(column=4, columnspan=1, row=7,sticky=N)

lem_5=tk.Label(master=tab1,text="Horas de trabajo diarias (duración jornada)")
eem_5= Entry(master=tab1,textvariable=em_horasJornadaDiaria, state=DISABLED)
lem_5.grid(column=1, columnspan=3, row=8,sticky=N)
eem_5.grid(column=4, columnspan=1, row=8,sticky=N)                   

lem_extra=tk.Label(master=tab1,text="No modificar lo siguiente",fg="red")
lem_extra.grid(column=1, columnspan=3, row=10,sticky=N)

lem_6=tk.Label(master=tab1,text="Costo por reactivo")
eem_6= Entry(master=tab1,textvariable=em_costoReactivo, state=DISABLED, foreground="red")
lem_6.grid(column=1, columnspan=3, row=12,sticky=N)
eem_6.grid(column=4, columnspan=1, row=12,sticky=N) 

lem_7=tk.Label(master=tab1,text="Pago mínimo por cuestionario")
eem_7= Entry(master=tab1,textvariable=em_pagoMinimo, state=DISABLED, foreground="red")
lem_7.grid(column=1, columnspan=3, row=13,sticky=N)
eem_7.grid(column=4, columnspan=1, row=13,sticky=N) 

lem_8=tk.Label(master=tab1,text="Viàticos por día")
eem_8= Entry(master=tab1,textvariable=em_viaticosPorDia, state=DISABLED, foreground="red")
lem_8.grid(column=1, columnspan=3, row=14,sticky=N)
eem_8.grid(column=4, columnspan=1, row=14,sticky=N) 

lem_9=tk.Label(master=tab1,text="Costo por diseñar cuestionario")
eem_9= Entry(master=tab1,textvariable=em_costoDisenoCuestionario, state=DISABLED, foreground="red")
lem_9.grid(column=1, columnspan=3, row=15,sticky=N)
eem_9.grid(column=4, columnspan=1, row=15,sticky=N) 

lem_10=tk.Label(master=tab1,text="Costo por diseño, selección y expansión de muestra")
eem_10= Entry(master=tab1,textvariable=em_costoMuestreo, state=DISABLED, foreground="red")
lem_10.grid(column=1, columnspan=3, row=16,sticky=N)
eem_10.grid(column=4, columnspan=1, row=16,sticky=N) 

lem_11=tk.Label(master=tab1,text="Costo por elaboración de informe")
eem_11= Entry(master=tab1,textvariable=em_costoInforme, state=DISABLED, foreground="red")
lem_11.grid(column=1, columnspan=3, row=17,sticky=N)
eem_11.grid(column=4, columnspan=1, row=17,sticky=N) 

lem_12=tk.Label(master=tab1,text="Pago por hora de supervisor")
eem_12= Entry(master=tab1,textvariable=em_pagoHORAsupervisor, state=DISABLED, foreground="red")
lem_12.grid(column=1, columnspan=3, row=18,sticky=N)
eem_12.grid(column=4, columnspan=1, row=18,sticky=N) 

lem_13=tk.Label(master=tab1,text="Màximo de reactivos humanamente posibles por persona-día")
eem_13= Entry(master=tab1,textvariable=em_maximoReactivosHumanamentePosibles, state=DISABLED, foreground="red")
lem_13.grid(column=1, columnspan=3, row=19,sticky=N)
eem_13.grid(column=4, columnspan=1, row=19,sticky=N) 

lem_14=tk.Label(master=tab1,text="Preguntas que se pueden hacer por minuto")
eem_14= Entry(master=tab1,textvariable=em_preguntasPorMinuto, state=DISABLED, foreground="red")
lem_14.grid(column=1, columnspan=3, row=20,sticky=N)
eem_14.grid(column=4, columnspan=1, row=20,sticky=N) 

lem_15=tk.Label(master=tab1,text="Honorarios Project Manager")
eem_15= Entry(master=tab1,textvariable=em_costoProjectManager, state=DISABLED, foreground="red")
lem_15.grid(column=1, columnspan=3, row=21,sticky=N)
eem_15.grid(column=4, columnspan=1, row=21,sticky=N) 

lem_18=tk.Label(master=tab1,text="Cuantas veces se hará la encuesta?")
eem_18= Entry(master=tab1,textvariable=em_cuantasVecesSeHaraLaEncuesta, state=DISABLED, foreground="red")
lem_18.grid(column=1, columnspan=3, row=22,sticky=N)
eem_18.grid(column=4, columnspan=1, row=22,sticky=N) 

lem_19=tk.Label(master=tab1,text="Tasa de depreciaciòn por repetición")
eem_19= Entry(master=tab1,textvariable=em_tasaDepreciacionPorRepeticion, state=DISABLED, foreground="red")
lem_19.grid(column=1, columnspan=3, row=23,sticky=N)
eem_19.grid(column=4, columnspan=1, row=23,sticky=N) 


eem_16= Button(master=tab1,text="Añadir encuesta", state=DISABLED, command=agregaEncuesta)
eem_16.grid(column=2, columnspan=1, row=25,sticky=N)

eem_17= Text(master=tab1,foreground="red", state="normal")
eem_17.grid(column=0, columnspan=10, row=26, rowspan=3,sticky=NE)



botonesDeGrupoEncuesta.append(eem_1)
botonesDeGrupoEncuesta.append(eem_2)
botonesDeGrupoEncuesta.append(eem_3)
botonesDeGrupoEncuesta.append(eem_4)
botonesDeGrupoEncuesta.append(eem_5)
botonesDeGrupoEncuesta.append(eem_6)
botonesDeGrupoEncuesta.append(eem_7)
botonesDeGrupoEncuesta.append(eem_8)
botonesDeGrupoEncuesta.append(eem_9)
botonesDeGrupoEncuesta.append(eem_10)
botonesDeGrupoEncuesta.append(eem_11)
botonesDeGrupoEncuesta.append(eem_12)
botonesDeGrupoEncuesta.append(eem_13)
botonesDeGrupoEncuesta.append(eem_14)
botonesDeGrupoEncuesta.append(eem_15)
botonesDeGrupoEncuesta.append(eem_16)
botonesDeGrupoEncuesta.append(eem_18)
botonesDeGrupoEncuesta.append(eem_19)





#14 Sitio web
# 14.1 Variables sitio web
sw_rAvanzado=BooleanVar(master=tab4,value=False)
#sw_rAvanzado.set(True)
sw_rBasico=BooleanVar(master=tab4,value=False)
#sw_rBasico.set(True)
sw_htmlCSSjs=BooleanVar()
#sw_htmlCSSjs.set(True)
sw_jsAvanzado=BooleanVar()
#sw_jsAvanzado.set(True)
sw_leaflet=BooleanVar()
#sw_leaflet.set(True)
sw_php=BooleanVar()
#sw_php.set(True)
sw_mysqlAvanzado=BooleanVar()
#sw_mysqlAvanzado.set(True)
sw_elektron=BooleanVar()
#sw_elektron.set(True)
sw_c_rAvanzado=DoubleVar()
sw_c_rAvanzado.set(4286)
sw_c_rBasico=DoubleVar()
sw_c_rBasico.set(2858)
sw_c_htmlCSSjs=DoubleVar()
sw_c_htmlCSSjs.set(2858)
sw_c_jsAvanzado=DoubleVar()
sw_c_jsAvanzado.set(2858)
sw_c_leaflet=DoubleVar()
sw_c_leaflet.set(4286)
sw_c_php=DoubleVar()
sw_c_php.set(3572)
sw_c_mysqlAvanzado=DoubleVar()
sw_c_mysqlAvanzado.set(3572)
sw_c_elektron=DoubleVar()
sw_c_elektron.set(1429)
sw_resumen=StringVar()
sw_resumen.set("")
sw_detalle=StringVar()
sw_detalle.set("")
# funcioes sitio web 

# 13.2 funciones

def agregaSitioWeb():
    miPresupuesto.SitioWeb(rAvanzado=sw_rAvanzado.get(),rBasico=sw_rBasico.get(),htmlCSSjs=sw_htmlCSSjs.get(),jsAvanzado=sw_jsAvanzado.get(),leaflet=sw_leaflet.get(),php=sw_php.get(),mysqlAvanzado=sw_mysqlAvanzado.get(),elektron=sw_elektron.get(),c_rAvanzado=sw_c_rAvanzado.get(),c_rBasico=sw_c_rBasico.get(),c_htmlCSSjs=sw_c_htmlCSSjs.get(),c_jsAvanzado=sw_c_jsAvanzado.get(),c_leaflet=sw_c_leaflet.get(),c_php=sw_c_php.get(),c_mysqlAvanzado=sw_c_mysqlAvanzado.get(),c_elektron=sw_c_elektron.get())    
    miPresupuesto.sitioWeb.detalle()
    miPresupuesto.sitioWeb.resumen()
    print(sw_rAvanzado.get())
    print(sw_rBasico.get())

    sw_detalle.set(miPresupuesto.sitioWeb.midetalle)
    z=sw_detalle.get()
    print(sw_detalle.get())
    e_sw18.delete(1.0,END)
    e_sw18.insert(END,z)
    miPresupuesto.costoProyecto()
    
    resumenProyecto.set(miPresupuesto.texto)
    w=resumenProyecto.get()
    print(resumenProyecto.get())
    resumen1.delete(1.0,END)
    resumen1.insert(END,w)

##14.3 botones

l_sw1=tk.Label(master=tab4,text="Proceso básico R")
e_sw1= Checkbutton(master=tab4,onvalue=True, offvalue=False,variable=sw_rBasico, state=DISABLED)
l_sw1.grid(column=1, columnspan=3, row=4,sticky=N)
e_sw1.grid(column=4, columnspan=1, row=4,sticky=N)

l_sw2=tk.Label(master=tab4,text="Proceso avanzado R")
e_sw2= Checkbutton(master=tab4,onvalue=True, offvalue=False,variable=sw_rAvanzado, state=DISABLED)
l_sw2.grid(column=1, columnspan=3, row=5,sticky=N)
e_sw2.grid(column=4, columnspan=1, row=5,sticky=N)

l_sw3=tk.Label(master=tab4,text="HTML, CSS y JS básico")
e_sw3= Checkbutton(master=tab4,onvalue=True, offvalue=False,variable=sw_htmlCSSjs, state=DISABLED)
l_sw3.grid(column=1, columnspan=3, row=6,sticky=N)
e_sw3.grid(column=4, columnspan=1, row=6,sticky=N)

l_sw4=tk.Label(master=tab4,text="JS avanzado")
e_sw4= Checkbutton(master=tab4,onvalue=True, offvalue=False,variable=sw_jsAvanzado, state=DISABLED)
l_sw4.grid(column=1, columnspan=3, row=7,sticky=N)
e_sw4.grid(column=4, columnspan=1, row=7,sticky=N)


l_sw5=tk.Label(master=tab4,text="Leaflet")
e_sw5= Checkbutton(master=tab4,onvalue=True, offvalue=False,variable=sw_leaflet, state=DISABLED)
l_sw5.grid(column=1, columnspan=3, row=8,sticky=N)
e_sw5.grid(column=4, columnspan=1, row=8,sticky=N)


l_sw6=tk.Label(master=tab4,text="PHP")
e_sw6= Checkbutton(master=tab4,onvalue=True, offvalue=False,variable=sw_php, state=DISABLED)
l_sw6.grid(column=1, columnspan=3, row=9,sticky=N)
e_sw6.grid(column=4, columnspan=1, row=9,sticky=N)

l_sw7=tk.Label(master=tab4,text="MySQL avanzado")
e_sw7= Checkbutton(master=tab4,onvalue=True, offvalue=False,variable=sw_mysqlAvanzado, state=DISABLED)
l_sw7.grid(column=1, columnspan=3, row=10,sticky=N)
e_sw7.grid(column=4, columnspan=1, row=10,sticky=N)

l_sw8=tk.Label(master=tab4,text="Elektron")
e_sw8= Checkbutton(master=tab4,onvalue=True, offvalue=False,variable=sw_elektron, state=DISABLED)
l_sw8.grid(column=1, columnspan=3, row=11,sticky=N)
e_sw8.grid(column=4, columnspan=1, row=11,sticky=N)

esw_extra=tk.Label(master=tab4,text="No modificar lo siguiente",fg="red")
esw_extra.grid(column=1, columnspan=3, row=13,sticky=N)


l_sw9=tk.Label(master=tab4,text="Costo por R básico")
e_sw9= Entry(master=tab4,textvariable=sw_c_rBasico, state=DISABLED, foreground="red")
l_sw9.grid(column=1, columnspan=3, row=15,sticky=N)
e_sw9.grid(column=4, columnspan=1, row=15,sticky=N) 

l_sw10=tk.Label(master=tab4,text="Costo por R avanzado")
e_sw10= Entry(master=tab4,textvariable=sw_c_rAvanzado, state=DISABLED, foreground="red")
l_sw10.grid(column=1, columnspan=3, row=16,sticky=N)
e_sw10.grid(column=4, columnspan=1, row=16,sticky=N)

l_sw11=tk.Label(master=tab4,text="Costo por HTML-CSS-JS")
e_sw11= Entry(master=tab4,textvariable=sw_c_htmlCSSjs, state=DISABLED, foreground="red")
l_sw11.grid(column=1, columnspan=3, row=17,sticky=N)
e_sw11.grid(column=4, columnspan=1, row=17,sticky=N)

l_sw12=tk.Label(master=tab4,text="Costo por JS avanzado")
e_sw12= Entry(master=tab4,textvariable=sw_c_jsAvanzado, state=DISABLED, foreground="red")
l_sw12.grid(column=1, columnspan=3, row=18,sticky=N)
e_sw12.grid(column=4, columnspan=1, row=18,sticky=N)

l_sw13=tk.Label(master=tab4,text="Costo por Leaflet")
e_sw13= Entry(master=tab4,textvariable=sw_c_leaflet, state=DISABLED, foreground="red")
l_sw13.grid(column=1, columnspan=3, row=19,sticky=N)
e_sw13.grid(column=4, columnspan=1, row=19,sticky=N)

l_sw14=tk.Label(master=tab4,text="Costo por PHP")
e_sw14= Entry(master=tab4,textvariable=sw_c_php, state=DISABLED, foreground="red")
l_sw14.grid(column=1, columnspan=3, row=20,sticky=N)
e_sw14.grid(column=4, columnspan=1, row=20,sticky=N)

l_sw15=tk.Label(master=tab4,text="Costo por MySQL avanzado")
e_sw15= Entry(master=tab4,textvariable=sw_c_mysqlAvanzado, state=DISABLED, foreground="red")
l_sw15.grid(column=1, columnspan=3, row=21,sticky=N)
e_sw15.grid(column=4, columnspan=1, row=21,sticky=N)

l_sw16=tk.Label(master=tab4,text="Costo por Elektron")
e_sw16= Entry(master=tab4,textvariable=sw_c_elektron, state=DISABLED, foreground="red")
l_sw16.grid(column=1, columnspan=3, row=22,sticky=N)
e_sw16.grid(column=4, columnspan=1, row=22,sticky=N)


e_sw17= Button(master=tab4,text="Añadir sitio Web", state=DISABLED, command=agregaSitioWeb)
e_sw17.grid(column=2, columnspan=1, row=24,sticky=N)

e_sw18= Text(master=tab4,foreground="red", state="normal")
e_sw18.grid(column=0, columnspan=10, row=26, rowspan=3,sticky=NE)


botonesDeGrupoSitioWeb.append(e_sw1)
botonesDeGrupoSitioWeb.append(e_sw2)
botonesDeGrupoSitioWeb.append(e_sw3)
botonesDeGrupoSitioWeb.append(e_sw4)
botonesDeGrupoSitioWeb.append(e_sw5)
botonesDeGrupoSitioWeb.append(e_sw6)
botonesDeGrupoSitioWeb.append(e_sw7)
botonesDeGrupoSitioWeb.append(e_sw8)
botonesDeGrupoSitioWeb.append(e_sw9)
botonesDeGrupoSitioWeb.append(e_sw10)
botonesDeGrupoSitioWeb.append(e_sw11)
botonesDeGrupoSitioWeb.append(e_sw12)
botonesDeGrupoSitioWeb.append(e_sw13)
botonesDeGrupoSitioWeb.append(e_sw14)
botonesDeGrupoSitioWeb.append(e_sw15)
botonesDeGrupoSitioWeb.append(e_sw16)
botonesDeGrupoSitioWeb.append(e_sw17)





#Funciones
def exportaDetalle():
    fecha=datetime.datetime.now()
    fecha=str(fecha.strftime("%Y-%b-%d %H_%M"))
    nombre="miPresupuesto_{}.csv".format(fecha)
    print(nombre)
    archivo=open(nombre,"w")
    archivo.write(miPresupuesto.texto)
    if miPresupuesto.sitioWeb!=False:
        archivo.write(miPresupuesto.sitioWeb.midetalle)
    if miPresupuesto.encuesta!=False:
        archivo.write(miPresupuesto.encuesta.midetalle)
    if miPresupuesto.entrevista!=False:
        archivo.write(miPresupuesto.entrevista.midetalle)
    if miPresupuesto.grupoFocal!=False:
        archivo.write(miPresupuesto.grupoFocal.midetalle)
    archivo.close()
    print("exportado")
    
    #escribir.writerow(miPresupuesto.entrevista.midetalle)
    #escribir.writerow(miPresupuesto.grupoFocal.midetalle)
    #archivo.close()
    

#Botones

resumen1= Text(master=tab5,foreground="blue", state="normal")
resumen1.grid(column=0, columnspan=10, row=2, rowspan=3,sticky=NE)

resumen2= Button(master=tab5,text="Exportar detalle", state="normal", command=exportaDetalle)
resumen2.grid(column=2, columnspan=1, row=10,sticky=N)


#miPresupuesto.grupoFocal.detalle()

# paràmetros de encuesta
#miPresupuesto.Encuesta()
#miPresupuesto.encuesta.parametrosFijos()
#miPresupuesto.encuesta.parametrosVariables()
#miPresupuesto.encuesta.planifica()
#miPresupuesto.encuesta.detalle()
# costo de proyecto








app.mainloop()