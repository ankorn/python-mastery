## cooperative inheritance
- class X(Base) => super().base_class_method() does not call Base class, but next class in __mro__
- __mro__ is defined my a child

## class
- @classmethod handles class state(not instance state like normal method); passes cls on which method was called
- cls state meant to be readonly: assignment to instance(self.) always creates instance state (it does not modify the class even if the same variable exists in cls)

## closure
- you can use @property and @.setter without class in clousure