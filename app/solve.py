# -*- coding: utf-8 -*-
import FreeCAD

class Solve(object):
    def __init__(self, parent, with_gui=True):
        self.Object = parent.newObject("App::DocumentObjectGroupPython", "Solve")
        self.ObjectProxy = _SolveProxy(self.Object)
        if with_gui:
            from gui.solve import ViewProviderSolve
            self.ViewProvider = ViewProviderSolve(self.Object.ViewObject)

class _SolveProxy(object):
    def __init__(self, obj):
        self._object = obj
        obj.Proxy = self
        obj.addProperty("App::PropertyPythonObject", "newObject")
        obj.newObject = self.newObject

    def onChanged(self, fp, prop):
        FreeCAD.Console.PrintMessage("Change property: %s\n" % prop)

    def execute(self, fp):
        FreeCAD.Console.PrintMessage("Recompute Python Solve feature\n")

    def newObject(self, obj_type, name):
        new_obj = self._object.Document.addObject(obj_type, name)
        self.addObject(new_obj)
        return new_obj

    def addObject(self, obj):
        if obj not in self._object.Group:
            group = list(self._object.Group)
            group.append(obj)
            self._object.Group = group

    def getObject(self, obj_name):
        for obj in self._object.Group:
            if obj.Name == obj_name:
                return obj

    def hasObject(self, obj):
        return obj in self._object.Group

    def removeObject(self, obj):
        group = list(self._object.Group)
        group.remove(obj)
        self._object.Group = group


    def removeObjectsFromDocument(self):
        document = self._object.Document
        for obj in self._object.Group:
            document.removeObject(obj.Name)
        name = self._object.Name
        del self._object
        document.removeObject(name)