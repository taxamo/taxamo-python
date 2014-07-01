import pkgutil
import unittest

from taxamo.test import *

def all_names():
    for _, modname, _ in pkgutil.iter_modules(__path__):
        if modname.startswith('test_'):
            yield 'taxamo.test.' + modname


def all():
    return unittest.defaultTestLoader.loadTestsFromNames(all_names())