#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
Created on Sat Jan 18 11:29:53 2014

@author: acalvo
"""

import sys
from PySide import QtGui
import VistaClasificacion
import ckCtrlClasificacion

atributos =  ckCtrlClasificacion.mC.bcC.listaAtributos()
app = QtGui.QApplication(sys.argv) #Se crea una instancia de aplicación
form = VistaClasificacion.VentanasAtributos("Climas", atributos) #Se crea una instancia de de una ventana
sys.exit(app.exec_())


 

 
