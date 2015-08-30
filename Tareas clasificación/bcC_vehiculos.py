#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

#  Representa las caracteristicas que pueden tener los atributos de un objeto del dominio de la 
# aplicacion. Es necesaria su creacion para el desarrollo de la interfaz del programa, para que
# se puedan mostrar en ella los campos requeridos para la creacion del objeto desconocido a 
# clasificar.
class Atributo ():

    """
    La clase Atributo representa las características que pueden tener los atributos de un objeto del dominio
    de la aplicacion. Es necesaria su creación para el desarrollo de la interfaz del programa, para que
    se puedan mostrar en ella los campos requeridos para la creación del objeto desconocido a clasificar.
    """
 
    def __init__(self, nombre = None, atrib = None, defecto = None, booleano = None, valores = []):
        """
        Constructor de la clase Atributo.
        """
    
        self.nombre = nombre
        self.atrib = atrib
        self.defecto = defecto
        self.booleano = booleano
        self.valores = valores

#  Por cada atributo que puedan tener los objetos del dominio de la aplicacion se crea una clase
# que hereda de la clase Atributo, obligando a todos los atributos de los permisos a tener las
# mismas caracteristicas.

class n_ruedas (Atributo):
    
    """
    Clase que define el numero de ruedas que debe tener el vehiculo
    """
    def __init__(self):
        
        nombre = 'Numero de ruedas'
        atrib = 'n_ruedas'
        defecto = '4'
        Atributo.__init__(self, nombre, atrib, defecto)
        
class vel_max (Atributo):
    
    """
    Clase que define la velocidad maxima permitida
    """
    def __init__(self):
        
        nombre = 'Vel. maxima'
        atrib = 'vel_max'
        defecto = '100'
        Atributo.__init__(self, nombre, atrib, defecto)
        
class n_ejes (Atributo):
    
    """
    Clase que define el numero maximo de ejes que debe tener el vehi�culo
    """
    def __init__(self):
        
        nombre = 'Num. ejes'
        atrib = 'n_ejes'
        defecto = '0'
        Atributo.__init__(self, nombre, atrib, defecto)
        
class pma (Atributo):
    
    """
    Clase que define el peso maximo autorizado que puede transportar el vehi�culo
    """

    def __init__(self):
        
        nombre = 'PMA'
        atrib = 'pma'
        defecto = '0'
        Atributo.__init__(self, nombre, atrib, defecto)
        
class edad (Atributo):
    
    """
    Clase que define la edad mi�nima requerida para obtener el permiso
    """

    def __init__(self):
        
        nombre = 'Edad'
        atrib = 'edad'
        defecto = '16'
        Atributo.__init__(self, nombre, atrib, defecto)
        
class n_asientos (Atributo):
    
    """
    Clase que define el numero maximo de asientos que debe tener el vehi�culo
    """

    def __init__(self):
        
        nombre = 'Num. asientos'
        atrib = 'n_asientos'
        defecto = '1'
        Atributo.__init__(self, nombre, atrib, defecto)
        
class cilindrada (Atributo):
    
    """
    Clase que define la cilindrada maxima que debe tener el vehi�culo
    """

    def __init__(self):
        
        nombre = 'Cilindrada'
        atrib = 'cilindrada'
        defecto = '49'
        Atributo.__init__(self, nombre, atrib, defecto)
        
class potencia (Atributo):
    
    """
    Clase que define la potencia maxima que puede tener el vehi�culo
    """

    def __init__(self):
        
        nombre = 'Potencia'
        atrib = 'potencia'
        defecto = '0'
        Atributo.__init__(self, nombre, atrib, defecto)
        
class sidecar (Atributo):
    
    """
    Clase que define si el permiso autoriza el uso de sidecar
    """

    def __init__(self):
        
        nombre = 'Tiene sidecar'
        atrib = 'sidecar'
        defecto = 'sidecar'
        booleano = 'True'
        Atributo.__init__(self, nombre, atrib, defecto, booleano)

