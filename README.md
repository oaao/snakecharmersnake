# snakecharmersnake
a python interpreter, written in python (learning project from reference)

## setup
crack your knuckles and grab a tea

## usage

The **Interpreter** object can be used instruction-by-instruction:

```python
>>> from objects import Interpreter
>>>
>>> i = Interpreter()
>>> i.LOAD_VALUE(10)
>>> i.LOAD_VALUE(20)
>>> i.ADD_TWO_VALUES()
>>> i.PRINT_ANSWER()
30
```

The **Interpreter** can also take a dictionary of actions in the format:

```python
ACTIONS = {

    'instructions': [
        ('INSTRUCTION', val_index),
        ...
    ],

    'values':       [v1, v2, v3, ...]
}
```
For example,
```python
>>> evals = {
...     'instructions': [
...         ('LOAD_VALUE', 0),
...         ('LOAD_VALUE', 1),
...         ('ADD_TWO_VALUES', None),
...         ('PRINT_ANSWER', None),
...     ]
...     ,
...     'values': [
...         7, 5
...     ]
... }
>>>
>>> i.run(evals)
12
```
