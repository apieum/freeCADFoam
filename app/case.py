# -*- coding: utf-8 -*-
import FreeCAD
from app.preprocessing import Preprocessing
from app.solve import Solve
from app.postprocessing import Postprocessing

class Case(object):
    def __init__(self, document, with_gui=True):
        self.Object = document.addObject("App::DocumentObjectGroupPython","Case")
        self.ObjectProxy = _CaseProxy(self.Object)
        if with_gui:
            from gui.case import ViewProviderCase
            self.ViewProvider = ViewProviderCase(self.Object.ViewObject)
        self.preprocessing = Preprocessing(self.Object, with_gui)
        self.solve = Solve(self.Object, with_gui)
        self.postprocessing = Postprocessing(self.Object, with_gui)

    def run(self):
        raise NotImplemented("Case::run not yet implemented")

class _CaseProxy(object):
    def __init__(self, obj):
        self._object = obj
        obj.Proxy = self
        obj.addProperty("App::PropertyPythonObject", "newObject")
        obj.newObject = self.newObject
        obj.addProperty("App::PropertyPythonObject", "Preprocessing")
        obj.addProperty("App::PropertyPythonObject", "Solve")
        obj.addProperty("App::PropertyPythonObject", "Postprocessing")

    def onChanged(self, fp, prop):
        FreeCAD.Console.PrintMessage("Change property: %s\n" % prop)

    def execute(self, fp):
        FreeCAD.Console.PrintMessage("Recompute Python Case feature\n")

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