class remolque (Atributo):
    
    """
    Clase que define si el permiso autoriza el uso de remolque
    """

    def __init__(self):
        
        nombre = 'Tiene remolque'
        atrib = 'remolque'
        defecto = 'remolque'
        booleano = 'True'
        Atributo.__init__(self, nombre, atrib, defecto, booleano)
        
class peso_remolque (Atributo):
    
    """
    Clase que define el peso maximo del remolque que puede llevar el vehi�culo
    """

    def __init__(self):
        
        nombre = 'Peso remolque'
        atrib = 'peso_remolque'
        defecto = '0'
        Atributo.__init__(self, nombre, atrib, defecto)
        
class mercancias_peligrosas (Atributo):
    
    """
    Clase que define si el permiso autoriza a transportar mercanci�as peligrosas
    """

    def __init__(self):
        
        nombre = 'Transporte de merc. peligrosa'
        atrib = 'mercancias_peligrosas'
        defecto = 'mercancias'
        booleano = 'True'
        Atributo.__init__(self, nombre, atrib, defecto, booleano)

class transporte_personas (Atributo):
    
    """
    Clase que define si el permiso autoriza a transportar personas
    """

    def __init__(self):
        
        nombre = 'Transporte publico'
        atrib = 'transporte_personas' 
        defecto = 'transporte_p'
        booleano = 'True'
        Atributo.__init__(self, nombre, atrib, defecto, booleano)
    
class transporte_sanitario (Atributo):
    
    """
    Clase que define si el permiso autoriza el transporte sanitario
    """

    def __init__(self):
        
        nombre = 'Transporte sanitario'
        atrib = 'transporte_sanitario' 
        defecto = 'transporte_s'
        booleano = 'True'
        Atributo.__init__(self, nombre, atrib, defecto, booleano)
            
class taxi (Atributo):
    
    """
    Clase que define si el permiso autoriza el uso de taxis
    """

    def __init__(self):
        
        nombre = 'taxi'
        atrib = 'taxi' 
        defecto = 'taxi'
        booleano = 'True'
        Atributo.__init__(self, nombre, atrib, defecto, booleano)

#  Representa las caracteristicas de los atributos que tienen los objetos del dominio
# de la aplicacion que se van a almacenar en la base de conocimiento. Esto es necesario
# para poder realizar de mejor forma el proceso de comparacion de atributos necesario
# para realizar el metodo de clasificacion de la poda en el modelo.
class Caracteristica ():
    
    """
    La clase Caracteri�stica representa las caracteristicas de los atributos que tienen los objetos del dominio
    de la aplicacion que se van a almacenar en la base de conocimiento. Esto es necesario
    para poder realizar de mejor forma el proceso de comparacion de atributos necesario
    para realizar el metodo de clasificacion de la poda en el modelo. 
    """
	
    def __init__(self, nombre = None, valor = None):
    
        self.nombre = nombre
        self.valor = valor

#  Por cada atributo que puedan presentar las clases de objetos del dominio de la aplicaacion
# almacenados en la base de conocimiento se crea una clase que hereda de la clase Caracteristica.
class Ruedas (Caracteristica):
      
    """
    Clase que define el numero de ruedas que debe tener el vehi�culo
    """

    def __init__(self, valor = None):
        
        nombre = 'n_ruedas'
        Caracteristica.__init__(self, nombre, valor)
        self.valor = valor
        
class Velmax (Caracteristica):
    
    """
    Clase que define la velocidad maxima permitida
    """

    def __init__(self, valor = None):
        
        nombre = 'vel_max'
        Caracteristica.__init__(self, nombre, valor)
        self.valor = valor
        
class Ejes (Caracteristica):
    
    """
    Clase que define el numero maximo de ejes que debe tener el vehi�culo
    """

    def __init__(self, valor = None):
        
        nombre = 'n_ejes'
        Caracteristica.__init__(self, nombre, valor)
        self.valor = valor
        
class Pma (Caracteristica):
    
    """
    Clase que define el peso maximo autorizado que puede transportar el vehículo
    """

    def __init__(self, valor = None):
        
        nombre = 'pma'
        Caracteristica.__init__(self, nombre, valor)
        self.valor = valor
        
