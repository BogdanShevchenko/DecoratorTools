Function to parse parameters of function without access to it's inside.
When we pass some positional arguments and named arguments to function, they are visible inside the function as some parameters. Also, some of parameters can be taken from default values if not passed.

In example if we define function

```python
def f(a, b, *args, c=1, d=2, **kwargs):
	return a+b
```

and call it with arguments

```python
f(10, b=5)
```

parameters of function will be
```python
{a: 10, b: 5, args: [], c: 1, d: 2, kwargs: {}}
```

The same result will be returned by
```python
from from parce import get_args_dict

get_args_dict(f, args=[10], kwargs={'b': 5})
```
