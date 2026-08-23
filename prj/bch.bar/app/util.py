#!/usr/bin/env python3

import colorama
F=colorama.Fore
S=colorama.Style
def bold(text):  return f'{S.BRIGHT}{text}{S.RESET_ALL}'
def green(text): return bold(f'{F.GREEN}{text}{F.RESET}')
def red  (text): return bold(f'{F.RED}{text}{F.RESET}')