class Edad (Caracteristica):
    
    """
    Clase que define la edad mínima requerida para obtener el permiso
    """

    def __init__(self, valor = None):
        
        nombre = 'edad'
        Caracteristica.__init__(self, nombre, valor)
        self.valor = valor
        
class Asientos (Caracteristica):
    
    """
    Clase que define el número máximo de asientos que debe tener el vehículo
    """

    def __init__(self, valor = None):
        
        nombre = 'n_asientos'
        Caracteristica.__init__(self, nombre, valor)
        self.valor = valor
        
class Cilindrada (Caracteristica):
    
    """
    Clase que define la cilindrada máxima que debe tener el vehículo
    """

    def __init__(self, valor = None):
        
        nombre = 'cilindrada'
        Caracteristica.__init__(self, nombre, valor)
        self.valor = valor
        
class Potencia (Caracteristica):
    
    """
    Clase que define la potencia máxima que puede tener el vehículo
    """

    def __init__(self, valor = None):
        
        nombre = 'potencia'
        Caracteristica.__init__(self, nombre, valor)
        self.valor = valor
        
class Sidecar (Caracteristica):
    
    """
    Clase que define si el permiso autoriza el uso de sidecar
    """

    def __init__(self, valor = None):
        
        nombre = 'sidecar'
        Caracteristica.__init__(self, nombre, valor)
        self.valor = valor

class Remolque (Caracteristica):
    
    """
    Clase que define si el permiso autoriza el uso de remolque
    """

    def __init__(self, valor = None):
        
        nombre = 'remolque'
        Caracteristica.__init__(self, nombre, valor)
        self.valor = valor        

class PesoRemolque (Caracteristica):
    
    """
    Clase que define el peso máximo del remolque que puede llevar el vehículo
    """

    def __init__(self, valor = None):
        
        nombre = 'peso_remolque'
        Caracteristica.__init__(self, nombre, valor)
        self.valor = valor
        
class MercanciasPeligrosas (Caracteristica):
    
    """
    Clase que define si el permiso autoriza a transportar mercancías peligrosas
    """

    def __init__(self, valor = None):
        
        nombre = 'mercancias_peligrosa'
        Caracteristica.__init__(self, nombre, valor)
        self.valor = valor

class TransportePersonas (Caracteristica):
    
    """
    Clase que define si el permiso autoriza a transportar personas
    """

    def __init__(self, valor = None):
        
        nombre = 'transporte_publico'
        Caracteristica.__init__(self, nombre, valor)
        self.valor = valor    

class TransporteSanitario (Caracteristica):
    
    """
    Clase que define si el permiso autoriza el transporte sanitario
    """

    def __init__(self, valor = None):
        
        nombre = 'transporte_sanitario'
        Caracteristica.__init__(self, nombre, valor)
        self.valor = valor

class Taxi (Caracteristica):
     """
     Clase que define si el permiso autoriza el uso de taxi
     """
     
     def __init__(self, valor = None):

        nombre = 'taxi'
        Caracteristica.__init__(self, nombre, valor)
        self.valor = valor
 
#  Este metodo sirve para obtener una lista de todos los atributos que puede presentar un objeto
# en el dominio de la aplicacion. La utiliza la Vista para mostrar los datos en la interfaz de usuario.
def listaAtributos ():

    """
    Este metodo sirve para obtener una lista de todos los atributos que puede presentar un objeto
    en el dominio de la aplicacion. La utiliza la Vista para mostrar los datos en la interfaz de usuario.
    """

	# Devuelve la lista de observables de la base del conocimiento
    atributos = []
    atributos.append (n_ruedas())
    atributos.append (vel_max())
    atributos.append (n_ejes())
    atributos.append (pma())
    atributos.append (edad())
    atributos.append (n_asientos())
    atributos.append (cilindrada())
    atributos.append (potencia())
    atributos.append (sidecar())
    atributos.append (remolque())
    atributos.append (peso_remolque())
    atributos.append (mercancias_peligrosas())
    atributos.append (transporte_personas())
    atributos.append (transporte_sanitario())
    atributos.append (taxi())

    return atributos

