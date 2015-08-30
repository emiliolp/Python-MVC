#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
Created on Sun Jan 19 12:19:10 2014

@author: Manuel Gallego Cerrillo
"""
# Define la clase que representa a los posibles sintomas observables
class Observable():
	''' Valores que debe tener cada sintoma '''
	def __init__(self,nombre=None,tipo=None,valoresPermitidos=None,valor=None):
		self.nombre=nombre
		self.valor=valor
		self.valoresPermitidos=valoresPermitidos

class ApagadoMotor(Observable):
	''' Sintoma: El motor se apaga cuando no debería '''
	def __init__(self, valor = None):
		nombre = "Motor se apaga"
		tipo = "boolean"
		valoresPermitidos = None
		Observable.__init__(self, nombre, tipo, valor, valoresPermitidos)
		self.valor = valor

class RalentiIrregular (Observable):
	''' Sintoma: El motor presenta un ralentí irregular '''
	def __init__(self, valor = None):
		nombre = "Ralenti irregular"
		tipo = "boolean"
		valoresPermitidos = None
		Observable.__init__(self, nombre, tipo, valor, valoresPermitidos)
		self.valor = valor

class RegimenRevolucionesExcesivo (Observable):
	''' Sintoma: El motor presenta un regimen de giro excesivo cuando se pone en marcha '''
	def __init__(self, valor = None):
		nombre = "Excesivo regimen de revoluciones"
		tipo = "boolean"
		valoresPermitidos = None
		Observable.__init__(self, nombre, tipo, valor, valoresPermitidos)
		self.valor = valor

class TironesEnFrio (Observable):
	''' Sintoma: El coche pega tirones cuando se encuentra a temperatura baja operativa '''
	def __init__(self, valor = None):
		nombre = "Tirones en frio"
		tipo = "boolean"
		valoresPermitidos = None
		Observable.__init__(self, nombre, tipo, valor, valoresPermitidos)
		self.valor = valor

class FaltaPotencia (Observable):
	''' Sintoma: El coche presenta una falta de potencia al acelerar '''
	def __init__(self, valor = None):
		nombre = "Falta de potencia"
		tipo = "boolean"
		valoresPermitidos = None
		Observable.__init__(self, nombre, tipo, valor, valoresPermitidos)
		self.valor = valor

class AvisoTemperaturaMotor (Observable):
	''' Sintoma: Se ha encendido una luz de aviso de temperatura excesiva en el motor '''
	def __init__(self, valor = None):
		nombre = "Indicador temperatura motor"
		tipo = "boolean"
		valoresPermitidos = None
		Observable.__init__(self, nombre, tipo, valor, valoresPermitidos)
		self.valor = valor

class ExcesoConsumoAceite (Observable):
	''' Sintoma: El motor presenta un consumo de acite excesivo '''
	def __init__(self, valor = None):
		nombre = "Exceso consumo aceite"
		tipo = "boolean"
		valoresPermitidos = None
		Observable.__init__(self, nombre, tipo, valor, valoresPermitidos)
		self.valor = valor

class AvisoNivelAceite (Observable):
	''' Sintoma: Se ha encendido una luz de aviso de nivel de aceite bajo '''
	def __init__(self, valor = None):
		nombre = "Indicador nivel aceite"
		tipo = "boolean"
		valoresPermitidos = None
		Observable.__init__(self, nombre, tipo, valor, valoresPermitidos)
		self.valor = valor

# Devuelve la lista de observables de la base de conocimiento
def observables ():
	''' Crea una instancia de todos los observables almacenados en la base de conocimiento '''
	observables = []
	observables.append (ApagadoMotor ())
	observables.append (RalentiIrregular ())
	observables.append (RegimenRevolucionesExcesivo ())
	observables.append (TironesEnFrio ())
	observables.append (FaltaPotencia ())
	observables.append (AvisoTemperaturaMotor ())
	observables.append (ExcesoConsumoAceite ())
	observables.append (AvisoNivelAceite ())
	
	return observables

# Define la clase que representa a las posibles averias
class Averia():
	''' Valores que debe tener cada averia '''
	def __init__(self,nombre):
		self.nombre=nombre

# Averia: Admision obstruida
class AdmisionObstruida(Averia):
	''' Averia: Hay residuos que obstuyen la admisión de aire del motor '''
	def __init__(self):
	
            apagadoMotor=ApagadoMotor(True)
            ralentiIrregular=RalentiIrregular(True)
            regimenRevolucionesExcesivo=RegimenRevolucionesExcesivo(True)
            self.debePresentar=[apagadoMotor,ralentiIrregular,regimenRevolucionesExcesivo]
            self.ayuda="Verificar entradas de aire a la admision. Si estan obstruidas pueden provocar que se regule el ralenti muy bajo haciendo que el motor se pare."
            Averia.__init__(self,nombre=u'Admision obstruida'.encode(encoding='iso-8859-1'))

# Averia: Fallo en la valvula estabilizadora de ralenti
class FalloValvulaRalenti (Averia):
	''' Averia: La valvula estabilizadora del ralenti esta fallando '''
	def __init__(self):
		Averia.__init__(self, nombre = u'Fallo en la valvula estabilizadora de ralenti'.encode(encoding='iso-8859-1'))
		apagadoMotor = ApagadoMotor (True)
		ralentiIrregular = RalentiIrregular (True)
		regimenRevolucionesExcesivo = RegimenRevolucionesExcesivo (True)
		self.debePresentar = [apagadoMotor, ralentiIrregular, regimenRevolucionesExcesivo]
		self.ayuda = "Comprobar si se abre la valvula de forma rapida y total sin engancharse o quedar atascada."

# Averia: Valvulas de admision obstruidas
class ValvulasAdmisionObstruidas (Averia):
	''' Averia: Hay residuos que obstruyen las valvulas de admision '''
	def __init__(self):
		Averia.__init__(self, nombre = u'Valvulas de admision abostruidas'.encode(encoding='iso-8859-1'))
		tironesEnFrio = TironesEnFrio (True)
		faltaDePotencia = FaltaPotencia (True)
		ralentiIrregular = RalentiIrregular (True)
		self.debePresentar = [tironesEnFrio, faltaDePotencia]
		self.ayuda = "Residuos producidos por el combustible obstaculizan las partes bajas de los vastagos de las valvulas de admision, impidiendo que entre suficiente cantidad de aire a los cilindros."

# Averia: Bujias indacuadas
class BujiasInadecuadas (Averia):
	''' Averia: El motor tiene instaladas una bujias inadecuadas '''
	def __init__(self):
		Averia.__init__(self, nombre = u'Bujias inadecuadas'.encode(encoding='iso-8859-1'))
		tironesEnFrio = TironesEnFrio (True)
		faltaDePotencia = FaltaPotencia (True)
		ralentiIrregular = RalentiIrregular (True)
		self.debePresentar = [tironesEnFrio, faltaDePotencia]
		self.ayuda = "Las bujias instaladas son incorrectas para las caracteristicas del motor."

# Averia: Problema con algun manguito del circuito de refrigeracion
class ProblemaManguito (Averia):
	''' Averia: Alguno de los manguitos del circuito de refrigeracion esta en mal estado '''
	def __init__(self):
		Averia.__init__(self, nombre = u'Problema con algun manguito del circuito de refrigeracion'.encode(encoding='iso-8859-1'))
		avisoTemperaturaMotor = AvisoTemperaturaMotor (True)
		self.debePresentar = [avisoTemperaturaMotor]
		self.ayuda = "Alguno de los manguitos del circuito de refrigeracion del motor pueden estar desajustados o danyados, provocando la pérdidad de líquido refrigerante."

# Averia: Problema con el termostato del sistema de refrigeracion
class ProblemaTermostato (Averia):
	''' Averia: El termostato del sistema de refrigeracion esta fallando '''
	def __init__(self):
		Averia.__init__(self, nombre = u'Problema termostato del sistema de refrigeracion'.encode(encoding='iso-8859-1'))
		avisoTemperaturaMotor = AvisoTemperaturaMotor (True)
		self.debePresentar = [avisoTemperaturaMotor]
		self.ayuda = "El termostato del sistema de refrigeracion funciona incorrectamente, haciendo que el sistema de refrigeracion funcione de forma incorrecta provocando el sobrecalentamiento del motor."

# Averia: Fisura en la junta de la culata
class FisuraJuntaCulata (Averia):
	''' Averia: Hay una fisura en la junta de la culata '''
	def __init__(self):
		Averia.__init__(self, nombre = u'Fisura junta de la culata'.encode(encoding='iso-8859-1'))
		avisoTemperaturaMotor = AvisoTemperaturaMotor (True)
		self.debePresentar = [avisoTemperaturaMotor]
		self.ayuda = "Una fisura en la junta de la culata provoca la perdida de liquido refrigerante, haciendo que el motor se sobrecaliente por falta de liquido."

# Averia: Filtracion de aceite por los retenes
class FiltracionAceiteRetenes (Averia):
	''' Averia: Se filtra aceite a la camara de combustion a traves de los segmentos de los pistones '''
	def __init__(self):
		Averia.__init__(self, nombre = u'Filtracion de aceite por los retenes'.encode(encoding='iso-8859-1'))
		avisoNivelAceite = AvisoNivelAceite (True)
		self.debePresentar = [avisoNivelAceite]
		self.ayuda = "La carbonizacion de los retenes provoca la filtracion de aceite."

# Devuelve una lista con las averias almacenadas en la base de conocimiento
def hipotesis():
    ''' Crea una instancia de cada tipo de Averia almacenada en la base de conocimiento '''
    admisionObstruida=AdmisionObstruida()
    falloValvulaRalenti = FalloValvulaRalenti ()
    valvulasAdmisionObstruidas = ValvulasAdmisionObstruidas ()
    bujiasInadecuadas = BujiasInadecuadas ()
    problemaManguito = ProblemaManguito ()
    problemaTermostato = ProblemaTermostato ()
    fisuraJuntaCulata = FisuraJuntaCulata ()
    filtracionAceiteRetenes = FiltracionAceiteRetenes ()
    lHp = [admisionObstruida, falloValvulaRalenti, valvulasAdmisionObstruidas, bujiasInadecuadas, problemaManguito, problemaTermostato, fisuraJuntaCulata, filtracionAceiteRetenes]
    return lHp
    
def creaObservable(tp):
    '''Crea una instancia de un observable si la tupla coincide con la base de conocimiento
    . Si la observable es correcta devuelve una instancia de la observable.
    Corregir. Hay que mejorar esta función'''
    
    print tp
    if tp[0]==u'Motor se apaga':
        ob=ApagadoMotor(tp[1])
        if tp[1]=='True':
            ob.valor=True
        return ob
    elif tp[0]==u'Ralenti irregular':
        ob=RalentiIrregular(tp[1])
        if tp[1]=='True':
            ob.valor=True
        return ob
    elif tp[0]==u'Excesivo regimen de revoluciones':
        ob=RegimenRevolucionesExcesivo(tp[1])
        if tp[1]=='True':
            ob.valor=True
        return ob
    elif tp[0]==u'Tirones en frio':
        ob=TironesEnFrio(tp[1])
        if tp[1]=='True':
            ob.valor=True
        return ob
    elif tp[0]==u'Falta de potencia':
        ob=FaltaPotencia(tp[1])
        if tp[1]=='True':
            ob.valor=True
        return ob
    elif tp[0]==u'Indicador temperatura motor':
        ob=AvisoTemperaturaMotor(tp[1])
        if tp[1]=='True':
            ob.valor=True
        return ob
    elif tp[0]==u'Exceso consumo aceite':
        ob=ExcesoConsumoAceite(tp[1])
        if tp[1]=='True':
            ob.valor=True
        return ob
    elif tp[0]==u'Indicador nivel aceite':
        ob=AvisoNivelAceite(tp[1])
        if tp[1]=='True':
            ob.valor=True
        return ob
    return None
