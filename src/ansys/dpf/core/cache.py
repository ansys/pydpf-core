# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Provides for caching evaluated results for faster re-evaluation."""

from typing import NamedTuple


def class_handling_cache(cls):
    """Class decorator used to handle cache.

    To use it, add a ''_to_cache'' static attribute in the given class.
    This private dictionary should map class getters to their list of setters.
    At initialization, this decorator add a ''_cache'' property to the class.
    This new property is an instance of ''CacheHandler''.

    .. note::
       The method must be used as a class decorator.
    """
    if hasattr(cls, "_to_cache"):

        def get_handler(mesh):
            if hasattr(mesh, "__cache"):
                return mesh.__cache
            else:
                setattr(mesh, "__cache", CacheHandler(cls, cls._to_cache))
            return mesh.__cache

        for getter, setters in cls._to_cache.items():
            if setters:
                for setter in setters:
                    setattr(cls, setter.__name__, _handle_cache(setter))
            setattr(cls, getter.__name__, _handle_cache(getter))

        setattr(cls, "_cache", property(get_handler))
    return cls


class MethodIdentifier(NamedTuple):
    """Provides for identifying a method."""

    method_name: str
    args: list
    kwargs: dict

    def __eq__(self, other):
        """Compare two methods for equality."""
        if isinstance(other, str):
            return self.method_name == other
        else:
            return (
                self.method_name == other.method_name
                and self.args == other.args
                and self.kwargs == other.kwargs
            )

    def __hash__(self):
        """Fetch the hash corresponding to a method."""
        hash = self.method_name.__hash__()
        if self.args:
            hash += self.args.__hash__()
        if self.kwargs:
            hash += self.kwargs.__hash__()
        return hash


class CacheHandler:
    """Handle cache complexity.

    Is initialized by a class and a dictionary mapping the getters
    which support caching to their setters.
    When the getters of the dictionary are called, their parameters
    and their results are cached so that, when the getters are called again
    with the same parameters, the data is directly recovered instead of reevaluated.
    When the setters associated to getters in the input dictionary are called,
    their associated getters' caches are cleared.

    Parameters
    ----------
    cls : type
        Class type

    getters_to_setters_dict : dict[function:list[function]]
        Map class getters to their list of setters which need to be cached
    """

    def __init__(self, cls, getters_to_setters_dict):
        self.getter_to_setters_name = {}
        for getter, setters in getters_to_setters_dict.items():
            setters_name = []
            if setters:
                for setter in setters:
                    setters_name.append(setter.__name__)
            self.getter_to_setters_name[getter.__name__] = setters_name

        self.setter_to_getter_names = {}
        for getter, setters in self.getter_to_setters_name.items():
            for setter in setters:
                self.setter_to_getter_names[setter] = getter

        self.cached = {}

    def handle(self, object, func, *args, **kwargs):
        """Recover data which has already been cached."""
        identifier = MethodIdentifier(func.__name__, args, kwargs)
        if identifier in self.cached:
            return self.cached[identifier]
        elif func.__name__ in self.getter_to_setters_name:
            self.cached[identifier] = func(object, *args, **kwargs)
            setattr(func, "under_cache", False)
            return self.cached[identifier]
        else:
            if (
                func.__name__ in self.setter_to_getter_names
                and self.setter_to_getter_names[func.__name__] in self.cached
            ):
                del self.cached[self.setter_to_getter_names[func.__name__]]
            return func(object, *args, **kwargs)

    def clear(self):
        """Clear cached data."""
        self.cached = {}


def _handle_cache(func):
    """Call the cache handler to either recover cached data, either cache the data or clear some cached data if the method is a setter.

    .. note::
       The method must be used as a decorator.
    """

    def wrapper(self, *args, **kwargs):
        """Call the original function."""
        if hasattr(self, "_cache"):
            return self._cache.handle(self, func, *args, **kwargs)
        else:
            func(self, *args, **kwargs)

    return wrapper


def _setter(func):
    """Add a private attribute to the class (``self._is_set = True``) when a method with this decorator is used.

    .. note::
       The method must be used as a decorator.
    """

    def wrapper(self, *args, **kwargs):
        """Call the original function."""
        if hasattr(self, "_is_set"):
            self._is_set = True
        else:
            setattr(self, "_is_set", True)
        func(self, *args, **kwargs)

    return wrapper
