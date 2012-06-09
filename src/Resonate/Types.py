'''
Created on Jun 6, 2012

@author: Joe
'''
import struct
from twisted.internet import protocol

class Protocol(protocol.Protocol):
    neededbytes = 0
    def setNeededBytes(self, bytecount):
        #if ('parent' in locals()):
        #    change = self.parent
        self.parent.setNeededBytes(bytecount)
        
class Byte(Protocol):
    def __init__(self, parent):
        self.parent = parent
        self.setNeededBytes(1)
    def receive(self, extract):
        return struct.unpack(">b",extract)[0]
    @staticmethod
    def send(value):
        return struct.pack(">b", value)
    
class UnsignedByte(Protocol):
    def __init__(self, parent):
        self.parent = parent
        self.setNeededBytes(1)
    def receive(self, extract):
        return struct.unpack(">B",extract)[0]
    @staticmethod
    def send(value):
        return struct.pack(">B", value)
    
class Short(Protocol):
    def __init__(self, parent):
        self.parent = parent
        self.setNeededBytes(2)
    def receive(self, extract):
        #return ord(extract[0]) << 8 | ord(extract[1])
        return struct.unpack(">h",extract)[0]
    @staticmethod
    def send(value):
        return struct.pack(">h", value)
    
class UnsignedShort(Protocol):
    def __init__(self, parent):
        self.parent = parent
        self.setNeededBytes(2)
    def receive(self, extract):
        #return ord(extract[0]) << 8 | ord(extract[1])
        return struct.unpack(">H",extract)[0]
    @staticmethod
    def send(value):
        return struct.pack(">H", value)

class Integer(Protocol):
    def __init__(self, parent):
        self.parent = parent
        self.setNeededBytes(2)
    def receive(self, extract):
        #return (ord(extract[0]) << 24 | ord(extract[1]) << 16 |
        #        ord(extract[2]) << 8  | ord(extract[3]))
        return struct.unpack(">i",extract)[0]
    @staticmethod
    def send(value):
        return struct.pack(">i", value)
    
class Long(Protocol):
    def __init__(self, parent):
        self.parent = parent
        self.setNeededBytes(2)
    def receive(self, extract):
        #return (ord(extract[0]) << 64 | ord(extract[1]) << 56 |
        #        ord(extract[2]) << 40 | ord(extract[3]) << 32 |
        #        ord(extract[4]) << 24 | ord(extract[5]) << 16 |
        #        ord(extract[6]) << 8  | ord(extract[7]))
        return struct.unpack(">l",extract)[0]
    @staticmethod
    def send(value):
        return struct.pack(">l", value)
    
class Float(Protocol):
    def __init__(self, parent):
        self.parent = parent
        self.setNeededBytes(4)
    def receive(self, extract):
        return struct.unpack(">f",extract)[0]
    @staticmethod
    def send(value):
        return struct.pack(">f", value)
    
class Double(Protocol):
    def __init__(self, parent):
        self.parent = parent
        self.setNeededBytes(8)
    def receive(self, extract):
        return struct.unpack(">d",extract)[0]
    @staticmethod
    def send(value):
        return struct.pack(">d", value)

class String(Protocol):
    i = 0
    def __init__(self, parent):
        self.parent = parent
        self.short = Short(self)

    def receive(self, extract):
        if self.i == 0:
            length = self.short.receive(extract)
            self.setNeededBytes(length*2)
            self.i= 1
        else:
            return extract
        return None
    @staticmethod
    def send(value):
        return Short.send(len(value))+value.encode(value, "utf-16_be")
    
class Slot(Protocol):
    i = 0
    def __init__(self, parent):
        self.parent = parent
        self.read = Short(self)

    def receive(self, extract):
        if self.i == 0:
            length = self.read.receive(extract)
            self.setNeededBytes(length*2)
            
            if (length < 0):
                return False #TODO: return something better ;)
            
            self.read = Byte(self)
            
            self.i= 1
        elif self.i == 1:
            self.itemid = self.read.receive(extract)
            
            self.read = Short(self)
            
            self.i = 2
        elif self.i == 2:
            self.metavalue = self.read.receive(extract)
            
        return None

class Bool(Protocol):
    def __init__(self, parent):
        self.parent = parent
        self.setNeededBytes(1)
    def receive(self, extract):
        return ord(extract)!=0
    @staticmethod
    def send(value):
        return struct.pack(">b", value)

class Metadata(Protocol):
    def __init__(self, parent):
        self.parent = parent
        self.reader = Short(self)
        self.i = 0
        self.metadata = {}
    def receive(self, extract):
        if self.i == 0:
            self.x = self.reader.receive(extract)
            self.i = 1
        if self.i == 1:
            if self.x != 127:
                self.index = self.x & 0x1F
                self.ty = self.x >> 5
                if   self.ty == 0: self.reader = Byte(self)
                elif self.ty == 1: self.reader = Short(self)
                elif self.ty == 2: self.reader = Integer(self)
                elif self.ty == 3: self.reader = Float(self)
                elif self.ty == 4: self.reader = String(self)
                elif self.ty == 5:
                    self.i = 3
                    #skipping our reader due to complexity
                    self.setNeededBytes(5)
                elif self.ty == 6:
                    self.i = 4
                    self.setNeededBytes(4*4)
        if self.i == 2:
            value = self.reader.receive(extract)
            self.metadata[self.index] = (self.ty, value)
            self.i = 1
        if self.i == 3:
            val = {}
            (val["id"], val["count"], val["damage"]) = struct.unpack(">hBh");
            self.metadata[self.index] = (self.ty, value)
            self.i = 1
        if self.i == 4:
            value = struct.unpack(">iii");
            self.metadata[self.index] = (self.ty, value)
            self.i = 1