import inspect
import sys


def _sort_supported_kwargs(bound_method, **kwargs):
    """Filters the kwargs for a given method."""
    # Ignore warnings unless specified
    if not sys.warnoptions:
        import warnings

        warnings.simplefilter("ignore")
    # Get supported arguments
    supported_args = inspect.getfullargspec(bound_method).args
    kwargs_in = {}
    kwargs_not_avail = {}
    # Filter the given arguments
    for key, item in kwargs.items():
        if key in supported_args:
            kwargs_in[key] = item
        else:
            kwargs_not_avail[key] = item
    # Prompt a warning for arguments filtered out
    if len(kwargs_not_avail) > 0:
        txt = f"The following arguments are not supported by {bound_method}: "
        txt += str(kwargs_not_avail)
        warnings.warn(txt)
    # Return the accepted arguments
    return kwargs_in
