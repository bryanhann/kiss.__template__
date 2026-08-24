#!/usr/bin/env python3

from __me__ import ME

def demo_callback():
    """Demonstrate the internal 'callback' feature.
    """
    ME.cb_append( '# this is an appended line' )
    ME.cb_append( '# this is another line' )
    ME.dump()

