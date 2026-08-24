#!/usr/bin/env python3

from __me__.check import check4mods

def demo_check(): 
    """Demonstrate the internal 'check' testing system.
    """
    import __me__.demos.checkthis as outer
    import __me__.demos.checkthis.inner as inner
    check4mods(outer, inner)

