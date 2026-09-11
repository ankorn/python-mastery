from logcall import logged, logformat
from validate import validated, Integer

class Spam:
    @logged
    def instance_method(self):
        pass

    @logged
    @classmethod
    def class_method(cls):
        pass

    @logged
    @staticmethod
    def static_method():
        pass

    @logged
    @property
    def property_method(self):
        pass
    
s = Spam()
s.instance_method()
Spam.class_method()
Spam.static_method()
s.property_method