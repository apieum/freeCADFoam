# -*- coding: utf-8 -*-
from app.case import Case
from gui.case import ViewProviderCase
from tests.stepsDefinition import StepsDefinition
from lettuce import world

@StepsDefinition()
class StructureSteps(object):
    def i_create_a_case(self, step):
        world.Case = Case(world.document)
    def document_contains_a_case_object(self, step):
        case = world.document.getObject("Case")
        self.assertIs(case, world.Case.Object)
    def case_object_contains_a_view_provider_case(self, step):
        case = world.document.getObject("Case")
        self.assertIsInstance(case.ViewObject.Proxy, ViewProviderCase)
