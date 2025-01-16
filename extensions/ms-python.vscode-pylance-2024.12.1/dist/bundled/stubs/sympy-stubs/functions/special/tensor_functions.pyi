from typing import Literal
from typing_extensions import Self

from sympy.core.basic import Basic
from sympy.core.function import Function, UndefinedFunction

def Eijk(*args, **kwargs) -> type[UndefinedFunction]: ...
def eval_levicivita(*args): ...

class LeviCivita(Function):
    is_integer = ...
    @classmethod
    def eval(cls, *args) -> None: ...
    def doit(self, **hints): ...

class KroneckerDelta(Function):
    is_integer = ...
    @classmethod
    def eval(cls, i, j, delta_range=...) -> Self | None: ...
    @property
    def delta_range(self) -> Basic | None: ...
    @property
    def is_above_fermi(self) -> bool: ...
    @property
    def is_below_fermi(self) -> bool: ...
    @property
    def is_only_above_fermi(self) -> Literal[False]: ...
    @property
    def is_only_below_fermi(self) -> Literal[False]: ...
    @property
    def indices_contain_equal_information(self) -> bool: ...
    @property
    def preferred_index(self) -> Basic: ...
    @property
    def killable_index(self) -> Basic: ...
    @property
    def indices(self) -> tuple[Basic, ...]: ...
