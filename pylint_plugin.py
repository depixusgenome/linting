#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# pylint: disable=protected-access
"Correcting a pylint bug in python 3.7 and pylint <= 2.2.1"
from   pathlib   import Path
from   importlib import import_module
import sys
import re

def _namedtuple_docstring():
    from  pylint.checkers.base import DocStringChecker as _doc
    def _check_docstring(self, node_type, node, *args,
                         __old__ = _doc._check_docstring, **kwa):
        # don't warn about missing-docstring in NamedTuple
        if node_type == 'class' and len(node.bases) == 1 and node.doc is None:
            if getattr(node.bases[0], 'name', None) == 'NamedTuple':
                return
        __old__(self, node_type, node, *args, **kwa)
    _doc._check_docstring = _check_docstring

def register(*_):
    "monkeypatch the item"
    path = Path(__file__).parent.parent/"_pylint_plugin.py"
    if path.exists():
        try:
            sys.path.insert(0, str(path.parent.resolve()))
            import_module("_pylint_plugin").register(*_)
        finally:
            sys.path.pop(0)
    _namedtuple_docstring()
    import pylint_plugin_numpy
