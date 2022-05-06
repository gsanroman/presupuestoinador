import math

class SitioWeb:
    def __init__(self,rAvanzado=True,rBasico=False,htmlCSSjs=True,jsAvanzado=True,leaflet=True,php=False,mysqlAvanzado=False,elektron=True):
        self.rAvanzado=rAvanzado
        self.rBasico=rBasico
        self.htmlCSSjs=htmlCSSjs
        self.jsAvanzado=jsAvanzado
        self.leaflet=leaflet
        self.php=php
        self.mysqlAvanzado=mysqlAvanzado
        self.elektron=elektron
        self.costoTotal=0
        self.miresumen=""
        self.midetalle=""
        self.cuiales=""
        self.dic={}
        self.costoUAQ=0
        self.costoSitioWeb=0
    
    def costosFijosWeb(self,c_rAvanzado=3000,c_rBasico=2000,c_htmlCSSjs=2000,c_jsAvanzado=1500,c_leaflet=3000,c_php=2500,c_mysqlAvanzado=2500,c_elektron=1000):
        self.c_rAvanzado=c_rAvanzado
        self.c_rBasico=c_rBasico
        self.c_htmlCSSjs=c_htmlCSSjs
        self.c_jsAvanzado=c_jsAvanzado
        self.c_leaflet=c_leaflet
        self.c_php=c_php
        self.c_mysqlAvanzado=c_mysqlAvanzado
        self.c_elektron=c_elektron
        if self.rAvanzado==True:
            self.costoTotal=self.costoTotal+self.c_rAvanzado
        if self.rBasico==True:
            self.costoTotal=self.costoTotal+self.c_rBasico
        if self.htmlCSSjs==True:
            self.costoTotal=self.costoTotal+self.c_htmlCSSjs
        if self.jsAvanzado==True:
            self.costoTotal=self.costoTotal+self.c_jsAvanzado
        if self.leaflet==True:
            self.costoTotal=self.costoTotal+self.c_leaflet
        if self.php==True:
            self.costoTotal=self.costoTotal+self.c_php
        if self.mysqlAvanzado==True:
            self.costoTotal=self.costoTotal+self.c_mysqlAvanzado
        if self.elektron==True:
            self.costoTotal=self.costoTotal+self.c_elektron
        self.costoSitioWeb=self.costoTotal
        self.costoUAQ=math.ceil(self.costoTotal/.7)
        self.miresumen=""
        self.midetalle=""
        self.cuiales=""
        self.dic={"Incluye R Avanzado":self.rAvanzado,
        "Incluye R Basico":self.rBasico,
        "Incluye html-CSS-js":self.htmlCSSjs,
        "Incluye js Avanzado":self.jsAvanzado,
        "Incluye leaflet":self.leaflet,
        "Incluye php":self.php,
        "mysqlAvanzado":self.mysqlAvanzado,
        "elektron":self.elektron,
        "costo r Avanzado":self.c_rAvanzado,
        "costo rBasico":self.c_rBasico,
        "costo htmlCSSjs":self.c_htmlCSSjs,
        "costo jsAvanzado":self.c_jsAvanzado,
        "costo leaflet":self.c_leaflet,
        "costo php":self.c_php,
        "costo mysql Avanzado":self.c_mysqlAvanzado,
        "costo elektron":self.c_elektron,
        "costo total":self.costoSitioWeb
        }
    
    def detalle(self): 
        texto1="\n\n Detalle Sitio web\n\n"
        for i in self.dic.keys():
            print(f'{i}: {self.dic[i]}')
            self.midetalle=self.midetalle+'{}: {}.\n'.format(i,self.dic[i])
        self.midetalle=texto1+self.midetalle
        
    def resumen(self):
        print(f'Aplicación web. Costo (sin overhead): ${self.costoTotal} pesos.')
        self.miresumen="Aplicación web. Costo (sin overhead): $"+ str(self.costoTotal) +" pesos."