#  Esta clase representa a un objeto que se encuentra dentro del dominio del sistema. En ella se indican
# los atributos que pueden presentarse en los objetos del dominio.
class Observable ():

	"""
		La clase Observable representa a un objeto que se encuentra dentro del dominio del sistema. En ella se indican
	los atributos que pueden presentarse en los objetos del dominio.
	"""

	def __init__(self, nombre = None, n_ruedas = None, vel_max = None, n_ejes = None, pma = None, edad = None, n_asientos = None, cilindrada = None, potencia = None, sidecar = None, remolque = None, peso_remolque = None, mercancias_peligrosas = None, transporte_personas = None, transporte_sanitario = None, taxi = None, valor = None):

		# Nombre del permiso
		self.nombre = nombre
		# Numero de ruedas del vehiculo
		self.n_ruedas = n_ruedas
		# Velocidad maxima permitida
		self.vel_max = vel_max
		# Numero de ejes del vehiculo
		self.n_ejes = n_ejes
		# Peso maximo autorizado (Kg)
		self.pma = pma
		# Edad minima permitida
		self.edad = edad
		# Numero de asientos (incluido el del conductor)
		self.n_asientos = n_asientos
		# Limite de cilindrada (cc)
		self.cilindrada = cilindrada
		# Limite de potencia (cv)
		self.potencia = potencia
		# Posibilidad de llevar sidecar
		self.sidecar = sidecar
		# Posibilidad de llevar remolque
		self.remolque = remolque
		# Peso maximo autorizado remolque
		self.peso_remolque = peso_remolque
		# Posibilidad de transportar mercancias peligrosas
		self.mercancias_peligrosas = mercancias_peligrosas
		# Posibilidad de transportar personas (ejemplo autobus)
		self.transporte_personas = transporte_personas
		# Transporte sanitario
		self.transporte_sanitario = transporte_sanitario
		self.valor = valor

#  Despues se crea una clase por cada tipo de elemento conocido del dominio de la aplicacion, en 
# este caso, permisos de conduccion. Todos ellos heredan de la clase Observable () y dan valor a
# los atributos que son necesarios en cada caso.
class PermisoAM (Observable):

	"""
	Clase que representa al permiso AM de ciclomotor menor de 50cc
	"""

	def __init__(self):

		nombre = 'AM'
		n_ruedas = Ruedas ('2')
		edad = Edad ('15')
		cilindrada = Cilindrada ('50')

		self.debePresentar = [n_ruedas, edad, cilindrada]
		Observable.__init__(self,nombre,n_ruedas,edad,cilindrada)

class PermisoA (Observable):

	"""
	Clase que representa al permiso A de cualquier ciclomotor
	"""

	def __init__(self):

		nombre = "A"
		n_ruedas = Ruedas ('2')		
		edad = Edad ('20')

		self.debePresentar = [n_ruedas, edad]
		Observable.__init__(self,nombre,n_ruedas,edad)

class PermisoA1 (Observable):

	"""
	Clase que representa al permiso A1 de ciclomotor menor de 125cc
	"""

	def __init__(self):

		nombre = "A1"
		n_ruedas = Ruedas ('2')
		edad = Edad ('16')
		cilindrada = Cilindrada ('125')
		potencia = Potencia ('15')
		sidecar = Sidecar ('sidecar')

		self.debePresentar = [n_ruedas, edad, cilindrada, potencia, sidecar]
  		Observable.__init__(self,nombre,n_ruedas,edad, cilindrada, potencia, sidecar)

class PermisoA2 (Observable):

	"""
	Clase que representa al permiso A2 de ciclomotor con potencia menor a 47 cv
	"""

	def __init__(self):

		nombre = "A2"
		edad = Edad ('18')
		n_ruedas = Ruedas ('2')
		potencia = Potencia ('47')

		self.debePresentar = [edad, n_ruedas, potencia]
		Observable.__init__(self,nombre,n_ruedas,edad, potencia)
		
