# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import app.scense.protoFile.itemInfo_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/strengthen/GetStrengthenPackageInfo.proto',
  package='protoFile.strengthen.GetStrengthenPackageInfo',
  serialized_pb='\n3protoFile/strengthen/GetStrengthenPackageInfo.proto\x12-protoFile.strengthen.GetStrengthenPackageInfo\x1a\x18protoFile/itemInfo.proto\">\n\x1fGetStrengthenPackageInfoRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0f\n\x07\x63urPage\x18\x02 \x02(\x05\"\x90\x01\n GetStrengthenPackageInfoResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\x08\x12K\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32=.protoFile.strengthen.GetStrengthenPackageInfo.StrengthenInfo\"\x82\x01\n\x0eStrengthenInfo\x12\x0f\n\x07nowPage\x18\x01 \x01(\x05\x12\x0f\n\x07maxPage\x18\x02 \x01(\x05\x12N\n\x0bstrItemList\x18\x03 \x03(\x0b\x32\x39.protoFile.strengthen.GetStrengthenPackageInfo.QhItemInfo\"A\n\nQhItemInfo\x12\x0f\n\x07itemtag\x18\x01 \x02(\x05\x12\"\n\x04item\x18\x02 \x02(\x0b\x32\x14.protoFile.ItemsInfo')




_GETSTRENGTHENPACKAGEINFOREQUEST = descriptor.Descriptor(
  name='GetStrengthenPackageInfoRequest',
  full_name='protoFile.strengthen.GetStrengthenPackageInfo.GetStrengthenPackageInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.strengthen.GetStrengthenPackageInfo.GetStrengthenPackageInfoRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='curPage', full_name='protoFile.strengthen.GetStrengthenPackageInfo.GetStrengthenPackageInfoRequest.curPage', index=1,
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
  serialized_start=128,
  serialized_end=190,
)


_GETSTRENGTHENPACKAGEINFORESPONSE = descriptor.Descriptor(
  name='GetStrengthenPackageInfoResponse',
  full_name='protoFile.strengthen.GetStrengthenPackageInfo.GetStrengthenPackageInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.strengthen.GetStrengthenPackageInfo.GetStrengthenPackageInfoResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.strengthen.GetStrengthenPackageInfo.GetStrengthenPackageInfoResponse.result', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='protoFile.strengthen.GetStrengthenPackageInfo.GetStrengthenPackageInfoResponse.data', index=2,
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
  serialized_start=193,
  serialized_end=337,
)


_STRENGTHENINFO = descriptor.Descriptor(
  name='StrengthenInfo',
  full_name='protoFile.strengthen.GetStrengthenPackageInfo.StrengthenInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='nowPage', full_name='protoFile.strengthen.GetStrengthenPackageInfo.StrengthenInfo.nowPage', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='maxPage', full_name='protoFile.strengthen.GetStrengthenPackageInfo.StrengthenInfo.maxPage', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='strItemList', full_name='protoFile.strengthen.GetStrengthenPackageInfo.StrengthenInfo.strItemList', index=2,
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
  serialized_start=340,
  serialized_end=470,
)


_QHITEMINFO = descriptor.Descriptor(
  name='QhItemInfo',
  full_name='protoFile.strengthen.GetStrengthenPackageInfo.QhItemInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='itemtag', full_name='protoFile.strengthen.GetStrengthenPackageInfo.QhItemInfo.itemtag', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='item', full_name='protoFile.strengthen.GetStrengthenPackageInfo.QhItemInfo.item', index=1,
      number=2, type=11, cpp_type=10, label=2,
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
  serialized_start=472,
  serialized_end=537,
)

_GETSTRENGTHENPACKAGEINFORESPONSE.fields_by_name['data'].message_type = _STRENGTHENINFO
_STRENGTHENINFO.fields_by_name['strItemList'].message_type = _QHITEMINFO
_QHITEMINFO.fields_by_name['item'].message_type = app.scense.protoFile.itemInfo_pb2._ITEMSINFO
DESCRIPTOR.message_types_by_name['GetStrengthenPackageInfoRequest'] = _GETSTRENGTHENPACKAGEINFOREQUEST
DESCRIPTOR.message_types_by_name['GetStrengthenPackageInfoResponse'] = _GETSTRENGTHENPACKAGEINFORESPONSE
DESCRIPTOR.message_types_by_name['StrengthenInfo'] = _STRENGTHENINFO
DESCRIPTOR.message_types_by_name['QhItemInfo'] = _QHITEMINFO

class GetStrengthenPackageInfoRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETSTRENGTHENPACKAGEINFOREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.strengthen.GetStrengthenPackageInfo.GetStrengthenPackageInfoRequest)

class GetStrengthenPackageInfoResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETSTRENGTHENPACKAGEINFORESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.strengthen.GetStrengthenPackageInfo.GetStrengthenPackageInfoResponse)

class StrengthenInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STRENGTHENINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.strengthen.GetStrengthenPackageInfo.StrengthenInfo)

class QhItemInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QHITEMINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.strengthen.GetStrengthenPackageInfo.QhItemInfo)

# @@protoc_insertion_point(module_scope)
