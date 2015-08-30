#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
Created on Sat Mar 22 2014

@author: Antonio Porraz Pérez
"""

from PySide import QtCore
import mC

def eventCandidatos(cdClasificacion):
    '''
    Evento que genera una lista de candidatos.
    Primero recoge los datos de la vista y los envía al modelo. Después recibe
    una lista de candidatos y los muestra en la lista.
    
    @param cdClasificacion: Vista de la aplicacion
    @type VentanasAtributos: VentanasAtributos
    
    '''
        
    listaObservables=[]
    cdClasificacion.listWidgetPosClasific.clear()    
    for h in mC.bcC.hipotesis():
        listaObservables.append(h.nombre)
    cdClasificacion.listWidgetPosClasific.addItems(listaObservables)
    
            
def eventClasifica(cdClasificacion):
    '''
    Evento que genera una lista de clasificados.
    Primero recoge los datos de la vista y los envía al modelo. Después recibe
    una lista de clasificados y los muestra en la lista.
    
    @param cdClasificacion: Vista de la aplicacion
    @type VentanasAtributos: VentanasAtributos
    
    '''
    pass
    eventCandidatos(cdClasificacion)
    atributos=[]
    for i in range(cdClasificacion.tableWidgetAtributos.rowCount()):
        item1=cdClasificacion.tableWidgetAtributos.item(i,0)
        if item1.checkState()==QtCore.Qt.CheckState.Checked:
            item3=cdClasificacion.tableWidgetAtributos.item(i,2)
            item2=cdClasificacion.tableWidgetAtributos.cellWidget(i, 1)
            if str(item2).startswith('<PySide.QtGui.QComboBox'):
                atributos.append( (item3.text() ,item2.currentText()) )
            else:
                atributos.append( (item3.text(), item2.text()) )

    listaCaracteristicas=[]
    atr=len (atributos)
    for i in range(atr):
        print atributos[i][0]
        print atributos[i][1]
        listaCaracteristicas.append(mC.bcC.creaCaracteristica( (atributos[i][0], atributos[i][1]) ))
        
    listaObservables=[]
    cdClasificacion.listWidgetClasificacion.clear()
    mp=mC.MetodoPoda(listaCaracteristicas)
    res = mp.execute()
    tam=len(res)
    if tam == 0:
        cdClasificacion.listWidgetClasificacion.addItem("<No existen resultados para esos atributos>")
    else:
        for h in res:
            listaObservables.append(h.nombre)
    cdClasificacion.listWidgetClasificacion.addItems(listaObservables)

if __name__=='__main__':  
    pass

            
        
        
