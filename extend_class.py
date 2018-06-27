# We want to extend classes with new methods
# Source: https://gist.github.com/victorlei/5968685

def extend_class(cls):
    return lambda f: (setattr(cls,f.__name__,f) or f)
