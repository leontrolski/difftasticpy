from . import difftasticpy as _difftasticpy  # type: ignore

def diff(a: str, b: str, *, width: int) -> str:
    _difftasticpy.foo(a, b, width)
