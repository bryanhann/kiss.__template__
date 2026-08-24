#!/usr/bin/env python3

from pathlib import Path
from importlib import import_module

def fns4mod(mod):
    for name in dir(mod):
        yield getattr(mod,name)

def fns4path(path):
    for mod in mods4path(path):
        yield from fns4mod(mod)

def mods4path(path):
    assert (path/'__init__.py').exists()
    for script in path.glob('*.py'):
        modname = modname4script(script)
        try:
            yield import_module(modname)
        except ModuleNotFoundError:
            continue

def modname4script(target):
    """Take the path to a target python script.
    Return the dotted module name.
    EG: 'LIB/foo/bar/zot.py' :-> 'foo.bar.zoto
    """
    assert target.name.endswith('.py')
    plist = []
    plist.append( target.name[:-3] )
    target = target.parent
    while (target/'__init__.py').exists():
        plist.append(target.name)
        target = target.parent
    plist.reverse()
    return '.'.join(plist) 
