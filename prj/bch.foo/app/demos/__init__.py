#!/usr/bin/env python3
from __me__.check import check4mods
from __me__ import MY

def demo_callback():
    MY.cb_append( '# this is an appended line' )
    MY.cb_append( '# this is another line' )
    MY.dump()

def demo_check(): 
    import demos.checkthis as outer
    import demos.checkthis.inner as inner
    check4mods(outer, inner)
