#!/usr/bin/env python3

import __me__.util  as UU
from .f_fns4path import fns4path


def exercise4fn(fn):
    PASS=UU.green('PASS')
    FAIL=UU.red('FAIL')
    mod  = fn.__module__.split('.')[-1]
    desc = f'[{mod}.{fn.__name__}]' 
    doc  = str(fn.__doc__).split('\n')[0] or 'no doc'
    try:
        fn()
        print( f'{PASS} {desc} {doc}' )
    except Exception as foo:
        exc=foo
        print( f'{FAIL} {desc} {doc} [{UU.bold(exc)}]' )


def check4mods(*mods):
    from pathlib import Path
    TAGS="sane sanity check".split()
    def sane(obj): return any( tag in str(obj.__doc__) for tag in TAGS ) 
    for mod in mods:
        print( UU.bold(f'CHECKING MODULE: {mod.__name__}'))
        path = Path(mod.__file__).parent
        for fn in filter( sane, fns4path(path)):
            exercise4fn(fn)

