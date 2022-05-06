import math

class Muestra:
    def __init__(self,confianza=1.96, error=.15,p=.5,tr=1,deff=1):
        self.confianza=confianza
        self.error=error
        self.p=p
        self.q=1-self.p
        self.tr=tr
        self.deff=deff
    
    def tamano(self):
        self.muestra=((self.confianza**2)*self.q*self.deff)/((self.error**2)*self.p*self.tr)
        self.muestra=math.ceil(self.muestra)
        return(self.muestra)
    
class Encuesta():   
    def __init__(self,tamanoMuestra=500):
        
        self.tamanoMuestra=tamanoMuestra,
        self.tamanoMuestra=list(self.tamanoMuestra)[0]
        self.miresumen=""
    def parametrosFijos(self,costoReactivo=.6,
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
        self.costoReactivo=costoReactivo
        self.pagoMinimo=pagoMinimo
        self.viaticosPorDia=viaticosPorDia
        self.costoDisenoCuestionario=costoDisenoCuestionario
        self.costoMuestreo=costoMuestreo
        self.costoInforme=costoInforme
        self.pagoHORAsupervisor=pagoHORAsupervisor
        self.maximoReactivosHumanamentePosibles=maximoReactivosHumanamentePosibles
        self.preguntasPorMinuto=preguntasPorMinuto
        self.costoProjectManager=costoProjectManager
        
    def parametrosVariables(
        self,
        cuantasVecesSeHaraLaEncuesta=1,
        tasaDepreciacionPorRepeticion=.05,
        numeroDeRectivos=50,                    
        diasDeOperativo=5,
        minutosDeDesplazamientoEntreViviendas=10,
        horasJornadaDiaria=4
        ):
        self.cuantasVecesSeHaraLaEncuesta=cuantasVecesSeHaraLaEncuesta
        self.tasaDepreciacionPorRepeticion=tasaDepreciacionPorRepeticion
        self.numeroDeRectivos=numeroDeRectivos
        self.diasDeOperativo=diasDeOperativo
        self.minutosDeDesplazamientoEntreViviendas=minutosDeDesplazamientoEntreViviendas
        self.horasJornadaDiaria=horasJornadaDiaria
        
    
    def planifica(self):
        if self.diasDeOperativo>5:
            a=self.tasaDepreciacionPorRepeticion*.20
            print(a)
            a=self.diasDeOperativo*a
            self.pagoHORAsupervisor=self.pagoHORAsupervisor-(self.pagoHORAsupervisor*a)
            print(a)
        b=self.cuantasVecesSeHaraLaEncuesta*self.tasaDepreciacionPorRepeticion
        self.costoDisenoCuestionario=self.costoDisenoCuestionario-((b*1.5)*self.costoDisenoCuestionario)
        self.costoMuestreo=self.costoMuestreo-(self.costoMuestreo*b)
        self.costoInforme=self.costoInforme-(self.costoInforme*b)
        self.costoProjectManager=self.costoProjectManager-(self.costoProjectManager*b)
         
         
         
         
        self.tiempoPorCuestionario=self.numeroDeRectivos/self.preguntasPorMinuto
        self.cuotaMaxima=self.maximoReactivosHumanamentePosibles/self.numeroDeRectivos
        self.jornadaReal=(self.cuotaMaxima*(self.tiempoPorCuestionario+self.minutosDeDesplazamientoEntreViviendas))/60    
        self.personalNecesario=(self.tamanoMuestra/self.cuotaMaxima)/self.diasDeOperativo
        z=self.jornadaReal/self.horasJornadaDiaria
        y=math.ceil(self.jornadaReal%self.horasJornadaDiaria)
        if(z>1.05):
            self.personalNecesario=self.personalNecesario+y
        else:
            self.personalNecesario=self.personalNecesario+0
        self.personalNecesario=math.ceil(self.personalNecesario)
        self.supervisorNecesario=math.floor(self.personalNecesario/4.7)
        self.pagoPorCuestionario=self.pagoMinimo
        z=self.numeroDeRectivos*self.costoReactivo
        if(z>self.pagoMinimo):
            self.pagoPorCuestionario=z
        self.pagoMedioEncuestador=self.pagoPorCuestionario*self.cuotaMaxima*self.diasDeOperativo
        self.pagoSupervisor=self.pagoHORAsupervisor*self.horasJornadaDiaria*self.diasDeOperativo
        self.totalViaticos=math.ceil(self.viaticosPorDia*self.personalNecesario*self.diasDeOperativo)
        self.totalSupervisores=self.pagoSupervisor*self.supervisorNecesario
        self.totalEncuestadores=self.pagoPorCuestionario*self.tamanoMuestra
        self.totalCampo=self.totalViaticos+self.totalEncuestadores+self.totalSupervisores
        self.totalGabinete=self.costoDisenoCuestionario+self.costoMuestreo+self.costoInforme+self.costoProjectManager
        self.totalUnitario=self.totalCampo+self.totalGabinete
        self.total=self.totalUnitario*self.cuantasVecesSeHaraLaEncuesta
        self.midetalle=""
        self.overheadUAQ=round(self.total/.7,2)
        self.dic={"muestra":math.ceil(self.tamanoMuestra),
                  "diasDeOperativo":self.diasDeOperativo,
                  "reactivos":self.numeroDeRectivos,
                "tiempoPorCuestionario" :round(self.tiempoPorCuestionario,2),
                  "cuotaMaxima":self.cuotaMaxima,
                  "horasJornadaDiaria":round(self.horasJornadaDiaria,2),
                  "personalNecesario":math.floor(self.personalNecesario),
                  "supervisorNecesario":self.supervisorNecesario,
                  "pagoPorCuestionario":self.pagoPorCuestionario,
                  "pagoMedioEncuestador":self.pagoMedioEncuestador,
                  "pagoSupervisor":self.pagoSupervisor,
                  "costoDisenoCuestionario":self.costoDisenoCuestionario,
                  "costoMuestreo":self.costoMuestreo,
                  "costoInforme":self.costoInforme,
                  "costoProjectManager":self.costoProjectManager,
                  "totalViaticos":self.totalViaticos,
                  "totalSupervisores":self.totalSupervisores,
                  "totalEncuestadores":self.totalEncuestadores,
                  "totalCampo":self.totalCampo,
                  "totalGabinete":self.totalGabinete,
                  "precioUnitario":self.totalUnitario,
                  "total":self.total,
                  "conOverheadUAQ":self.overheadUAQ
                  
                 
                  
        }
        
    def detalle(self):
        texto1="\n\n Detalle Encuesta\n\n"
        for i in self.dic.keys():
            print(f'{i}: {self.dic[i]}')
            self.midetalle=self.midetalle+'{}: {}.\n'.format(i,self.dic[i])
        self.midetalle=texto1+self.midetalle
        
    def resumen(self):
        print(f'Realización de {self.cuantasVecesSeHaraLaEncuesta} encuesta con muestra de {self.tamanoMuestra} cuestionarios de máximo {self.numeroDeRectivos} reactivos. El operativo se realizará con {self.personalNecesario} encuestadores y {self.supervisorNecesario} supervisores en campo en el curso de {self.diasDeOperativo} dìas, y  tendrà un costo de ${self.total} pesos (sin contar overhead).')
        self.miresumen='Realización de '+str(self.cuantasVecesSeHaraLaEncuesta)+' encuesta con muestra de '+str(self.tamanoMuestra)+' cuestionarios de máximo '+str(self.numeroDeRectivos)+' reactivos. El operativo se realizará con '+str(self.personalNecesario)+' encuestadores y '+str(self.supervisorNecesario)+' supervisores en campo en el curso de '+str(self.diasDeOperativo)+' dìas, y  tendrà un costo de $'+str(self.total)+' pesos (sin contar overhead).'
    

