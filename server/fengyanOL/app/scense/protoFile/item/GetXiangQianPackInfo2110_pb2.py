# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import app.scense.protoFile.itemInfo_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/item/GetXiangQianPackInfo2110.proto',
  package='protoFile.item.GetXiangQianPackInfo2110',
  serialized_pb='\n-protoFile/item/GetXiangQianPackInfo2110.proto\x12\'protoFile.item.GetXiangQianPackInfo2110\x1a\x18protoFile/itemInfo.proto\"7\n\x1bGetXiangQianPackInfoRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0c\n\x04page\x18\x02 \x02(\x05\"\x88\x01\n\x1cGetXiangQianPackInfoResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\x08\x12G\n\nxqPackInfo\x18\x03 \x01(\x0b\x32\x33.protoFile.item.GetXiangQianPackInfo2110.XQPackInfo\"w\n\nXQPackInfo\x12\x0f\n\x07\x63urPage\x18\x01 \x01(\x05\x12\x0f\n\x07maxPage\x18\x02 \x01(\x05\x12G\n\nxqItemInfo\x18\x03 \x03(\x0b\x32\x33.protoFile.item.GetXiangQianPackInfo2110.XQItemInfo\"E\n\nXQItemInfo\x12\x0e\n\x06inBody\x18\x01 \x01(\x05\x12\'\n\titemsInfo\x18\x02 \x01(\x0b\x32\x14.protoFile.ItemsInfo')




_GETXIANGQIANPACKINFOREQUEST = descriptor.Descriptor(
  name='GetXiangQianPackInfoRequest',
  full_name='protoFile.item.GetXiangQianPackInfo2110.GetXiangQianPackInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.item.GetXiangQianPackInfo2110.GetXiangQianPackInfoRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='page', full_name='protoFile.item.GetXiangQianPackInfo2110.GetXiangQianPackInfoRequest.page', index=1,
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
  serialized_start=116,
  serialized_end=171,
)


_GETXIANGQIANPACKINFORESPONSE = descriptor.Descriptor(
  name='GetXiangQianPackInfoResponse',
  full_name='protoFile.item.GetXiangQianPackInfo2110.GetXiangQianPackInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.item.GetXiangQianPackInfo2110.GetXiangQianPackInfoResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.item.GetXiangQianPackInfo2110.GetXiangQianPackInfoResponse.result', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='xqPackInfo', full_name='protoFile.item.GetXiangQianPackInfo2110.GetXiangQianPackInfoResponse.xqPackInfo', index=2,
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
  serialized_start=174,
  serialized_end=310,
)


_XQPACKINFO = descriptor.Descriptor(
  name='XQPackInfo',
  full_name='protoFile.item.GetXiangQianPackInfo2110.XQPackInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='curPage', full_name='protoFile.item.GetXiangQianPackInfo2110.XQPackInfo.curPage', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='maxPage', full_name='protoFile.item.GetXiangQianPackInfo2110.XQPackInfo.maxPage', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='xqItemInfo', full_name='protoFile.item.GetXiangQianPackInfo2110.XQPackInfo.xqItemInfo', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=312,
  serialized_end=431,
)


_XQITEMINFO = descriptor.Descriptor(
  name='XQItemInfo',
  full_name='protoFile.item.GetXiangQianPackInfo2110.XQItemInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='inBody', full_name='protoFile.item.GetXiangQianPackInfo2110.XQItemInfo.inBody', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='itemsInfo', full_name='protoFile.item.GetXiangQianPackInfo2110.XQItemInfo.itemsInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=433,
  serialized_end=502,
)

_GETXIANGQIANPACKINFORESPONSE.fields_by_name['xqPackInfo'].message_type = _XQPACKINFO
_XQPACKINFO.fields_by_name['xqItemInfo'].message_type = _XQITEMINFO
_XQITEMINFO.fields_by_name['itemsInfo'].message_type = app.scense.protoFile.itemInfo_pb2._ITEMSINFO
DESCRIPTOR.message_types_by_name['GetXiangQianPackInfoRequest'] = _GETXIANGQIANPACKINFOREQUEST
DESCRIPTOR.message_types_by_name['GetXiangQianPackInfoResponse'] = _GETXIANGQIANPACKINFORESPONSE
DESCRIPTOR.message_types_by_name['XQPackInfo'] = _XQPACKINFO
DESCRIPTOR.message_types_by_name['XQItemInfo'] = _XQITEMINFO

class GetXiangQianPackInfoRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETXIANGQIANPACKINFOREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.item.GetXiangQianPackInfo2110.GetXiangQianPackInfoRequest)

class GetXiangQianPackInfoResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETXIANGQIANPACKINFORESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.item.GetXiangQianPackInfo2110.GetXiangQianPackInfoResponse)

class XQPackInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _XQPACKINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.item.GetXiangQianPackInfo2110.XQPackInfo)

class XQItemInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _XQITEMINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.item.GetXiangQianPackInfo2110.XQItemInfo)

# @@protoc_insertion_point(module_scope)
