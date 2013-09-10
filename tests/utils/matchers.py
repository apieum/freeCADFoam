# -*- coding: utf-8 -*-
from should_dsl import matcher

def _class_compare(spotted, expected):
    spot_class = getattr(spotted, '__class__')
    return spot_class == expected or getattr(spot_class, '__name__') == expected

@matcher
def be_of_class():
    return (lambda spotted, expected:  _class_compare(spotted, expected) , "%s is %sof class %s")