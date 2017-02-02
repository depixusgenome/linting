# Stubs for numpy.distutils.command.config_compiler (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from distutils.core import Command

def show_fortran_compilers(_cache: Any = ...): ...

class config_fc(Command):
    description = ...  # type: str
    user_options = ...  # type: Any
    help_options = ...  # type: Any
    boolean_options = ...  # type: Any
    fcompiler = ...  # type: Any
    f77exec = ...  # type: Any
    f90exec = ...  # type: Any
    f77flags = ...  # type: Any
    f90flags = ...  # type: Any
    opt = ...  # type: Any
    arch = ...  # type: Any
    debug = ...  # type: Any
    noopt = ...  # type: Any
    noarch = ...  # type: Any
    def initialize_options(self): ...
    def finalize_options(self): ...
    def run(self): ...

class config_cc(Command):
    description = ...  # type: str
    user_options = ...  # type: Any
    compiler = ...  # type: Any
    def initialize_options(self): ...
    def finalize_options(self): ...
    def run(self): ...
