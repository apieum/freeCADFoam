# -*- coding: utf-8 -*-

class OpenFoamWorkbench(Workbench):
    "OpenFoam workbench object"
    ToolTip = "OpenFoam workbench"
    MenuText = "OpenFoam"
    Icon = "OpenFoam"
    Commands =  ['OpenFoam_CreateCase']
    def Initialize(self):
        import OpenFoamGui
        self.appendToolbar(self.MenuText, self.Commands)
        self.appendMenu(self.MenuText, self.Commands)

        try:
            import PyFoam
        except Exception, e:
            FreeCAD.Console.PrintError('Please install PyFoam.\nFor installation details see: http://openfoamwiki.net/index.php/Contrib_PyFoam#Installation')


Gui.addWorkbench(OpenFoamWorkbench())