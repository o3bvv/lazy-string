import sys

if sys.version_info >= (3, 9):
  from collections.abc import Callable
  from collections.abc import Mapping

  List  = list
  Tuple = tuple

else:
  from typing import Callable
  from typing import Mapping
  from typing import List
  from typing import Tuple

from collections import UserString

from typing import Any
from typing import TypeVar
from typing import Union


LazyString = TypeVar("LazyString")


class LazyString(UserString):
  """
  A string with delayed evaluation.

  :param func:   Callable (e.g., function) returning a string.
  :param args:   Optional positional arguments which will be passed to the ``func``.
  :param kwargs: Optional keyword arguments which will be passed to the ``func``.

  """

  __slots__ = ("_func", "_args", )

  def __new__(cls, func: Union[Callable, str], *args: Tuple, **kwargs: Mapping) -> object:
    if isinstance(func, str):
      # Many UserString's functions like `lower`, `__add__` and so on wrap
      # returned values with a call to `self.__class__(...)` to ensure the
      # result is of the same type as the original class.
      # However, as the result of all of such methods is always a string,
      # there's no need to create a new instance of a `LazyString`
      return func

    return object.__new__(cls)

  def __init__(self, func: Callable[..., str], *args: Tuple, **kwargs: Mapping) -> None:
    self._func   = func
    self._args   = args
    self._kwargs = kwargs

  @property
  def data(self) -> str:
    return self._func(*self._args, **self._kwargs)

  def __getnewargs_ex__(self) -> Tuple[Tuple, Mapping]:
    args = (self._func, ) + self._args
    return (args, self._kwargs)

  def __getstate__(self) -> Tuple[Callable, Tuple, Mapping]:
    return (self._func, self._args, self._kwargs)

  def __setstate__(self, state: Tuple[Callable, Tuple, Mapping]) -> None:
    self._func, self._args, self._kwargs = state

  def __getattr__(self, name: str) -> Any:
    return getattr(self.data, name)

  def __dir__(self) -> List[str]:
    return dir(str)

  def __copy__(self) -> LazyString:
    return self

  def __repr__(self) -> str:
    try:
      r = repr(str(self.data))
      return f"{self.__class__.__name__}({r})"
    except Exception:
      return "<%s broken>" % self.__class__.__name__
