#!/usr/bin/env python3

from __me__ import ME
from __me__.util import bold

def demo_my(name:str):
    """Return ME.my.NAME
    """
    head = f"ME.my.{name}"
    try:
        val=getattr(ME.my, name)
        print( f"{bold(head)} is '{val}'" )
    except KeyError:
        print( f"{bold(head)} is not defined" )

