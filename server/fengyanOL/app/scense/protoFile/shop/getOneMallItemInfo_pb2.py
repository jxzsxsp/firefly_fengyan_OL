# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/shop/getOneMallItemInfo.proto',
  package='protoFile.shop.getOneMallItemInfo',
  serialized_pb='\n\'protoFile/shop/getOneMallItemInfo.proto\x12!protoFile.shop.getOneMallItemInfo\"\'\n\x19getoneMallItemInfoRequest\x12\n\n\x02id\x18\x01 \x02(\x05\"|\n\x1agetoneMallItemInfoResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12=\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32/.protoFile.shop.getOneMallItemInfo.responseData\"\x1f\n\x0cresponseData\x12\x0f\n\x07\x65ndtime\x18\x01 \x02(\x03')




_GETONEMALLITEMINFOREQUEST = descriptor.Descriptor(
  name='getoneMallItemInfoRequest',
  full_name='protoFile.shop.getOneMallItemInfo.getoneMallItemInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.shop.getOneMallItemInfo.getoneMallItemInfoRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
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
  serialized_start=78,
  serialized_end=117,
)


_GETONEMALLITEMINFORESPONSE = descriptor.Descriptor(
  name='getoneMallItemInfoResponse',
  full_name='protoFile.shop.getOneMallItemInfo.getoneMallItemInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.shop.getOneMallItemInfo.getoneMallItemInfoResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.shop.getOneMallItemInfo.getoneMallItemInfoResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='protoFile.shop.getOneMallItemInfo.getoneMallItemInfoResponse.data', index=2,
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
  serialized_start=119,
  serialized_end=243,
)


_RESPONSEDATA = descriptor.Descriptor(
  name='responseData',
  full_name='protoFile.shop.getOneMallItemInfo.responseData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='endtime', full_name='protoFile.shop.getOneMallItemInfo.responseData.endtime', index=0,
      number=1, type=3, cpp_type=2, label=2,
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
  serialized_start=245,
  serialized_end=276,
)

_GETONEMALLITEMINFORESPONSE.fields_by_name['data'].message_type = _RESPONSEDATA
DESCRIPTOR.message_types_by_name['getoneMallItemInfoRequest'] = _GETONEMALLITEMINFOREQUEST
DESCRIPTOR.message_types_by_name['getoneMallItemInfoResponse'] = _GETONEMALLITEMINFORESPONSE
DESCRIPTOR.message_types_by_name['responseData'] = _RESPONSEDATA

class getoneMallItemInfoRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETONEMALLITEMINFOREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.shop.getOneMallItemInfo.getoneMallItemInfoRequest)

class getoneMallItemInfoResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETONEMALLITEMINFORESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.shop.getOneMallItemInfo.getoneMallItemInfoResponse)

class responseData(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESPONSEDATA
  
  # @@protoc_insertion_point(class_scope:protoFile.shop.getOneMallItemInfo.responseData)

# @@protoc_insertion_point(module_scope)
