# -*- coding: utf-8 -*-
from app.case import Case
from app.preprocessing import Preprocessing
from app.solve import Solve
from app.postprocessing import Postprocessing
from gui.case import ViewProviderCase
from tests.stepsDefinition import StepsDefinition
from lettuce import world

@StepsDefinition()
class StructureSteps(object):
    def i_create_a_case(self, step):
        world.Case = Case(world.document)
    def document_contains_a_case_object(self, step):
        case = world.document.getObject("Case")
        self.assertEqual(str(type(case)), "<type 'App.FeaturePython'>")
    def case_object_contains_a_view_provider_case(self, step):
        case = world.document.getObject("Case")
        self.assertIsInstance(case.ViewObject.Proxy, ViewProviderCase)
    def case_object_contains_preprocessing_solve_and_postprocessing_groups(self, step):
        u'''case object contains preprocessing, solve and postprocessing groups'''
        self.assertIsInstance(getattr(world.Case, 'preprocessing'), Preprocessing)
        self.assertIsInstance(getattr(world.Case, 'solve'), Solve)
        self.assertIsInstance(getattr(world.Case, 'postprocessing'), Postprocessing)
