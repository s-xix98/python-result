from dataclasses import dataclass
from functools import wraps
from typing import Callable, Generic, TypeVar, Union

from typing_extensions import ParamSpec

T = TypeVar("T")


@dataclass
class Ok(Generic[T]):
    _val: T

    def ok(self) -> T:
        return self._val

    def unsafe_ok(self) -> T:
        return self._val


@dataclass
class Error(Generic[T]):
    err_msg: str

    def unsafe_ok(self) -> T:
        raise ValueError(self.err_msg)


Result = Union[Ok[T], Error[T]]

# Deco
# ------------------------------------------------------------------------------------------
P = ParamSpec("P")
U = TypeVar("U")


def exception_to_result(func: Callable[P, Result[U]]) -> Callable[P, Result[U]]:
    @wraps(func)
    def result_wrapper(*args: P.args, **kwargs: P.kwargs) -> Result[U]:
        try:
            res = func(*args, **kwargs)
            return res
        except Exception as e:
            return Error(f"{e}")

    return result_wrapper
