from typing import TYPE_CHECKING

from . import difftasticpy as _difftasticpy  # type: ignore

if not TYPE_CHECKING:
    foo = _difftasticpy.foo
