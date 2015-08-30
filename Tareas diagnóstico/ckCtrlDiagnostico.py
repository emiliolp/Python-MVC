#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
Created on Sun Jan 19 10:28:45 2014

@author: acalvo
"""
from PySide import QtGui
from PySide import QtCore
import modelo

def eventCoberturaCausal(cdDiagnostico,tr=False):
    '''
    Inferenvia de cobretura causal.
    '''
    fallos=[]#Vamos a captar los fallos del cuadro de diálogo
    if tr:
        print 'entra'
    for i in range(cdDiagnostico.tableWidgetPosiblesFallos.rowCount()):
        item1=cdDiagnostico.tableWidgetPosiblesFallos.item(i,0)
        if item1.checkState()==QtCore.Qt.CheckState.Checked:
            item2=cdDiagnostico.tableWidgetPosiblesFallos.cellWidget(i, 1)
            fallos.append( (item1.text(),item2.currentText()) )
    if tr:
        print fallos
    cc=modelo.Cubrir(fallos)#Invocamos a la inferencia de cobertura causal del diagnóstico
    cc.execute()
    lHipotesis=[]
    for h in cc.listaHipotesis:
        lHipotesis.append(h.nombre)#Obtenemos la lista de hipótesis
    cdDiagnostico.listWidgetHipotesis.clear()#Borramos la información del listWidget
    cdDiagnostico.listWidgetHipotesis.addItems(lHipotesis)#añadimos la nueva información al listWidgwet
    
            
def eventDiagnostica(cdDiagnostico,tr=False):
    '''
    Controla el evendo de diagnóstico
    '''
    cdDiagnostico.PlainTextEditExplicacion.clear()
    pass
    eventCoberturaCausal(cdDiagnostico,tr=False)
    fallos=[]

    if tr:
        print 'entra'
    for i in range(cdDiagnostico.tableWidgetPosiblesFallos.rowCount()):
        item1=cdDiagnostico.tableWidgetPosiblesFallos.item(i,0)
        if item1.checkState()==QtCore.Qt.CheckState.Checked:
            item2=cdDiagnostico.tableWidgetPosiblesFallos.cellWidget(i, 1)
            fallos.append( (item1.text(),item2.currentText()) )#Creamos una tupla del fallo y sus posibles
                                                               #valores
    if tr:        
        print 'Presentando los fallos',fallos
        print '======================'
    
    #Comprueba que los fallos captados son compatibles con la base de conocimiento
    observables=modelo.identificaSignosSintomas(fallos)
    if tr:
        print 'Obteniendo Observables:', observables
    if not observables==None:#Continuo porque todo es correcto
        pass
        mcc=modelo.MetodoCoberturaCausal(observables)#Creamos una instancia del método cc
        mcc.execute()
        if tr:
            pass
        print 'Justificación'
        print '============='
        print mcc.explicacion
        print 
        print 'Diagnóstico: ' 
        print '============ '
        for d in mcc.diagnostico:
            print d.nombre
        print 'fin'
        cdDiagnostico.PlainTextEditExplicacion.clear()
        cdDiagnostico.PlainTextEditExplicacion.appendPlainText(mcc.explicacion)
        cdDiagnostico.PlainTextEditExplicacion.moveCursor(QtGui.QTextCursor.Start)
        
        cdDiagnostico.listWidgetDiagnosticos.clear()
        lDiag=[]
        for d in mcc.diagnostico:
            lDiag.append(d.nombre)
        cdDiagnostico.listWidgetDiagnosticos.addItems(lDiag)
        
        #Si no existen resultados
        res = mcc.diagnostico
        tam=len(res)
        if tam == 0:
            cdDiagnostico.listWidgetDiagnosticos.clear()#Borramos la información del listWidget
            cdDiagnostico.listWidgetDiagnosticos.addItem("<No existen resultados para esos atributos>")
    
    
        
        
    
    return
    mcc=modelo.MetodoCoberturaCausal(fallos)
    mcc.execute()
    print mcc.diagnostico
    print mcc.explicacion
    
    
 
def observables():
    return 

if __name__=='__main__':  
    pass

            
        
        
