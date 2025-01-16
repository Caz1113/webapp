from collections.abc import Iterable
from typing import Any, overload
from typing_extensions import TypeIs

class LazyFixture:
    name: str
    def __init__(self, name: str) -> None: ...
    def __eq__(self, other: object) -> bool: ...

@overload
def lazy_fixture(names: str) -> LazyFixture: ...
@overload
def lazy_fixture(names: Iterable[str]) -> list[LazyFixture] | Any: ...
def is_lazy_fixture(val: object) -> TypeIs[LazyFixture]: ...
