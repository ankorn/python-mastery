from logcall import logged, logformat
from validate import validated, Integer, enforce

class Spam:
    @logged
    def instance_method(self):
        pass

    @classmethod
    @logged
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
    
@enforce(x=Integer, y=Integer, return_=Integer)
def pow(x, y):
    return x ** y

print(pow(1, -2))