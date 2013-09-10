#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys, os
if "FREECAD_PATH" not in os.environ:
    raise EnvironmentError("Please set FREECAD_PATH environment variable.")
sys.path.append(os.path.join(os.environ["FREECAD_PATH"], 'lib'))
sys.path.append(os.path.realpath(".."))
from lettuce import step, world, after

@step("FreeCAD (gui|cmd) is (initialized|open)")
def launch_freeCAD_step(step, mode="gui", state="initialized"):
    world.keep_open = state.lower() == "open"
    return launch_freeCAD(mode)

@step("([a-z_A-Z]+) workbench is loaded")
def load_workbench_step(step, workbench):
    return load_workbench(workbench)

@after.each_scenario
def keep_freeCAD_open(scenario):
    if getattr(world, 'keep_open', False):
        world.gui.exec_loop()
        del world.keep_open

def launch_freeCAD(mode="gui"):
    world.app = __import__('FreeCAD', globals(), locals())
    if mode.lower() == "gui":
        world.gui = __import__('FreeCADGui', globals(), locals())
        world.gui.showMainWindow()


    world.document = world.app.newDocument()

def load_workbench(workbench):
    workbench = "%sWorkbench" %workbench
    if workbench not in world.gui.listWorkbenches().keys():
        raise AttributeError("Workbench '%s' not exists." % workbench)
    world.gui.activateWorkbench(workbench)
    world.gui.updateGui()

if __name__ == "__main__":
    launch_freeCAD("gui")
    load_workbench("OpenFoam")
    world.document.addObject("Part::Box","Box")
    world.gui.exec_loop()
