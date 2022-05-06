import math

class GrupoFocal:
    def __init__(self,cuantos=4,minutos=	45,asistentes=	6,porcentajeValido=.75,factorDeTranscripcion=	4,
                costoDirectorMinuto=	5.178,costoRelatorMinuto=	1.852,material=	200):
        self.cuantos=cuantos
        self.minutos=minutos
        self.asistentes=asistentes
        self.porcentajeValido=porcentajeValido
        self.factorDeTranscripcion=factorDeTranscripcion
        self.costoDirectorMinuto=costoDirectorMinuto
        self.costoRelatorMinuto=costoRelatorMinuto
        self.costoDirectorMinutoAjustado=0
        self.costoRelatorMinutoAjustado=0
        self.x=0
        if self.asistentes==6:
            self.costoDirectorMinutoAjustado=self.costoDirectorMinuto
            self.costoRelatorMinutoAjustado=self.costoRelatorMinuto
        else:
            self.x=(self.asistentes-6)*.05
            self.costoDirectorMinutoAjustado=self.costoDirectorMinuto+(self.x*self.costoDirectorMinuto)
            self.costoRelatorMinutoAjustado=self.costoRelatorMinuto+(self.x*self.costoRelatorMinuto)
        self.material=material
        self.tiempoDeTranscripcion=math.ceil(self.minutos*self.factorDeTranscripcion*porcentajeValido)
        self.costoDirector=self.minutos*self.costoDirectorMinutoAjustado
        self.costoRelatorTranscripcion=self.costoRelatorMinutoAjustado*(self.tiempoDeTranscripcion)
        self.costoAnalisis=(.67*self.costoDirectorMinutoAjustado)*(self.minutos*self.porcentajeValido)
        self.costoUnitario=self.costoAnalisis+self.costoDirector+self.costoRelatorTranscripcion+self.material
        self.costoTotal=self.cuantos*self.costoUnitario
        self.costoUAQ=math.ceil(self.costoTotal/.7)
        self.miresumen=""
        self.midetalle=""
        self.dic={
        "Aumento al costo de personal por minuto por aumento en el numero de asistentes ":self.x,
        "minutos":self.minutos,
        "asistentes":self.asistentes,
        "porcentajeValido":self.porcentajeValido,
        "factorDeTranscripcion":self.factorDeTranscripcion,
        "costoDirectorMinuto":self.costoDirectorMinuto,
        "costoRelatorMinuto":self.costoRelatorMinuto,
        "costoDirectorMinutoAjustadoXParticipantes":self.costoDirectorMinutoAjustado,
        "costoRelatorMinutoAjustadoXParticipantes":self.costoRelatorMinutoAjustado,
        "material":self.material,
        "tiempoDeTranscripcion":self.tiempoDeTranscripcion,
        "costoDirector":self.costoDirector,
        "costoRelatorTranscripcion":self.costoRelatorTranscripcion,
        "costoAnalisis":self.costoAnalisis,
        "costo unitario": self.costoUnitario,
        "costo total":self.costoTotal,
        "costo UAQ":self.costoUAQ}

    def detalle(self):
        texto1="\n\n Detalle Grupos Focales\n\n"
        for i in self.dic.keys():
            print(f'{i}: {self.dic[i]}')
            self.midetalle=self.midetalle+'{}: {}.\n'.format(i,self.dic[i])
        self.midetalle=texto1+self.midetalle
        
    def resumen(self):
        print(f'Aplicación de {self.cuantos} grupos focales, con duración de {self.minutos} minutos, y un máximo de {self.asistentes} asistentes. Costo (sin overhead): ${self.costoTotal} pesos.')
        self.miresumen="Aplicación de "+str(self.cuantos)+" grupos focales, con duración de "+str(self.minutos)+" minutos, y un máximo de "+ str(self.asistentes)+" asistentes. Costo (sin overhead): $"+ str(self.costoTotal) +" pesos."


