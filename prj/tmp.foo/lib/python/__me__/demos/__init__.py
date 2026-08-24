#!/usr/bin/env python3

from .demo_callback import demo_callback
from .demo_my       import demo_my
from .demo_check    import demo_check
from .demo_die      import demo_die

UI={}
UI[ 'die' ]       = demo_die
UI[ 'check' ]     = demo_check
UI[ 'callback' ]  = demo_callback
UI[ 'my' ]        = demo_my


