from typing import NamedTuple


def class_handling_cache(cls):
    """Class decorator used to handle cache.
    To use it, add a ''_to_cache'' static attribute in the given class.
    This private dictionary should map class getters to their list of setters
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
    method_name: str
    args: list
    kwargs: dict

    def __eq__(self, other):
        if isinstance(other, str):
            return self.method_name == other
        else:
            return self.method_name == other.method_name \
                   and self.args == other.args \
                   and self.kwargs == other.kwargs

    def __hash__(self):
        hash = self.method_name.__hash__()
        if self.args:
            hash += self.args.__hash__()
        if self.kwargs:
            hash += self.kwargs.__hash__()
        return hash


class CacheHandler:
    def __init__(self, cls, getters_to_setters_list):

        self.getter_to_setters_name = {}
        for getter, setters in getters_to_setters_list.items():
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
        identifier = MethodIdentifier(func.__name__, args, kwargs)
        if identifier in self.cached:
            return self.cached[identifier]
        elif func.__name__ in self.getter_to_setters_name:
            self.cached[identifier] = func(object, *args, **kwargs)
            setattr(func, "under_cache", False)
            return self.cached[identifier]
        else:
            if func.__name__ in self.setter_to_getter_names \
                    and self.setter_to_getter_names[func.__name__] in self.cached:
                del self.cached[self.setter_to_getter_names[func.__name__]]
            return func(object, *args, **kwargs)


def _handle_cache(func):
    """Check that the method being called matches a certain server version.

    .. note::
       The method must be used as a decorator.
    """

    def wrapper(self, *args, **kwargs):
        """Call the original function"""
        if hasattr(self, "_cache"):
            return self._cache.handle(self, func, *args, **kwargs)
        else:
            func(self, *args, **kwargs)

    return wrapper
