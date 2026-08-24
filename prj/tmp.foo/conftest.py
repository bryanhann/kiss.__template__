import os
import sys
from pathlib import Path
from tempfile import mktemp

NAME = Path(__file__).parent.name
HERE = Path(__file__).parent
HERE = str(HERE) 

LIB  = f"{HERE}/lib/python"
BASE = f"{HERE}/app"
PYTHONPATH = f"{LIB}:{BASE}"

THIS = "THIS_magic_123"
CALLBACK = f"{mktemp()}/callback"

def pytest_configure(config):
    sys.path.append(LIB)
    sys.path.append(BASE)
    os.environ[ "THIS"             ] = THIS
    os.environ[ f"{THIS}_NAME"     ] = NAME
    os.environ[ f"{THIS}_CALLBACK" ] = CALLBACK
    os.environ[ "my_callback"      ] = CALLBACK
    os.environ[ "my_name"          ] = NAME
    os.environ[ "my_pylib"         ] = LIB
    os.environ[ "my_bucket_dst"    ] = "s3://xxx"
    os.environ[ "PYTHONPATH"       ] = PYTHONPATH


