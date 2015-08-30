#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
@author: Jael M.
"""


import sys
from PySide import QtCore
from PySide import QtGui
import ckCtrlDiagnostico

class DiagnosticDlg(QtGui.QWidget):
    '''
    Cuadro de dialógo para la tarea de diangóstico
    '''
    def __init__(self, name, observables=None, parent=None):
        '''
        Inicio del cuadro de diálogo
        
        @param name: Nombre del cuadro
        @type name: string
        
        @param observables: Posibles observables
        @type obsevables: tupla de dos valores 
        
        '''
        super(DiagnosticDlg, self).__init__(parent)

        self.name = name #Coloca el nombre al cuadro de diálogo
        #Label
        labelListA=QtGui.QLabel("Selecione los Fallos Presentados",self)
        labelListB=QtGui.QLabel("",self)#quitar
        observables_list = [(f.nombre , f.valor)  for f in observables]
        header = ['NOMBRE', 'VALOR']
        self.tableWidgetPosiblesFallos = QtGui.QTableWidget(len(observables_list),2) #Crea la tabla de elementos
        self.tableWidgetPosiblesFallos.setColumnWidth(0, 400) #Asignan ancho a las columnas
        self.tableWidgetPosiblesFallos.setColumnWidth(1, 400)
        self.tableWidgetPosiblesFallos.setHorizontalHeaderLabels(header) #Asigna etiquetas a las columnas
        
        for i in range(len(observables)):
            item1 = QtGui.QTableWidgetItem(observables[i].nombre) #Crea un item y le asigna el nombre de la observable
            item1.setCheckState(QtCore.Qt.Checked) # Establece propiedades a las celdas de la primera columna
            item1.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            combobox = QtGui.QComboBox()
            combobox.addItem('True') 
            combobox.addItem('False') 
            self.tableWidgetPosiblesFallos.setCellWidget(i, 1, combobox)

            self.tableWidgetPosiblesFallos.setItem(i, 0, item1)#Establecemos el item en la columna 0
                
        labelHipotesisL=QtGui.QLabel("Posibles Hipotesis",self)#Creamos un listwidget para las posibles hipótesis
        labelHipotesisR=QtGui.QLabel("",self)
        self.listWidgetHipotesis = QtGui.QListWidget()#Lista de hipótesis
        
        labelDiagnosticoL=QtGui.QLabel("Diagnóstico",self)
        labelDiagnosticoR=QtGui.QLabel("",self)
        self.listWidgetDiagnosticos = QtGui.QListWidget()#Lista de diagnósticos
        
        labelExplicacionL=QtGui.QLabel("Explicacion",self)
        labelExplicacionR=QtGui.QLabel("     ",self)
        self.PlainTextEditExplicacion = QtGui.QPlainTextEdit()#Cuadro de texto    de la explicación           
        #Botones
        self.coberturaCausalButton=QtGui.QPushButton('Cobertura Causal')#Para invocar el método de cobretura causal
        self.coberturaCausalButton.setToolTip('Realizar cobertura causal')
        self.diagnosticaButton=QtGui.QPushButton('Diagnostica') #Para ejecutar el diagnóstico
        self.diagnosticaButton.setToolTip('Realizar diagnostico')        
        self.exitButton=QtGui.QPushButton('Exit') #Para salir del programa
        self.exitButton.setToolTip('Salir')
        
        self.buttonsLayout = QtGui.QHBoxLayout() #Gestor de diseño horizontal
        #http://stackoverflow.com/questions/20452754/how-exactly-does-addstretch-work-in-qboxlayout
        self.buttonsLayout.addStretch()
        self.buttonsLayout.addWidget(self.coberturaCausalButton)
        self.buttonsLayout.addWidget(self.diagnosticaButton)
        self.buttonsLayout.addWidget(self.exitButton)
        self.buttonsLayout.addStretch()
        
        #Rejilla de distribución de los controles
        #Ver http://srinikom.github.io/pyside-docs/PySide/QtGui/QGridLayout.html
        grid = QtGui.QGridLayout()
        grid.setSpacing(5)
        grid.addWidget(labelListA, 0, 0)
        grid.addWidget(self.tableWidgetPosiblesFallos, 1, 0,1,2)
        grid.addWidget(labelListB, 0, 1)
        
        grid.addWidget(labelHipotesisL, 2, 0)
        grid.addWidget(labelHipotesisR, 2, 1)
        grid.addWidget(self.listWidgetHipotesis, 3, 0,1,2)
        
        grid.addWidget(labelDiagnosticoL, 4, 0)
        grid.addWidget(labelDiagnosticoR, 4, 1)
        grid.addWidget(self.listWidgetDiagnosticos, 5, 0,1,2)
        grid.addWidget(labelExplicacionL, 6, 0)
        grid.addWidget(labelExplicacionR, 6, 1)
        grid.addWidget(self.PlainTextEditExplicacion, 7, 0,1,2)
        
        #Diseño principal
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addLayout(grid)
        mainLayout.addLayout(self.buttonsLayout)
        self.setLayout(mainLayout) #Asignar a la ventana la distribución de los controles
        
    
        self.setGeometry(300, 300, 900, 600)
        self.setWindowTitle(u"TAREA DE DIAGNOSTICO".format(self.name))
        self.show()
 
        self.center()
        
        #Conexiones de los botones y eventos en las listas:
        #==========
        self.coberturaCausalButton.clicked.connect(self.coberturaCausal)
        self.diagnosticaButton.clicked.connect(self.diagnostica)
        self.exitButton.clicked.connect(self.close)

    def diagnostica(self):
        '''
        Funcion de inicio del evento de diagnostico
        
        @param self: Objeto de la Vista DiagnosticDlg
        @type self: DiagnosticDlg
        
        '''
        ckCtrlDiagnostico.eventDiagnostica(self)
        
        
    def coberturaCausal(self):
        '''
        Funcion de inicio del evento de cobertura causal
        
        @param self: Objeto de la Vista DiagnosticDlg
        @type self: DiagnosticDlg
        
        '''
        #Recolecta datos de las vistas y se lo pasamos al controlador
        # Al pasar self pasamos toda la información de la ventana
        ckCtrlDiagnostico.eventCoberturaCausal(self)
    
    def center(self):   
        '''
        Funcion para centrar la ventana
        
        @param self: Objeto de la Vista DiagnosticDlg
        @type self: DiagnosticDlg
        
        '''
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



        
if __name__ == "__main__":
    if True:
        #Podemos probar el módulo de vistas de forma autónoma
        observables =  ckCtrlDiagnostico.modelo.bc2.observables()
        
        app = QtGui.QApplication(sys.argv)
        form = DiagnosticDlg("Fallos", observables)
        sys.exit(app.exec_())
    if False:
        observables =  ckCtrlDiagnostico.modelo.bc2.observables()
        print observables
        l = [(f.nombre , f.valor)  for f in observables]
        print l
        header = ['Nombre', 'Valor']
         
    

 