class PermisoB (Observable):

	"""
	Clase que representa al permiso B de vehículo con pma inferior a 3500 Kg y menos de 9 asientos
	"""

	def __init__(self):

		nombre = "B"
		edad = Edad ('18')
		# Numero de asientos menor a 9
		n_asientos = Asientos ('9')
		# PMA menor de 3500 Kg
		pma = Pma ('3500')
		remolque = Remolque ('remolque')
		# PMA remolque menor de 750 Kg
		peso_remolque = PesoRemolque ('750')

		self.debePresentar = [edad, n_asientos, pma, remolque, peso_remolque]
		Observable.__init__(self,nombre,edad, n_asientos, pma, remolque, peso_remolque)

class PermisoC (Observable):

	"""
	Clase que representa al permiso C de vehículo con pma mayor a 3500 Kg y menos de 9 asientos
	""" 

	def __init__(self):

		nombre = "C"
		edad = Edad ('21')
		# PMA mayor de 3500 Kg
		pma = Pma ('3500')
		n_asientos = Asientos ('9')
		remolque = Remolque ('remolque')
		# PMA remolque menor de 750 Kg
		peso_remolque = PesoRemolque ('750')

		self.debePresentar = [edad, pma, n_asientos, remolque, peso_remolque]
		Observable.__init__(self,nombre,edad, n_asientos, pma, remolque, peso_remolque)

class PermisoC1 (Observable):

	"""
	Clase que representa al permiso C1 de vehículo con pma inferior a 7500 Kg
	"""

	def __init__(self):

		nombre = "C1"
		edad = Edad ('18')
		# PMA menor de 7500 Kg
		pma = Pma ('7500')
		remolque = Remolque ('remolque')
		# PMA remolque menor de 750 Kg
		peso_remolque = PesoRemolque ('750')

		self.debePresentar = [edad, pma, remolque, peso_remolque]
  		Observable.__init__(self,nombre,edad, pma, remolque, peso_remolque)

class PermisoD (Observable):

	"""
	Clase que representa al permiso D de vehículo con número de asientos superior a 9
	"""

	def __init__(self):

		nombre = "D"
		edad = Edad ('24')
		transporte_personas = TransportePersonas ('True')
		# Numero de asientos superior a 9
		n_asientos = Asientos ('9')
		remolque = Remolque ('remolque')
		# PMA remolque menor de 750 Kg
		peso_remolque = PesoRemolque ('750')

		self.debePresentar = [edad, transporte_personas, n_asientos, remolque, peso_remolque]
		Observable.__init__(self,nombre,edad, n_asientos, transporte_personas, remolque, peso_remolque)

class PermisoD1 (Observable):

	"""
	Clase que representa al permiso D1 de vehículo con número de asientos inferior a 17
	"""

	def __init__(self):

		nombre = "D1"
		edad = Edad ('21')
		transporte_personas = TransportePersonas ('True')
		# Numero asientos mayor de 9 e inferior a 17
		n_asientos = Asientos ('17')
		remolque = Remolque ('remolque')
		# PMA remolque menor de 750 Kg
		peso_remolque = PesoRemolque ('750')

		self.debePresentar = [edad, transporte_personas, n_asientos, remolque, peso_remolque]
  		Observable.__init__(self,nombre,edad, n_asientos, transporte_personas, remolque, peso_remolque)

class PermisoE (Observable):

	"""
	Clase que representa al permiso E de vehículo con remolque de pma mayor de 750 Kg
	"""

	def __init__(self):

		nombre = "E"
		edad = Edad ('18')
		remolque = Remolque ('remolque')
		# PMA remolque mayor de 750 Kg
		peso_remolque = PesoRemolque ('750')

		self.debePresentar = [edad, remolque, peso_remolque]
		Observable.__init__(self,nombre,edad, remolque, peso_remolque)

