import math
from presupuestoDeGrupoFocal import GrupoFocal
from presupuestoDeLaEntrevista import Entrevista
from presupuestoDeLaMuestra import Encuesta
from presupuestoDeSitioWeb import SitioWeb



#Los argumentos son booleanos; True por cada elemento que se vaya a incluir en el presupuesto
class Presupuesto:
    def __init__(self):
        self.entrevista=False
        self.grupoFocal=False
        self.encuesta=False
        self.sitioWeb=False
        self.costoEncuesta=0
        self.costoEntrevista=0
        self.costoGrupoFocal=0
        self.costoSitioWeb=0
        self.subtotal=0
        self.totalUAQ=0
        
    def Entrevista(self,minutos=45,cuantas=12,costoMinuto=1.7009,minutosPorItem=6):
        self.entrevista=Entrevista(minutos,cuantas,costoMinuto,minutosPorItem)

    def GrupoFocal(self,cuantos=4,minutos=	45,asistentes=	6,porcentajeValido=.75,factorDeTranscripcion=	4,
                costoDirectorMinuto=	5.178,costoRelatorMinuto=	1.852,material=	200):
        self.grupoFocal=GrupoFocal(cuantos,minutos,asistentes,porcentajeValido,factorDeTranscripcion, costoDirectorMinuto,costoRelatorMinuto,material)
    def Encuesta(self,tamanoMuestra=500):
        self.encuesta=Encuesta(tamanoMuestra)
    

    
    def parametrosfijos(self,costoReactivo=.6,
                        pagoMinimo=50,
                        viaticosPorDia=50,
                        costoDisenoCuestionario=7142,
                        costoMuestreo=28571,
                        costoInforme=2143, 
                        pagoHORAsupervisor=240,
                        maximoReactivosHumanamentePosibles=400,
                        preguntasPorMinuto=2.3,
                        costoProjectManager=7500
                        ):
        if self.encuesta!=False:
            self.encuesta.parametrosFijos(costoReactivo,
                        pagoMinimo,
                        viaticosPorDia,
                        costoDisenoCuestionario,
                        costoMuestreo,
                        costoInforme, 
                        pagoHORAsupervisor,
                        maximoReactivosHumanamentePosibles,
                        preguntasPorMinuto,
                        costoProjectManager
                        )

    def parametrosVariables(self,numeroDeRectivos=50,diasDeOperativo=5,minutosDeDesplazamientoEntreViviendas=10,horasJornadaDiaria=4):
        if self.encuesta!=False:
            self.encuesta.parametrosVariables(numeroDeRectivos,diasDeOperativo=5,minutosDeDesplazamientoEntreViviendas=10,horasJornadaDiaria=4)
    
    
    def SitioWeb(self,rAvanzado=True,rBasico=False,htmlCSSjs=True,jsAvanzado=True,leaflet=True,php=False,mysqlAvanzado=False,elektron=True,c_rAvanzado=3000,c_rBasico=2000,c_htmlCSSjs=2000,c_jsAvanzado=1500,c_leaflet=3000,c_php=2500,c_mysqlAvanzado=2500,c_elektron=1000):
        self.sitioWeb=SitioWeb(rAvanzado,rBasico,htmlCSSjs,jsAvanzado,leaflet,php,mysqlAvanzado,elektron)
        self.sitioWeb.costosFijosWeb(c_rAvanzado,c_rBasico,c_htmlCSSjs,c_jsAvanzado,c_leaflet,c_php,c_mysqlAvanzado,c_elektron)
        
   
    def calculaCosto(self):
        self.texto="\n\n"
        if self.sitioWeb!=False:
            self.costoSitioWeb=self.sitioWeb.costoSitioWeb
            self.texto=self.texto+" "+self.sitioWeb.miresumen+"\n"
        else:
            self.costoSitioWeb=0
            
        if self.grupoFocal!=False:
            self.costoGrupoFocal=self.grupoFocal.costoTotal
            self.texto=self.texto+" "+self.grupoFocal.miresumen+"\n"
        else:
            self.costoGrupoFocal=0
            
        if self.encuesta!=False:
            self.costoEncuesta=self.encuesta.total
            self.texto=self.texto+" "+self.encuesta.miresumen+"\n"
        else:
            self.costoEncuesta=0
            
        if self.entrevista!=False:
            self.costoEntrevista=self.entrevista.costoProyectoEntrevistas
            self.texto=self.texto+" "+self.entrevista.miresumen+"\n"
        else:
            self.costoEntrevista=0
        
        self.subtotal= math.ceil(self.costoGrupoFocal+self.costoEncuesta+self.costoEntrevista+self.costoSitioWeb)
        self.totalUAQ=math.ceil(self.subtotal/.7)
        self.texto=self.texto+'Subtotal: $ {}. \n. Total UAQ: ${}.'.format(self.subtotal,self.totalUAQ)
            
    def costoProyecto(self):
        self.calculaCosto()
        print(self.texto)
        #print(f'Subtotal: $ {self.subtotal}. \n. Total UAQ: $ {self.totalUAQ}.')
        

'''
mip= Presupuesto()       
mip.SitioWeb()
print(mip.sitioWeb.elektron)
mip.sitioWeb.resumen()
print(mip.sitioWeb.detalle())
print(mip.sitioWeb.dic)
print(mip.sitioWeb.midetalle)
'''