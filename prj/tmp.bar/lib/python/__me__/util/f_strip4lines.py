#!/usr/bin/env python3
def strip4lines(lines): 
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop(-1)
    return lines

