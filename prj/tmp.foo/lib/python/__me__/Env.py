#!/usr/bin/env python3

import os

from __me__.util import bold, _shorten, pathify

class Env(dict):
    def __init__(self):
        prefix = 'my_'
        for key, val in os.environ.items():
            self[ _shorten(key, prefix ) ] = val
        if None in self: del self[None]
    def __getattr__(self, name):
        return pathify(self[name])
    def dump(self):
        bold( "MyEnv:" )
        for k,v in self.items():
             print( f"{key}: {val}" )


ENV=Env()

