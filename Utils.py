def set_proc_name(newname):
    from ctypes import cdll, byref, create_string_buffer
    libc = cdll.LoadLibrary('libc.so.6')
    buff = create_string_buffer(len(newname)+1)
    buff.value = bytes(newname, "UTF-8")
    libc.prctl(15, byref(buff), 0, 0, 0)

class Pointer():
    def __init__(self,data:int | bytes):
        if type(data) is int:
            self.value = data % (256**5)
        elif type(data) is bytes:
            self.value = int.from_bytes(data,'big') % (256**5)
        else:
            raise TypeError("Pointer must be initiated with int or bytes object")
        
    def __iadd__(self,other):
        if type(other) is int:
            self.value += other
            return self
        else:
            raise TypeError(f"Couldn't add Pointer and {type(other)}")
        
    def __isub__(self,other):
        if type(other) is int:
            self.value -= other
            return self
        else:
            raise TypeError(f"Couldn't sub Pointer and {type(other)}")
        
    def __imul__(self,other):
        if type(other) is int:
            self.value *= other
            return self
        else:
            raise TypeError(f"Couldn't mult Pointer and {type(other)}")
        
    def __idiv__(self,other):
        if type(other) is int:
            self.value /= other
            return self
        else:
            raise TypeError(f"Couldn't div Pointer and {type(other)}")
        
    def __imod__(self,other):
        if type(other) is int:
            self.value %= other
            return self
        else:
            raise TypeError(f"Couldn't mod Pointer and {type(other)}")

    def __repr__(self):
        return f"Pointer({self.value})"
    
    def __int__(self):
        return self.value
    
    def __bytes__(self):
        return int.to_bytes(self.value,'big')
    
    def __iter__(self):
        return iter(bytes(self))

    def __index__(self):
        return int(self)

    def __lt__(self,other):
        if type(other) is int:
            return int(self) < other
        else:
            return self < other
        
    def __le__(self,other):
        if type(other) is int:
            return int(self) <= other
        else:
            return self <= other
        
    def __gt__(self,other):
        if type(other) is int:
            return int(self) > other
        else:
            return self > other
        
    def __ge__(self,other):
        if type(other) is int:
            return int(self) >= other
        else:
            return self >= other
            
    def __eq__(self,other):
        if type(other) is int:
            return int(self) == other
        else:
            return self == other
            
    
    def __add__(self,other):
        if type(other) is int:
            return self.value + other
        else:
            raise TypeError(f"Couldn't add Pointer and {type(other)}")
    def __sub__(self,other):
        if type(other) is int:
            return self.value - other
        else:
            raise TypeError(f"Couldn't sub Pointer and {type(other)}")
    def __mul__(self,other):
        if type(other) is int:
            return self.value * other
        else:
            raise TypeError(f"Couldn't mult Pointer and {type(other)}")
    def __div__(self,other):
        if type(other) is int:
            return self.value / other
        else:
            raise TypeError(f"Couldn't div Pointer and {type(other)}")
    def __mod__(self,other):
        if type(other) is int:
            return self.value % other
        else:
            raise TypeError(f"Couldn't mod Pointer and {type(other)}")