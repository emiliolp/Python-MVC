#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
Created on Sun Jan 19 12:19:10 2014

@author: Emilio López Piña
"""
import bc2

class MetodoCoberturaCausal():
    '''Método de cobertura causal para la tarea de diagnóstico'''
    def __init__(self,quejas):
        self.quejas=quejas
        self.explicacion=''
        self.diferencial=[]
        self.diagnostico=[]
        
    def execute(self):
        #Obtiene conjunto de hipótesis
        self.explicacion+=u'Ejecutando método cobertura causal. Obtenemos conjunto diferencial:\n\n'.encode(encoding='iso-8859-1')
        cc=Cubrir(self.quejas)
        self.diferencial=cc.execute()
        
        for hipotesis in self.diferencial:
            self.explicacion+=hipotesis.nombre.encode(encoding='iso-8859-1')+'\n'.encode(encoding='iso-8859-1')
        
        while len(self.diferencial)>0:
            seleccionar=Seleccionar(self.diferencial)
            hipotesis=seleccionar.execute()
            self.explicacion+=u'\n\nProbamos la hipótesis de '.encode(encoding='iso-8859-1')
            self.explicacion+=hipotesis.nombre.encode(encoding='iso-8859-1')
            #verificar
            verifica=Verificar(hipotesis,self.quejas)
            verifica.execute()
            if verifica.resultado==False:#Si el resultado de la verificación elimina la hipótesis del conjunto diferencial
                self.diferencial.remove(hipotesis)
            else:
                self.diagnostico.append(hipotesis)#Añade a la lista de diagnósticos compatibles la hipotesis
                self.diferencial.remove(hipotesis)#Suprime la hipótesis evaluada
            self.explicacion+=verifica.justificacion.encode(encoding='iso-8859-1')
         
        print self.explicacion
        print "\nDiagnóstico:"
        for j in range(len (self.diagnostico)):
            print self.diagnostico[j].nombre
            
        print "\nFIN"
        
     
class Inferencia():
    def __init__(self):
        pass
    def execute(self):
        pass
    
class Cubrir(Inferencia):
    '''
    Se presenta una lista de propiedades y proporciona una lista de posibles 
    hipotesis
    '''
    def __init__(self,quejas):
        Inferencia.__init__(self)
        self.quejas=quejas
        self.listaHipotesis=[]
    def execute(self):
        '''
        Genera las clases candidatas a ser solucion
        '''
        hipotesis=bc2.hipotesis()
        self.listaHipotesis=hipotesis
        return hipotesis
        
class Seleccionar(Inferencia):
    '''
    Selecciona hipotesis del conjunto diferencial
    '''
    def __init__(self,hipotesis):
        Inferencia.__init__(self)
        self.hipotesis=hipotesis
    def execute(self):
        if len(self.hipotesis)>0:
            return self.hipotesis[0]
        else:
            return None
            
class Especificar(Inferencia):
    '''    
    Devuelve un atributo cuyo valor (desconocido)
    sera de utilidad para distinguir entre las clases candidatas
    '''
    def __init__(self,quejas,indice):
        Inferencia.__init__(self)
        self.quejas=quejas
        self.indice=indice
    def execute(self):
        atributo=self.quejas[self.indice]
        return atributo
        
class Obtener(Inferencia):
    '''
    Obtiene el valor asociado a un atributo en el
    objeto a clasificar
    '''
    def __init__(self,caracteristica):
        Inferencia.__init__(self)
        self.caracteristica=caracteristica
    def execute(self):
        return self.caracteristica.valor

class Verificar(Inferencia):
    '''
    Comprueba si un conjunto de quejas coinciden con un determinada hipotesis
    '''
    def __init__(self,hipotesis,quejas):
        Inferencia.__init__(self)
        self.quejas=quejas
        self.hipotesis=hipotesis
        self.resultado=False
        self.justificacion=''
    def execute(self):
        encontrado=0
        aux=[]
        aux=self.hipotesis.debePresentar
            
        print "nueva hipotesis"
        for i in range(len(self.quejas)):
            #igual=False
            #for j in range(len (aux)):
            #borrar las hipotesis que se encuentran, cambiar el for por 
            #un while que avance cuando no se ha borrado elemento
            # de debePresentar
            #for j in range(len(self.hipotesis.debePresentar)):
            j=0
            while(len(self.hipotesis.debePresentar)>0):
                if self.quejas[i].nombre==self.hipotesis.debePresentar[j].nombre:
                    if self.quejas[i].valor==self.hipotesis.debePresentar[j].valor:                        
                        encontrado+=1
                        if self.hipotesis.debePresentar[-1]==self.hipotesis.debePresentar[j]:
                            self.hipotesis.debePresentar.remove(self.hipotesis.debePresentar[j])
                            break;
                        else:
                            self.hipotesis.debePresentar.remove(self.hipotesis.debePresentar[j])
                        if len (self.hipotesis.debePresentar)==0 or self.hipotesis.debePresentar[-1]==self.hipotesis.debePresentar[j]: 
                            break
                    else:
                        if self.hipotesis.debePresentar[-1]==self.hipotesis.debePresentar[j]:
                            break
                        else:
                            j+=1
                else:
                    if self.hipotesis.debePresentar[-1]==self.hipotesis.debePresentar[j]:
                            break
                    else:
                        j+=1
            #if not igual:
            #    print "................."
            #    print "no presenta"
            #    print aux[i].nombre
#borrar las que coinciden y dejar el resto, se obtiene las fallidas
        
        if len(self.quejas)==encontrado:
            self.resultado=True
            self.justificacion+=u'\n    Puede ser '.encode(encoding='iso-8859-1')
            self.justificacion+=self.hipotesis.nombre
        else:
            self.justificacion+=u'\n    No puede ser '.encode(encoding='iso-8859-1')
            self.justificacion+=self.hipotesis.nombre
            self.justificacion+=u', deberia presentar:'.encode(encoding='iso-8859-1')
            for i in range(len(aux)):
                self.justificacion+='\n    -'+aux[i].nombre
        
        return (self.resultado,self.justificacion)
            
def identificaSignosSintomas(ltFallos):
    '''Identifica una lista de tuplas como signos y sintomas (fallos:atributo,valor)
    y compureba que son observables correctas de la base de conocimiento.
    '''
    obs=[]
    for tf in ltFallos:#Comprobar que cada fallo está en la base de conocimiento
        
        ob=bc2.creaObservable(tf)
        print ob
        if not ob==None:
            obs.append(ob)
        else:
            return None
    return obs 
        
if __name__ == '__main__':
    
    if True:
        tironesFrio = bc2.TironesEnFrio (True)
        faltaPotencia=bc2.FaltaPotencia(True)
        mcc=MetodoCoberturaCausal([tironesFrio,faltaPotencia])
        mcc.execute()
