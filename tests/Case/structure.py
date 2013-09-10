# -*- coding: utf-8 -*-
from tests.Base import world, should, be_instance_of, be_of_class, StepsDefinition, be_into
from App import Case, Preprocessing, Solve, Postprocessing
from gui.case import ViewProviderCase


@StepsDefinition()
class StructureSteps(object):

    def i_create_a_case(self, step):
        world.Case = Case(world.document)

    def document_contains_a_case_object(self, step):
        case = world.document.getObject("Case")
        case |should| be_of_class("FeaturePython")

    def case_object_contains_a_view_provider_case(self, step):
        case = world.document.getObject("Case")
        case.ViewObject.Proxy |should| be_instance_of(ViewProviderCase)

    def case_object_contains_preprocessing_solve_and_postprocessing_groups(self, step):
        u'''case object contains preprocessing, solve and postprocessing groups'''
        getattr(world.Case, 'preprocessing') |should| be_instance_of(Preprocessing)
        getattr(world.Case, 'solve') |should| be_instance_of(Solve)
        getattr(world.Case, 'postprocessing') |should| be_instance_of(Postprocessing)

    def preprocessing_solve_and_postprocessing_are_children_of_case_object(self, step):
        world.Case.preprocessing.Object |should| be_into(world.Case.Object.Group)
        world.Case.solve.Object |should| be_into(world.Case.Object.Group)
        world.Case.postprocessing.Object |should| be_into(world.Case.Object.Group)
