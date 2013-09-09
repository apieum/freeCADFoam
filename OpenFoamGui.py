# -*- coding: utf-8 -*-
import FreeCAD, FreeCADGui
from app.case import Case


class CreateCase:
    mod_name = 'OpenFoam'
    def Activated(self):
        FreeCAD.Console.PrintMessage('Creation of a new case\n')
        Case(FreeCAD.ActiveDocument)

    def GetResources(self):
        return {'Pixmap' : 'OpenFoam', 'MenuText': 'Create Case', 'ToolTip': 'Create New OpenFoam Case'}


FreeCADGui.addCommand('OpenFoam_CreateCase', CreateCase())