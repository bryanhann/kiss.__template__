#!/usr/bin/env python3

import colorama as _CC
_F=_CC.Fore
_S=_CC.Style
def bold(text):  return f'{_S.BRIGHT}{text}{_S.RESET_ALL}'
def green(text): return bold(f'{_F.GREEN}{text}{_F.RESET}')
def red  (text): return bold(f'{_F.RED}{text}{_F.RESET}')

