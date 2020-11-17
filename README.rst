lazy-string
===========

Python library for defining strings with delayed evaluation.

|pypi_package| |python_versions| |license|


The package provides a ``LazyString`` class. Its constructor accepts a callable (say, a function) which will be called when string's value is needed. The constructor also allows to specify positional and keyword arguments for that callable:

.. code-block:: python

  def __init__(self, func: Callable[..., str], *args: Tuple, **kwargs: Mapping) -> None:
    ...


The value is re-evaluated on every access.


Installation
------------

Available as a `PyPI <https://pypi.python.org/pypi/lazy-string>`_ package:

.. code-block:: bash

  pip install lazy-string


Usage
-----

Using with a function having no parameters:

.. code-block:: python

  from lazy_string import LazyString

  def make_foo() -> str:
    return "foo"

  s = LazyString(make_foo)


The value is evaluated on demand:

.. code-block:: python

  >>> s + " bar"
  'foo bar'

  >>> str(s)
  'foo'


Representation explicitly tells it's a ``LazyString``:

.. code-block:: python

  >>> s
  LazyString('foo')


It's safe to pass standard strings, as they will be returned as-is:

.. code-block:: python

  >>> LazyString("foo bar")
  'foo bar'


Supports methods of standard strings:

.. code-block:: python

  >>> s.upper()
  'FOO'

  >>> "f" in s
  True

  >>> dir(s)
  ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
   '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
   '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__',
   '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__',
   '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__',
   '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
   'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',
   'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha',
   'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric',
   'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower',
   'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust',
   'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith',
   'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


Supplying parameters for the callable:

.. code-block:: python

  def make_foo(arg1, arg2):
    return f"foo {arg1} {arg2}"

  s = LazyString(make_foo, 123, arg2=456)


.. code-block:: python

  >>> str(s)
  'foo 123 456'


Implementation Details
----------------------

``LazyString`` is inherited from `collections.UserString <https://docs.python.org/3/library/collections.html#collections.UserString>`_.

.. code-block:: python

  >>> LazyString.__mro__
  (<class 'lazy_string.LazyString'>, <class 'collections.UserString'>,
   <class 'collections.abc.Sequence'>, <class 'collections.abc.Reversible'>,
   <class 'collections.abc.Collection'>, <class 'collections.abc.Sized'>,
   <class 'collections.abc.Iterable'>, <class 'collections.abc.Container'>,
   <class 'object'>)


Serialization
-------------

Pickling
^^^^^^^^

Supported out of the box:

.. code-block:: python

  >>> import pickle
  >>> s == pickle.loads(pickle.dumps(s))
  True


To JSON
^^^^^^^

Supported with any encoder able to encode ``collections.UserString``:

.. code-block:: python

  import json
  import collections

  class JSONEncoder(json.JSONEncoder):

    def default(self, o):
      if isinstance(o, collections.UserString):
        return str(o)
      return super().default(o)


.. code-block:: python

  >>> data = {'s': s}
  >>> json.dumps(data, cls=JSONEncoder)
  '{"s": "foo"}'


.. |pypi_package| image:: https://img.shields.io/pypi/v/lazy-string
   :target: http://badge.fury.io/py/lazy-string/
   :alt: Version of PyPI package

.. |python_versions| image:: https://img.shields.io/badge/Python-3.7+-brightgreen.svg
   :alt: Supported versions of Python

.. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/oblalex/lazy-string/blob/main/LICENSE
   :alt: MIT license
