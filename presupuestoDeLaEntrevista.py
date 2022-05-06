import math

class Entrevista:
    def __init__(self,minutos=45,cuantas=12,costoMinuto=1.7009,minutosPorItem=6):
        self.minutos=minutos
        self.cuantas=cuantas
        self.costoMinuto=costoMinuto
        self.minutosPorItem=minutosPorItem
        self.itemsPosibles=math.floor(self.minutos/minutosPorItem)
        self.tiempoTranscripcion=self.minutosPorItem*4
        self.tiempoEtiquetado=self.minutosPorItem*2
        self.tiempoTotalPorItem=self.minutosPorItem+self.tiempoTranscripcion+self.tiempoEtiquetado
        self.tiempoRealEntrevista=self.itemsPosibles*self.tiempoTotalPorItem
        self.costoEntrevista=self.tiempoRealEntrevista*self.costoMinuto
        self.costoProyectoEntrevistas=self.cuantas*self.costoEntrevista
        self.costoUAQ=self.costoProyectoEntrevistas/.7
        self.miresumen=""
        self.midetalle=""
        self.dic={
            "minutos":self.minutos,
            "cuantas":self.cuantas,
            "costoMinuto":self.costoMinuto,
            "minutosPorItem":self.minutosPorItem,
            "itemsPosibles":self.itemsPosibles,
            "tiempoTranscripcion":self.tiempoTranscripcion,
            "tiempoEtiquetado":self.tiempoEtiquetado,
            "tiempoTotalPorItem":self.tiempoTotalPorItem,
            "tiempoRealEntrevista":self.tiempoRealEntrevista,
            "costoEntrevista":self.costoEntrevista,
            "costoProyectoEntrevistas":self.costoProyectoEntrevistas,
            "costoUAQ":self.costoUAQ
        }
    
    def detalle(self):
        texto1="\n\n Detalle Entrevista\n\n"
        for i in self.dic.keys():
            print(f'{i}: {self.dic[i]}')
            self.midetalle=self.midetalle+'{}: {}.\n'.format(i,self.dic[i])
        self.midetalle=texto1+self.midetalle
        
    def resumen(self):
        print(f'Realización de {self.cuantas} entrevistas semiestructuradas, con duración media de {self.minutos} minutos, con transcripcion y etiquetado, y màximo {self.itemsPosibles} items. Costo total: {self.costoProyectoEntrevistas} pesos. ') 
        self.miresumen='Realización de '+str(self.cuantas)+' entrevistas semiestructuradas, con duraciòn media de '+str(self.minutos)+' minutos, con transcripcion y etiquetado, y màximo '+str(self.itemsPosibles)+' items. Costo total (sin overhead): '+str(self.costoProyectoEntrevistas)+' pesos.'
        print(self.miresumen)



