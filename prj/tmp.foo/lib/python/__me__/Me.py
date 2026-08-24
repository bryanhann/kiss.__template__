from pathlib import Path
from pprint import pprint

from .util import bold
from .Env import ENV

class Me:
    def __init__(self):
        self._env = ENV
    @property
    def my(self):
        return self._env

    def dump(self):
        print( f"{bold('My.my')}" )
        pprint( self.my )
        print( f"{bold('My.my.callback.readtext()')}" ) 
        print( self.my.callback.read_text() )

    def cb_append(self, line):
        with open(self.my.callback, 'a') as fd:
            fd.write(f"{line}\n") 

ME = Me()
