from pathlib import Path
from pprint import pprint
from util import bold
from . import THIS
CALLBACK=THIS.CALLBACK
class My:
    def __init__(self):
        self._env = THIS
    @property
    def env(self): return self._env 
    @property
    def name(self): return self._env.NAME 
    def dump(self):
        print( f"{bold('MY ENVIRONMENT')}" )
        pprint( self._env )
        print( f"{bold('MY CALLBACK FILE')}" )
        print( Path(self.env.CALLBACK).read_text() )
    def cb_append(self, line):
        with open(self.env.CALLBACK, 'a') as fd:
            fd.write(f"{line}\n") 
    @property
    def _cbpath(self):
        return Path(self.env.CALLBACK) 
MY = My()
