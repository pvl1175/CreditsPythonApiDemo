#
# Autogenerated by Thrift Compiler (1.0.0-dev)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys

from thrift.transport import TTransport
all_structs = []


class Variant(object):
    """
    Attributes:
     - v_bool
     - v_i8
     - v_i16
     - v_i32
     - v_i64
     - v_double
     - v_string
     - v_list
     - v_set
     - v_map

    """


    def __init__(self, v_bool=None, v_i8=None, v_i16=None, v_i32=None, v_i64=None, v_double=None, v_string=None, v_list=None, v_set=None, v_map=None,):
        self.v_bool = v_bool
        self.v_i8 = v_i8
        self.v_i16 = v_i16
        self.v_i32 = v_i32
        self.v_i64 = v_i64
        self.v_double = v_double
        self.v_string = v_string
        self.v_list = v_list
        self.v_set = v_set
        self.v_map = v_map

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.BOOL:
                    self.v_bool = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BYTE:
                    self.v_i8 = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.v_i16 = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.v_i32 = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.v_i64 = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.DOUBLE:
                    self.v_double = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.v_string = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.LIST:
                    self.v_list = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = Variant()
                        _elem5.read(iprot)
                        self.v_list.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.SET:
                    self.v_set = set()
                    (_etype9, _size6) = iprot.readSetBegin()
                    for _i10 in range(_size6):
                        _elem11 = Variant()
                        _elem11.read(iprot)
                        self.v_set.add(_elem11)
                    iprot.readSetEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.MAP:
                    self.v_map = {}
                    (_ktype13, _vtype14, _size12) = iprot.readMapBegin()
                    for _i16 in range(_size12):
                        _key17 = Variant()
                        _key17.read(iprot)
                        _val18 = Variant()
                        _val18.read(iprot)
                        self.v_map[_key17] = _val18
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Variant')
        if self.v_bool is not None:
            oprot.writeFieldBegin('v_bool', TType.BOOL, 1)
            oprot.writeBool(self.v_bool)
            oprot.writeFieldEnd()
        if self.v_i8 is not None:
            oprot.writeFieldBegin('v_i8', TType.BYTE, 2)
            oprot.writeByte(self.v_i8)
            oprot.writeFieldEnd()
        if self.v_i16 is not None:
            oprot.writeFieldBegin('v_i16', TType.I16, 3)
            oprot.writeI16(self.v_i16)
            oprot.writeFieldEnd()
        if self.v_i32 is not None:
            oprot.writeFieldBegin('v_i32', TType.I32, 4)
            oprot.writeI32(self.v_i32)
            oprot.writeFieldEnd()
        if self.v_i64 is not None:
            oprot.writeFieldBegin('v_i64', TType.I64, 5)
            oprot.writeI64(self.v_i64)
            oprot.writeFieldEnd()
        if self.v_double is not None:
            oprot.writeFieldBegin('v_double', TType.DOUBLE, 6)
            oprot.writeDouble(self.v_double)
            oprot.writeFieldEnd()
        if self.v_string is not None:
            oprot.writeFieldBegin('v_string', TType.STRING, 7)
            oprot.writeString(self.v_string.encode('utf-8') if sys.version_info[0] == 2 else self.v_string)
            oprot.writeFieldEnd()
        if self.v_list is not None:
            oprot.writeFieldBegin('v_list', TType.LIST, 8)
            oprot.writeListBegin(TType.STRUCT, len(self.v_list))
            for iter19 in self.v_list:
                iter19.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.v_set is not None:
            oprot.writeFieldBegin('v_set', TType.SET, 9)
            oprot.writeSetBegin(TType.STRUCT, len(self.v_set))
            for iter20 in self.v_set:
                iter20.write(oprot)
            oprot.writeSetEnd()
            oprot.writeFieldEnd()
        if self.v_map is not None:
            oprot.writeFieldBegin('v_map', TType.MAP, 10)
            oprot.writeMapBegin(TType.STRUCT, TType.STRUCT, len(self.v_map))
            for kiter21, viter22 in self.v_map.items():
                kiter21.write(oprot)
                viter22.write(oprot)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(Variant)
Variant.thrift_spec = (
    None,  # 0
    (1, TType.BOOL, 'v_bool', None, None, ),  # 1
    (2, TType.BYTE, 'v_i8', None, None, ),  # 2
    (3, TType.I16, 'v_i16', None, None, ),  # 3
    (4, TType.I32, 'v_i32', None, None, ),  # 4
    (5, TType.I64, 'v_i64', None, None, ),  # 5
    (6, TType.DOUBLE, 'v_double', None, None, ),  # 6
    (7, TType.STRING, 'v_string', 'UTF8', None, ),  # 7
    (8, TType.LIST, 'v_list', (TType.STRUCT, [Variant, None], False), None, ),  # 8
    (9, TType.SET, 'v_set', (TType.STRUCT, [Variant, None], False), None, ),  # 9
    (10, TType.MAP, 'v_map', (TType.STRUCT, [Variant, None], TType.STRUCT, [Variant, None], False), None, ),  # 10
)
fix_spec(all_structs)
del all_structs
