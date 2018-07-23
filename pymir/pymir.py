"""A simple helper class to run miriad commands. Although there are 
other packages around (mirpy), I prefer to work with the string 
invocations of the tasks, as you don't have to worry about the annoying
`in` and `map` clashes. 

Raises:
    ValueError -- The error raised by a failed miriad task will be 
                  passed up
    AttributeError -- in __getattr__ to allow Pickles to work
    AttributeError -- in __getattr__ to allow Pickles to work
"""
import subprocess as sp

class mirstr(str):
    """Class to run a miriad task as a method call. Uses str as a base
    to make string printing easier. 
    """
    def __new__(cls, value, *args, over=None, **kwargs):
        """The new constructor for an immutable object

        over {dict} -- Replace keys and values with items 
                       specified in over
        """
        if over is not None:
            for k in over.keys():
                if f"{k}=" not in value:
                    value += f" {k}={over[k]}"
                elif f"{k}=" in value:
                    # Slice out the existing option and replace it
                    a1 = value.index(f"{k}=")
                    b1 = value[a1:].index(" ") + a1
                    value = value[:a1] + f"{k}={over[k]} " + value[b1:]

        obj = str.__new__(cls,value)
        return obj

    def __init__(self, *args, **kwargs):
        """Initialise the instance. I think for immutable types there
        is the __new__() method that should be used. To be looked at. 
        """

        self.p = None
    
    def __str__(self):
        to_print = self
        
        if self.p is not None:
            to_print += '\n'
            to_print += self.p.stdout
            
        return to_print
    
    def run(self, *args, **kwargs):
        self.p = sp.run(self.split(), *args, stdout=sp.PIPE, stderr=sp.PIPE, **kwargs)
        self.p.stdout = self.p.stdout.decode()
        self.p.stderr = self.p.stderr.decode()
        
        if self.p.returncode:
            raise ValueError(self.p.stderr)
        
        return self
    
    def __call__(self, *args, **kwargs):
        return self.run(*args, **kwargs)
        
    def attribute(self, key):
        items = self.split()
        for i in items:
            if f"{key}=" in i:
                return i.split('=')[1]
        
        return None

    def __getattr__(self, name):
        """Assume this is miriad task related. It can be expanded further if
        needed to include header look ups, I guess. 
        
        Arguments:
            name {str} -- attribute from the miriad process str
        """
        try:
            val = self.attribute(name)
            if val is not None:
                return val
            
            raise AttributeError(name)

        except:
            raise AttributeError(name)

if __name__ == '__main__':
    a = mirstr(f"invert vis=test options=op1,op2,op3 imsize=5,5,beam robust=0")
    print(type(a))
    print(a)
    print(a == 'invert vis=test options=mfs,double,sdb  imsize=2,2,beam')

    a = mirstr(f"invert vis=test options=op1,op2,op3", 
                over={"imsize":"2,2,beam", "options":"mfs,double,sdb"})
    print(type(a))
    print(a)

    print(a == 'invert vis=test options=mfs,double,sdb  imsize=2,2,beam')

    pbplot = mirstr("pbplot freq=2.1 bw=2.048 device=/xs", over={'telescop':'ATCA'}).run()
    print(pbplot)