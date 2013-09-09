# -*- coding: utf-8 -*-
from app.case import Case
from lettuce import step, world

@step(u'When I create a Case')
def when_i_create_a_case(step):
    world.Case = Case(world.document)
@step(u'Then document contains a case object')
def then_document_contains_a_case_object(step):
    assert False, 'This step must be implemented'
@step(u'And case object contains a case view provider')
def and_case_object_contains_a_case_view_provider(step):
    assert False, 'This step must be implemented'
