import fire

from __me__ import THIS

from demos import *

def demo_die(err):
    exit(err)

if __name__=='__main__':
    fire.Fire(name=THIS.NAME)
