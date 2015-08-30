#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
Created on Sat Jan 18 11:29:53 2014

@author: acalvo
"""

import sys
from PySide import QtGui
import ckVtsDiagnosticoD
import ckCtrlDiagnostico

observables =  ckCtrlDiagnostico.modelo.bc2.observables()
app = QtGui.QApplication(sys.argv) #Se crea una instancia de aplicación
form = ckVtsDiagnosticoD.DiagnosticDlg("Fallos", observables) #Se crea una instancia de de una ventana
sys.exit(app.exec_())


 

 
