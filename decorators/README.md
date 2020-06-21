# Decorators

Decorators can be interpreted in the context of *function building*

```
@deco 
def my_func():
    pass
```
    
should be interpreted as 

```deco(my_func)```

In other words, the decorator simply wraps the function. 

In another life, one might interpret my_func as a callback 