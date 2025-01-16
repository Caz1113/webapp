from collections import UserList
from collections.abc import Mapping, Sequence
from datetime import datetime
from typing import Any

from django.core.exceptions import ValidationError
from django.forms.renderers import BaseRenderer
from django.utils.safestring import SafeText

def pretty_name(name: str) -> str: ...
def flatatt(attrs: dict[str, Any]) -> SafeText: ...

class RenderableMixin:
    def get_context(self) -> Mapping[str, Any]: ...
    def render(
        self,
        template_name: str | None = ...,
        context: Mapping[str, Any] | None = ...,
        renderer: BaseRenderer | None = ...,
    ) -> SafeText: ...

class RenderableFormMixin(RenderableMixin):
    def as_p(self) -> SafeText: ...
    def as_table(self) -> SafeText: ...
    def as_ul(self) -> SafeText: ...
    def as_div(self) -> SafeText: ...

class RenderableErrorMixin(RenderableMixin):
    def as_json(self, escape_html: bool = ...) -> str: ...
    def as_text(self) -> SafeText: ...
    def as_ul(self) -> SafeText: ...

class ErrorDict(dict[str, ErrorList], RenderableErrorMixin):
    template_name: str
    template_name_text: str
    template_name_ul: str
    renderer: BaseRenderer
    def __init__(
        self, *args: Any, renderer: BaseRenderer | None = ..., **kwargs: Any
    ): ...
    def as_data(self) -> dict[str, list[ValidationError]]: ...
    def get_json_data(self, escape_html: bool = ...) -> dict[str, Any]: ...

class ErrorList(UserList[ValidationError | str], RenderableErrorMixin):
    template_name: str
    template_name_text: str
    template_name_ul: str
    data: list[ValidationError | str]
    error_class: str
    renderer: BaseRenderer
    def __init__(
        self,
        initlist: Sequence[str | Exception] | None = ...,
        error_class: str | None = ...,
        renderer: BaseRenderer | None = None,
    ) -> None: ...
    def as_data(self) -> list[ValidationError]: ...
    def get_json_data(self, escape_html: bool = ...) -> list[dict[str, str]]: ...

def from_current_timezone(value: datetime) -> datetime: ...
def to_current_timezone(value: datetime) -> datetime: ...
