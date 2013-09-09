# -*- coding: utf-8 -*-
import FreeCAD


class ViewProviderPostprocessing(object):
    def __init__(self, obj):
        self._object = obj
        obj.Proxy = self

    def claimChildren(self):
        children = []
        try:
            children = self._object.Object.Group
        except AttributeError:
            FreeCAD.Console.PrintMessage("ViewProviderPostprocessing Oject has no Group")
        return children


    def updateData(self, fp, prop):
        FreeCAD.Console.PrintMessage("Propriété %s changé\n" % prop)

    def getDisplayModes(self, obj):
        return []

    def getDefaultDisplayMode(self):
        return 'Part'

    def setDisplayMode(self, mode):
        return mode

    def onChanged(self, vp, prop):
        FreeCAD.Console.PrintMessage("Change property: %s\n" % prop)

    def getIcon(self):
        "Return the icon in XPM format which will appear in the tree view. This method is\
                optional and if not defined a default icon is shown."
        return """
            /* XPM */
            static const char * ViewProviderBox_xpm[] = {
            "16 16 6 1",
            "   c None",
            ".  c #141010",
            "+  c #615BD2",
            "@  c #C39D55",
            "#  c #000000",
            "$  c #57C355",
            "        ........",
            "   ......++..+..",
            "   .@@@@.++..++.",
            "   .@@@@.++..++.",
            "   .@@  .++++++.",
            "  ..@@  .++..++.",
            "###@@@@ .++..++.",
            "##$.@@$#.++++++.",
            "#$#$.$$$........",
            "#$$#######      ",
            "#$$#$$$$$#      ",
            "#$$#$$$$$#      ",
            "#$$#$$$$$#      ",
            " #$#$$$$$#      ",
            "  ##$$$$$#      ",
            "   #######      "};
            """

    def __getstate__(self):
        return None

    def __setstate__(self,state):
        return None