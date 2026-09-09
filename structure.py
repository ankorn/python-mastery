class Structure:
    _fields = ()
    
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        
        for name, value in zip(self._fields, args):
            self.__setattr__(name, value)
            
    def __repr__(self):
        return '%s(%s)' % (type(self).__name__, ', '.join(repr(getattr(self, name)) for name in self._fields))
    

    def __setattr__(self, name, value):
        if name not in self._fields and not name.startswith('_'):
            raise AttributeError(f'No attribute {name}')
        
        super().__setattr__(name, value) # object setattr