class PermisoBTP (Observable):

	"""
	Clase que representa al permiso BTP de vehículo con capacidad de transporte de personas, transporte sanitario o taxi
	"""

	def __init__(self):

		nombre = "BTP"
		edad = Edad ('18')
		transporte_personas = TransportePersonas ('transporte_p')
		transporte_sanitario = TransporteSanitario ('transporte_s')
		taxi = Taxi ('taxi')
		# PMA menor de 3500 Kg
		pma = Pma ('3500')

		self.debePresentar = [edad, transporte_personas, transporte_sanitario, taxi, pma]
		Observable.__init__(self,nombre,edad, transporte_personas, transporte_sanitario, pma, taxi)

class PermisoADR (Observable):

	"""
	Clase que representa al permiso ADR de vehículo con capacidad para transporte de mercancías peligrosas
	"""

	def __init__(self):

		nombre = "ADR"
		edad = Edad ('19')
		mercancias_peligrosas = MercanciasPeligrosas ('mercancias')

		self.debePresentar = [edad, mercancias_peligrosas]
		Observable.__init__(self,nombre, edad, mercancias_peligrosas)

#  Crea una instancia de la caracteristica que reciba. Se utiliza para crear objetos de la clase
# Caracteristica () con los datos introducidos en la interfaz que hacen referencia al elemento 
# desconocido a clasificar.
def creaCaracteristica (tupla):

	"""
		Crea una instancia de la caracteristica que reciba. Se utiliza para crear objetos de la clase
	Caracteristica () con los datos introducidos en la interfaz que hacen referencia al elemento 
	desconocido a clasificar.
	"""
  
	if tupla [0] =='n_ruedas':
		observable = Ruedas (tupla [1])
		return observable

	elif tupla [0] =='vel_max':
		observable = Velmax (tupla [1])
		return observable

	elif tupla [0] =='n_ejes':
		observable = Ejes (tupla [1])
		return observable

	elif tupla [0] =='pma':
		observable = Pma (tupla [1])
		return observable

	elif tupla [0] =='edad':
		observable = Edad (tupla [1])
		return observable

	elif tupla [0] =='n_asientos':
		observable = Asientos (tupla [1])
		return observable

	elif tupla [0] =='cilindrada':
		observable = Cilindrada (tupla [1])
		return observable

	elif tupla [0] =='potencia':
		observable = Potencia (tupla [1])
		return observable

	elif tupla [0] =='sidecar':
		observable = Sidecar (tupla [1])
		return observable

	elif tupla [0] =='remolque':
		observable = Remolque (tupla [1])
		return observable

	elif tupla [0] =='peso_remolque':
		observable = PesoRemolque (tupla [1])
		return observable
  
	elif tupla [0] =='mercancias_peligrosas':
		observable = MercanciasPeligrosas (tupla [1])
		return observable
  
	elif tupla [0] =='transporte_personas':
		observable = TransportePersonas (tupla [1])
		return observable
  
	elif tupla [0] =='transporte_sanitario':
		observable = TransporteSanitario (tupla [1])
		return observable
  
	elif tupla [0] =='taxi':
		observable = Taxi (tupla [1])
		return observable

	return None

#  Devuelve una lista con instancias de todos los elementos conocidos de la base 
# de conocimiento. Se utiliza por el Modelo para realizar el metodo de la poda.
def hipotesis ():

	"""
		Devuelve una lista con instancias de todos los elementos conocidos de la base 
	de conocimiento. Se utiliza por el Modelo para realizar el metodo de la poda.
	"""

	permisoAM = PermisoAM ()
	permisoA = PermisoA ()
	permisoA1 = PermisoA1 ()
	permisoA2 = PermisoA2 ()
	permisoB = PermisoB ()
	permisoC = PermisoC ()
	permisoC1 = PermisoC1 ()
	permisoD = PermisoD ()
	permisoD1 = PermisoD1 ()
	permisoE = PermisoE ()
	permisoBTP = PermisoBTP ()
	permisoADR = PermisoADR ()

	lHp = [permisoAM, permisoA, permisoA1, permisoA2, permisoB, permisoC, permisoC1, permisoD, permisoD1, permisoE, permisoBTP, permisoADR]

	return lHp
