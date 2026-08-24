from .f_fmap        import fmap
from .f_lmap        import lmap
from .f_goodfolder  import goodfolder
from .f_isfile      import isfile
from .f_lines4path  import lines4path
from .f_listify     import listify
from .f_mkdirs      import mkdirs
from .f_strip4lines import strip4lines
from .f_text4lines  import text4lines
from .f_walk        import walk
from .colors import *
def _shorten( string : str , prefix : str) -> str|None :
    if string.startswith(prefix):
        return string[len(prefix):]
    else: 
        return None

#!/usr/bin/env python3
from pathlib import Path

def pathify(string : str) -> Path | str:
    if string.startswith( '/' ):
       return Path(string)
    else:
       return string
