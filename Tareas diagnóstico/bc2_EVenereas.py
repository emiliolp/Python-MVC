#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
Created on Sun Jan 19 12:19:10 2014

@author: Pablo Garci­a Tamarit
"""
class Observable():
	''' Valores que tiene cada sintoma '''
	def __init__(self,nombre=None,tipo=None,valoresPermitidos=None,valor=None):
		self.nombre=nombre
		self.valor=valor
  		self.tipo=tipo
		self.valoresPermitidos=valoresPermitidos

class Fiebre (Observable):
	''' Sintoma fiebre '''
	def __init__(self, valor = None):
		nombre = "Fiebre"
		tipo = "boolean"
		valoresPermitidos = None
		Observable.__init__(self, nombre, tipo, valor, valoresPermitidos)
		self.valor = valor

class DolorCabeza (Observable):
	''' Sintoma Dolor de cabeza'''
	def __init__(self, valor = None):
		nombre = "Dolor de Cabeza"
		tipo = "boolean"
		valoresPermitidos = None
		Observable.__init__(self, nombre, tipo, valor, valoresPermitidos)
		self.valor = valor

class MalestarGeneral (Observable):
	''' Sintoma Malestar General '''
	def __init__(self, valor = None):
		nombre = "Malestar en General"
		tipo = "boolean"
		valoresPermitidos = None
		Observable.__init__(self, nombre, tipo, valor, valoresPermitidos)
		self.valor = valor

class Depresion (Observable):
	''' Sintoma Depresion '''
	def __init__(self, valor = None):
		nombre = "Depresion"
		tipo = "boolean"
		valoresPermitidos = None
		Observable.__init__(self, nombre, tipo, valor, valoresPermitidos)
		self.valor = valor

class Infertilidad (Observable):
	''' Sintoma Infertilidad '''
	def __init__(self, valor = None):
		nombre = "Infertilidad"
		tipo = "boolean"
		valoresPermitidos = None
		Observable.__init__(self, nombre, tipo, valor, valoresPermitidos)
		self.valor = valor

class Vomitos (Observable):
	''' Sintomas de Vomitos '''
	def __init__(self, valor = None):
		nombre = "Vomitos"
		tipo = "boolean"
		valoresPermitidos = None
		Observable.__init__(self, nombre, tipo, valor, valoresPermitidos)
		self.valor = valor

class Diarrea (Observable):
	''' Sintoma de Diarrea '''
	def __init__(self, valor = None):
		nombre = "Diarrea"
		tipo = "boolean"
		valoresPermitidos = None
		Observable.__init__(self, nombre, tipo, valor, valoresPermitidos)
		self.valor = valor

class HemorragiaGenitales (Observable):
	''' Sintoma Hemorragia en los Genitales '''
	def __init__(self, valor = None):
		nombre = "Hemorragia en los Genitales"
		tipo = "boolean"
		valoresPermitidos = None
		Observable.__init__(self, nombre, tipo, valor, valoresPermitidos)
		self.valor = valor

class Sarpullidos (Observable):
	''' Sintomas de Sarpullidos '''
	def __init__(self, valor = None):
		nombre = "Sarpullidos en la Piel Genitales"
		tipo = "boolean"
		valoresPermitidos = None
		Observable.__init__(self, nombre, tipo, valor, valoresPermitidos)
		self.valor = valor


class VerrugasGenitales (Observable):
	''' Sintoma de Verrugas en los genitales '''
	def __init__(self, valor = None):
		nombre = "Verrugas Genitales"
		tipo = "boolean"
		valoresPermitidos = None
		Observable.__init__(self, nombre, tipo, valor, valoresPermitidos)
		self.valor = valor

class InflamacionGangliosLinfaticos (Observable):
	''' Sintoma de InflamaciÃ³n de Ganglios Linfaticos '''
	def __init__(self, valor = None):
		nombre = "Inflamacion Ganglios Linfaticos"
		tipo = "boolean"
		valoresPermitidos = None
		Observable.__init__(self, nombre, tipo, valor, valoresPermitidos)
		self.valor = valor

class DolorOrinar (Observable):
	''' Sintoma de Dolor al Orinar '''
	def __init__(self, valor = None):
		nombre = "Dolor al Orinar"
		tipo = "boolean"
		valoresPermitidos = None
		Observable.__init__(self, nombre, tipo, valor, valoresPermitidos)
		self.valor = valor

def creaObservable(tp):
    '''Crea una instancia de un observable si la tupla coincide con la base de conocimiento
    . Si la observable es correcta devuelve una instancia de la observable.
    '''
    
    if tp[0]==u'Fiebre':
        ob=Fiebre(tp[1])
        if tp[1]=='True':
          ob.valor=True
        return ob
    elif tp[0]==u'Dolor de Cabeza':
        ob=DolorCabeza(tp[1])
        if tp[1]=='True':
            ob.valor=True
        return ob
    elif tp[0]==u'Malestar en General':
        ob=MalestarGeneral(tp[1])
        if tp[1]=='True':
            ob.valor=True
        return ob
    elif tp[0]==u'Depresion':
        ob=Depresion(tp[1])
        if tp[1] in ob.valoresPermitidos:
            ob.valor=tp[1]
            return ob
    elif tp[0]==u'Infertilidad':
        ob=Infertilidad(tp[1])
        if tp[1]=='True':
            ob.valor=True
        return ob
    elif tp[0]==u'Vomitos':
        ob=Vomitos(tp[1])
        if tp[1]=='True':
            ob.valor=True
        return ob
    elif tp[0]==u'Diarrea':
        ob=Diarrea(tp[1])
        if tp[1]=='True':
            ob.valor=True
        return ob
    elif tp[0]==u'Hemorragia en los Genitales':
        ob=HemorragiaGenitales(tp[1])
        if tp[1]=='True':
            ob.valor=True
        return ob
    elif tp[0]==u'Sarpullidos en la Piel Genitales':
        ob=Sarpullidos(tp[1])
        if tp[1]=='True':
            ob.valor=True
        return ob
    elif tp[0]==u'Verrugas Genitales':
        ob=VerrugasGenitales(tp[1])
        if tp[1]=='True':
            ob.valor=True
        return ob
    elif tp[0]==u'Inflamacion Ganglios Linfaticos':
        ob=InflamacionGangliosLinfaticos(tp[1])
        if tp[1]=='True':
            ob.valor=True
        return ob
    elif tp[0]==u'Dolor al Orinar':
        ob=DolorOrinar(tp[1])
        if tp[1]=='True':
            ob.valor=True
        return ob
    return None


def observables ():
	''' Variables de todos los observables '''
	observables = []
	observables.append (Fiebre ())
	observables.append (DolorCabeza ())
	observables.append (MalestarGeneral ())
	observables.append (Depresion ())
	observables.append (Infertilidad ())
	observables.append (Vomitos ())
	observables.append (Diarrea ())
	observables.append (HemorragiaGenitales ())
	observables.append (Sarpullidos ())
	observables.append (VerrugasGenitales ())
	observables.append (InflamacionGangliosLinfaticos ())
	observables.append (DolorOrinar ())
	
	return observables

class Enfermedad():
    	''' Valores que tiene enfermedad '''
	def __init__(self,nombre):
		self.nombre=nombre

class Sida(Enfermedad):
	''' Enfermedad Sida, sus Sintomas y Ayuda '''
	def __init__(self):
            fiebre=Fiebre(True)
            dolorCabeza=DolorCabeza(True)
            malestarGeneral=MalestarGeneral(True)
            depresion=Depresion(True)
            infertilidad=Infertilidad(True)
            vomitos=Vomitos(True)
            diarrea=Diarrea(True)
            inflamacionGangliosLinfaticos=InflamacionGangliosLinfaticos(True)
            self.debePresentar=[fiebre, dolorCabeza, malestarGeneral, depresion,infertilidad, vomitos, diarrea, inflamacionGangliosLinfaticos]
            self.ayuda=" No se cuenta con una vacuna que cure el sida. En la actualidad se trata con medicamentos antirretrovirales, para mejorar la respuesta inmunitaria y con otros medicamentos que ayudan a combatir las infecciones oportunistas."
            Enfermedad.__init__(self,nombre=u'Sida (VIH)')


class Clamidias (Enfermedad):
	''' Enfermedad Clamidias, sus Sintomas y Ayuda '''
	def __init__(self):
		
		dolorOrinar = DolorOrinar(True)
		self.debePresentar = [dolorOrinar]
		self.ayuda = "La infeccion debe desaparecer en 1 o 2 semanas con un buen tratamiento de antibioticos. Todos los companeros sexuales deberian tambien ser tratados, aunque no tengan si­ntomas."
		Enfermedad.__init__(self, nombre = "Infeccion por clamidias")


class HerpesGenital (Enfermedad):
	''' Enfermedad Herpes Genital, sus Sintomas y Ayuda '''
	def __init__(self):
		
		fiebre = Fiebre(True)
		verrugas = VerrugasGenitales(True)
		sarpullidos = Sarpullidos(True)
		self.debePresentar = [fiebre, verrugas, sarpullidos]
		self.ayuda = "El tratamiento del herpes genital no cura la enfermedad pero mejora los si­ntomas. Los banos calientes pueden aliviar el dolor asociado a las lesiones genitales. Tambien se recomienda una limpieza muy suave con agua y jabon. "
		Enfermedad.__init__(self, nombre = "Herpes Genital")


class Gonorrea (Enfermedad):
	''' Enfermedad Gonorrea, sus Sintomas y Ayuda '''
	def __init__(self):

		dolorOrinar = DolorOrinar(True)
		sarpullidos = Sarpullidos(True)
		verrugas = VerrugasGenitales(True)	
		self.debePresentar = [dolorOrinar, sarpullidos, verrugas]
		self.ayuda = "La gonorrea es muy facil de curar con medicamentos."
		Enfermedad.__init__(self, nombre = "Gonorrea")


class Sifilis(Enfermedad):
	''' Enfermedad Sifilis, sus Sintomas y Ayuda '''
	def __init__(self):
		
		fiebre = Fiebre(True)
		dolorCabeza = DolorCabeza(True)
		inflamacionGangliosLinfaticos = InflamacionGangliosLinfaticos (True)
		verrugas = VerrugasGenitales(True)
		malestarGeneral = MalestarGeneral(True)

		self.debePresentar = [fiebre, dolorCabeza, inflamacionGangliosLinfaticos, verrugas, malestarGeneral]
		self.ayuda = "Normalmente se trata con penicilina, pero pueden usarse otros antibioticos para los pacientes alergicos a la penicilina."
		Enfermedad.__init__(self, nombre = "Sifilis")


class Triconomiasis(Enfermedad):
	''' Enfermedad Triconomiasis, sus Sintomas y Ayuda '''
	def __init__(self):
		
		dolorOrinar = DolorOrinar(True)
		self.debePresentar = [dolorOrinar]
		self.ayuda = "Para evitar nuevas infecciones, la pareja sexual debe tratarse tambien."
		Enfermedad.__init__(self, nombre = "Triconomiasis")



def hipotesis():
    ''' Variables de las enfermedas dandoles el valor de su clase propia de enfermedad (lista las enfermedades) '''
    sida=Sida()
    clamidias = Clamidias ()
    herpesGenital = HerpesGenital ()
    gonorrea = Gonorrea ()
    sifilis = Sifilis ()
    triconomiasis = Triconomiasis ()
    lHp = [sida, clamidias, herpesGenital, gonorrea, sifilis, triconomiasis]
    return lHp