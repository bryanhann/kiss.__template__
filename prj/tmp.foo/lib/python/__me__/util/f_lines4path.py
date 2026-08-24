#!/usr/bin/env python3
def lines4path(path):
    if not path.exists(): return []
    return path.read_text().split('\n')
