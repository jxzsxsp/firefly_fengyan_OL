# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/zhanyi/GetNowZhanYiInfo4500.proto',
  package='protoFile.zhanyi.GetNowZhanYiInfo4500',
  serialized_pb='\n+protoFile/zhanyi/GetNowZhanYiInfo4500.proto\x12%protoFile.zhanyi.GetNowZhanYiInfo4500\"4\n\x17GetNowZhanYiInfoRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05index\x18\x02 \x02(\x05\"\x84\x01\n\x18GetNowZhanYiInfoResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x02(\t\x12G\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x39.protoFile.zhanyi.GetNowZhanYiInfo4500.ZhanyiResponseData\"\xf1\x01\n\x12ZhanyiResponseData\x12\r\n\x05index\x18\x01 \x01(\x05\x12\x0f\n\x07maxpage\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x04 \x01(\t\x12\r\n\x05state\x18\x05 \x01(\x05\x12\x45\n\x07monster\x18\x06 \x01(\x0b\x32\x34.protoFile.zhanyi.GetNowZhanYiInfo4500.ZhanyiMonster\x12I\n\x0czhangjielist\x18\x07 \x03(\x0b\x32\x33.protoFile.zhanyi.GetNowZhanYiInfo4500.ZhangJieInfo\"\x94\x01\n\x0cZhangJieInfo\x12\x12\n\nzhangjieid\x18\x01 \x01(\x05\x12\r\n\x05state\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x04 \x01(\t\x12\x45\n\x07monster\x18\x05 \x01(\x0b\x32\x34.protoFile.zhanyi.GetNowZhanYiInfo4500.ZhanyiMonster\";\n\rZhanyiMonster\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08resource\x18\x03 \x01(\x05')




_GETNOWZHANYIINFOREQUEST = descriptor.Descriptor(
  name='GetNowZhanYiInfoRequest',
  full_name='protoFile.zhanyi.GetNowZhanYiInfo4500.GetNowZhanYiInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.zhanyi.GetNowZhanYiInfo4500.GetNowZhanYiInfoRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='index', full_name='protoFile.zhanyi.GetNowZhanYiInfo4500.GetNowZhanYiInfoRequest.index', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=86,
  serialized_end=138,
)


_GETNOWZHANYIINFORESPONSE = descriptor.Descriptor(
  name='GetNowZhanYiInfoResponse',
  full_name='protoFile.zhanyi.GetNowZhanYiInfo4500.GetNowZhanYiInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.zhanyi.GetNowZhanYiInfo4500.GetNowZhanYiInfoResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.zhanyi.GetNowZhanYiInfo4500.GetNowZhanYiInfoResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='protoFile.zhanyi.GetNowZhanYiInfo4500.GetNowZhanYiInfoResponse.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=141,
  serialized_end=273,
)


_ZHANYIRESPONSEDATA = descriptor.Descriptor(
  name='ZhanyiResponseData',
  full_name='protoFile.zhanyi.GetNowZhanYiInfo4500.ZhanyiResponseData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='index', full_name='protoFile.zhanyi.GetNowZhanYiInfo4500.ZhanyiResponseData.index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='maxpage', full_name='protoFile.zhanyi.GetNowZhanYiInfo4500.ZhanyiResponseData.maxpage', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='name', full_name='protoFile.zhanyi.GetNowZhanYiInfo4500.ZhanyiResponseData.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='desc', full_name='protoFile.zhanyi.GetNowZhanYiInfo4500.ZhanyiResponseData.desc', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='state', full_name='protoFile.zhanyi.GetNowZhanYiInfo4500.ZhanyiResponseData.state', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='monster', full_name='protoFile.zhanyi.GetNowZhanYiInfo4500.ZhanyiResponseData.monster', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='zhangjielist', full_name='protoFile.zhanyi.GetNowZhanYiInfo4500.ZhanyiResponseData.zhangjielist', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=276,
  serialized_end=517,
)


_ZHANGJIEINFO = descriptor.Descriptor(
  name='ZhangJieInfo',
  full_name='protoFile.zhanyi.GetNowZhanYiInfo4500.ZhangJieInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='zhangjieid', full_name='protoFile.zhanyi.GetNowZhanYiInfo4500.ZhangJieInfo.zhangjieid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='state', full_name='protoFile.zhanyi.GetNowZhanYiInfo4500.ZhangJieInfo.state', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='name', full_name='protoFile.zhanyi.GetNowZhanYiInfo4500.ZhangJieInfo.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='desc', full_name='protoFile.zhanyi.GetNowZhanYiInfo4500.ZhangJieInfo.desc', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='monster', full_name='protoFile.zhanyi.GetNowZhanYiInfo4500.ZhangJieInfo.monster', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=520,
  serialized_end=668,
)


_ZHANYIMONSTER = descriptor.Descriptor(
  name='ZhanyiMonster',
  full_name='protoFile.zhanyi.GetNowZhanYiInfo4500.ZhanyiMonster',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.zhanyi.GetNowZhanYiInfo4500.ZhanyiMonster.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='name', full_name='protoFile.zhanyi.GetNowZhanYiInfo4500.ZhanyiMonster.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='resource', full_name='protoFile.zhanyi.GetNowZhanYiInfo4500.ZhanyiMonster.resource', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=670,
  serialized_end=729,
)

_GETNOWZHANYIINFORESPONSE.fields_by_name['data'].message_type = _ZHANYIRESPONSEDATA
_ZHANYIRESPONSEDATA.fields_by_name['monster'].message_type = _ZHANYIMONSTER
_ZHANYIRESPONSEDATA.fields_by_name['zhangjielist'].message_type = _ZHANGJIEINFO
_ZHANGJIEINFO.fields_by_name['monster'].message_type = _ZHANYIMONSTER
DESCRIPTOR.message_types_by_name['GetNowZhanYiInfoRequest'] = _GETNOWZHANYIINFOREQUEST
DESCRIPTOR.message_types_by_name['GetNowZhanYiInfoResponse'] = _GETNOWZHANYIINFORESPONSE
DESCRIPTOR.message_types_by_name['ZhanyiResponseData'] = _ZHANYIRESPONSEDATA
DESCRIPTOR.message_types_by_name['ZhangJieInfo'] = _ZHANGJIEINFO
DESCRIPTOR.message_types_by_name['ZhanyiMonster'] = _ZHANYIMONSTER

class GetNowZhanYiInfoRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETNOWZHANYIINFOREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.zhanyi.GetNowZhanYiInfo4500.GetNowZhanYiInfoRequest)

class GetNowZhanYiInfoResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETNOWZHANYIINFORESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.zhanyi.GetNowZhanYiInfo4500.GetNowZhanYiInfoResponse)

class ZhanyiResponseData(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ZHANYIRESPONSEDATA
  
  # @@protoc_insertion_point(class_scope:protoFile.zhanyi.GetNowZhanYiInfo4500.ZhanyiResponseData)

class ZhangJieInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ZHANGJIEINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.zhanyi.GetNowZhanYiInfo4500.ZhangJieInfo)

class ZhanyiMonster(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ZHANYIMONSTER
  
  # @@protoc_insertion_point(class_scope:protoFile.zhanyi.GetNowZhanYiInfo4500.ZhanyiMonster)

# @@protoc_insertion_point(module_scope)
