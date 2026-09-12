from validate import Validator

class Structure:
    _fields = ()
    _types = ()

    @classmethod
    def create_init(cls):
        argstr = ','.join(cls._fields)
        code = f'def __init__(self, {argstr}):\n'
        for name in cls._fields:
            code += f'    self.{name} = {name}\n'
            
        locs = {}
        exec(code, locs)
        cls.__init__ = locs['__init__']
        
    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)
    
    def __repr__(self):
        return '%s(%s)' % (type(self).__name__, ', '.join(repr(getattr(self, name)) for name in self._fields))

    def __setattr__(self, name, value):
        if name not in self._fields and not name.startswith('_'):
            raise AttributeError(f'No attribute {name}')
        
        super().__setattr__(name, value) # object setattr
        
    @classmethod
    def from_row(cls, row):
        rowdata = [ func(val) for func, val in zip(cls._types, row) ]
        return cls(*rowdata)

def validate_attributes(cls):
    validators = []
    types = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)
            
            if val.expected_type:
                types.append(val.expected_type)
            
    cls._types = types
            
    cls._fields = [val.name for val in validators]
    
    cls.create_init()
    
    return cls
