#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
Created on Sat Mar 22 2014

@author: Jael Moragas Ferrera
"""

import sys
from PySide import QtCore
from PySide import QtGui
import ckCtrlClasificacion


class VentanasAtributos(QtGui.QWidget):
    '''
    Cuadro de dialógo para la tarea de clasificacion
    '''
    def __init__(self, name, atributos=None, parent=None):
        '''
        Inicio del cuadro de diálogo
        
        @param name: Nombre del cuadro
        @type name: string
        
        @param atributos: Lista de atributos
        @type atributo: tupla de dos valores 
        
        @param parent: Objeto del que hereda
        @type parent: Objeto padre
        
        '''
        super(VentanasAtributos, self).__init__(parent)

        self.name = name
        labelListA=QtGui.QLabel("Selecione los Atributos",self)
        labelListB=QtGui.QLabel("",self)#quitar
        print atributos
        atributos_list = [(f.nombre)  for f in atributos]
        header = ['NOMBRE', 'VALOR']
        self.tableWidgetAtributos = QtGui.QTableWidget(len(atributos_list),3) 
        self.tableWidgetAtributos.setColumnWidth(0, 400)
        self.tableWidgetAtributos.setColumnWidth(1, 400)
        self.tableWidgetAtributos.setColumnWidth(2, 0)
        self.tableWidgetAtributos.setHorizontalHeaderLabels(header) 

        #Bucle para la crear la lista de atributos y sus valores
        for i in range(len(atributos)):
            item1 = QtGui.QTableWidgetItem(atributos[i].nombre)
            item1.setCheckState(QtCore.Qt.Unchecked) # Establece propiedades a las celdas de la primera columna                
            item1.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled) 
            item3 = QtGui.QTableWidgetItem(atributos[i].atrib)
            atributo = QtGui.QLineEdit()
            atributo.setText(atributos[i].atrib)
            atributo.setEnabled(False)
            self.tableWidgetAtributos.setCellWidget(i, 2, atributo)
            if atributos[i].booleano==None:#Si el tipo de observable es múltiple creamos un combox               
                text = QtGui.QLineEdit()
                text.setText(atributos[i].defecto)
                self.tableWidgetAtributos.setCellWidget(i, 1, text)
            elif atributos[i].booleano=='True':
                text = QtGui.QLineEdit()
                text.setEnabled(False)
                text.setText(atributos[i].defecto)
                self.tableWidgetAtributos.setCellWidget(i, 1, text)
            elif atributos[i].valores.__len__() > 0:
                combobox = QtGui.QComboBox()
                for j in atributos[i].valores:#añadimmos al combox los valeores permitidos
                    combobox.addItem(j) 
                self.tableWidgetAtributos.setCellWidget(i, 1, combobox)
                

            self.tableWidgetAtributos.setItem(i, 0, item1)
            self.tableWidgetAtributos.setItem(i, 2, item3)
                
        labelPosClasificL=QtGui.QLabel("Posibles Candidatos",self)
        labelPosClasificR=QtGui.QLabel("",self)
        self.listWidgetPosClasific = QtGui.QListWidget()
        
        labelClasificL=QtGui.QLabel("Clasificacion",self)
        labelClasificR=QtGui.QLabel("",self)
        self.listWidgetClasificacion = QtGui.QListWidget()
         
        #Botones
        self.busquedaClasificButton=QtGui.QPushButton('Candidatos')
        self.clasificButton=QtGui.QPushButton('Clasificar')
        self.exitButton=QtGui.QPushButton('Exit') 
        self.buttonsLayout = QtGui.QHBoxLayout() 
        self.buttonsLayout.addStretch()
        self.buttonsLayout.addWidget(self.busquedaClasificButton)
        self.buttonsLayout.addWidget(self.clasificButton)
        self.buttonsLayout.addWidget(self.exitButton)
        self.buttonsLayout.addStretch()
        
        #Anadido de celdas
        grid = QtGui.QGridLayout()
        grid.setSpacing(5)
        grid.addWidget(labelListA, 0, 0)
        grid.addWidget(self.tableWidgetAtributos, 1, 0,1,2)
        grid.addWidget(labelListB, 0, 1)
        
        grid.addWidget(labelPosClasificL, 2, 0)
        grid.addWidget(labelPosClasificR, 2, 1)
        grid.addWidget(self.listWidgetPosClasific, 3, 0,1,2)
        
        grid.addWidget(labelClasificL, 4, 0)
        grid.addWidget(labelClasificR, 4, 1)
        grid.addWidget(self.listWidgetClasificacion, 5, 0,1,2)
        
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addLayout(grid)
        mainLayout.addLayout(self.buttonsLayout)
        self.setLayout(mainLayout)
        
        #Forma de la ventana y mostrado
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle(u"TAREA DE CLASIFICACION".format(self.name))
        self.show()
 
        #Centrado de la ventana
        self.center()

        #CReacion de eventos
        self.busquedaClasificButton.clicked.connect(self.candidatos)
        self.clasificButton.clicked.connect(self.clasifica)
        self.exitButton.clicked.connect(self.close)
    
    def clasifica(self):
        '''
        Funcion de inicio del envento de clasificacion
        
        @param self: Objeto de la Vista VentanasAtributos
        @type self: VentanasAtributos
        
        '''
        ckCtrlClasificacion.eventClasifica(self)
        
    def candidatos(self):
        '''
        Funcion de inicio del envento de candidatos
        
        @param self: Objeto de la Vista VentanasAtributos
        @type self: VentanasAtributos
        
        '''
        ckCtrlClasificacion.eventCandidatos(self)
    
    def center(self): 
        '''
        Funcion para centrar la ventana
        
        @param self: Objeto de la Vista VentanasAtributos
        @type self: VentanasAtributos
        
        '''
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topRight())

    
if __name__ == "__main__":
    if True:
        #Podemos probar el módulo de vistas de forma autónoma
        
        atributos = ckCtrlClasificacion.mC.bcC.listaAtributos()
        app = QtGui.QApplication(sys.argv)
        form = VentanasAtributos("Clasificacion", atributos)
        sys.exit(app.exec_())

         
 