# -*- coding: utf-8 -*-
from lettuce.core import STEP_REGISTRY



def StepsDefinition(*args, **kwargs):
    return __DefineSteps(args, kwargs).builder

class __DefineSteps(object):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs

    def builder(self, steps_class):
        self.steps = steps_class.__call__(*self.args, **self.kwargs)
        exclude = getattr(self.steps, "exclude", [])
        for attr in dir(self.steps):
            if self.is_step(attr, exclude):
                step_method = getattr(self.steps, attr)
                sentence = self.stepSentence(step_method)
                self.registerStep(sentence, step_method)

        del self.args, self.kwargs
        return steps_class

    def is_step(self, step, exclude=[]):
        return step not in exclude and step[0] != '_' and callable(getattr(self.steps, step))

    def registerStep(self, sentence, method):
        STEP_REGISTRY[sentence] = method

    def stepSentence(self, method):
        method_name = method.__func__.__name__
        if method.__doc__ is not None:
            print method.__doc__
            sentence = method.__doc__
        else:
            sentence = method_name.replace('_', ' ')
            sentence[0].upper()  # useless ^^
        return sentence
