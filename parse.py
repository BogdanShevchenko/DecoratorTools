from collections.abc import Callable, Sequence


def get_args_dict(f: Callable, args: Sequence, kwargs: dict) -> dict:
    """
    By given function and passed args list and kwargs dict, return dictionary with names and values of all arguments,
    passed to the function, including defaults for those which wasn't passed
    :param f: any function
    :param args: all positional arguments, passed to function f
    :param kwargs: all named arguments passed to function f
    :return: dictionary with all parameters of the function. If function have **kwargs unpacking, there will be 'kwargs'
    parameter in resulting dict with all unpacked arguments,
    and also all this arguments will be in resulting dict by themselves
    """
    # co_varnames is list of all variables in function in order of definition, only order exception is args
    var_names = f.__code__.co_varnames
    # co_argcount if number of all named parameters before *args, or before **kwargs (or all parameters if no **kwargs)
    pos_arg_count = min(f.__code__.co_argcount, len(args))
    # 3 and 4 bit of flags indicates if there are *args and **kwargs unpacking in function
    flags = '{:04b}'.format(f.__code__.co_flags)
    has_args = int(flags[-3])
    has_kwargs = int(flags[-4])
    kwarg_name = [None, var_names[-1]][has_kwargs]
    # *args is always after all other named variables but before kwargs
    arg_name = [None, var_names[-1 - has_kwargs]][has_args]
    kwargs.update(zip(var_names[:pos_arg_count], args[:pos_arg_count]))
    if has_kwargs:
        kwargs[kwarg_name] = {i: kwargs[i] for i in kwargs if (i not in var_names) or (i in [arg_name, kwarg_name])}
    if has_args:
        kwargs[arg_name] = args[pos_arg_count:]
        defaults = f.__kwdefaults__ or {}
    else:
        args_from_named = var_names[pos_arg_count: len(args)]
        args_from_named_values = args[pos_arg_count:]
        kwargs.update(zip(args_from_named, args_from_named_values))

        defaults = f.__defaults__ or []
        defaults = dict(zip(
            var_names[-len(defaults) - has_kwargs:(-1 if has_kwargs else None)],
            defaults
        ))
    defaults.update(kwargs)
    return defaults
