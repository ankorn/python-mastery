# typedproperty.py

def typedproperty(name, expected_type):
    private_name = '_' + name

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, val)
   
    return value

class String:
    def __set_name__(self, owner, name):
        self.storage_name = f'_{name}'
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.storage_name)
    def __set__(self, instance, value):
        instance.__dict__[self.storage_name] = typedproperty(self.storage_name, value)
        
        
    