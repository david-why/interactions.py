import datetime

import attrs

from interactions.api.http.client import HTTPClient
from interactions.base import get_logger as get_logger
from io import FileIO, IOBase
from logging import Logger
from typing import Any, Optional, Union

log: Logger

class MISSING: ...

@attrs.define(eq=False, init=False, on_setattr=attrs.setters.NO_OP)
class DictSerializerMixin:
    _json: dict
    _extras: dict
    def __init__(self, kwargs_dict: dict = ..., **other_kwargs) -> None: ...

@attrs.define(eq=False, init=False, on_setattr=attrs.setters.NO_OP)
class ClientSerializerMixin(DictSerializerMixin):
    _client: HTTPClient

    def __init__(self, kwargs_dict: dict = ..., **other_kwargs):
        ...

def convert_list(converter): ...
def convert_int(converter): ...

define_defaults: Any
define: Any

def field(converter: Any | None = ..., default=..., add_client: bool = ..., discord_name: str = ..., **kwargs): ...

class Overwrite(DictSerializerMixin):
    id: int
    type: int
    allow: str
    deny: str

class ClientStatus(DictSerializerMixin):
    dektop: Optional[str]
    mobile: Optional[str]
    web: Optional[str]

class Snowflake:
    def __init__(self, snowflake: Union[int, str, 'Snowflake']) -> None: ...
    def __int__(self): ...
    @property
    def increment(self) -> int: ...
    @property
    def worker_id(self) -> int: ...
    @property
    def process_id(self) -> int: ...
    @property
    def epoch(self) -> float: ...
    @property
    def timestamp(self) -> datetime.datetime: ...
    def __hash__(self): ...
    def __eq__(self, other): ...

class Color:
    @property
    def blurple(self) -> hex: ...
    @property
    def green(self) -> hex: ...
    @property
    def yellow(self) -> hex: ...
    @property
    def fuchsia(self) -> hex: ...
    @property
    def red(self) -> hex: ...
    @property
    def white(self) -> hex: ...
    @property
    def black(self) -> hex: ...

class File:
    def __init__(self, filename: str, fp: Optional[IOBase] = ..., description: Optional[str] = ...) -> None: ...

class Image:
    def __init__(self, file: Union[str, FileIO], fp: Optional[IOBase] = ...) -> None: ...
    @property
    def data(self) -> str: ...
    @property
    def filename(self) -> str: ...
