# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/item/UnloadXiangQian2113.proto',
  package='protoFile.item.UnloadXiangQian2113',
  serialized_pb='\n(protoFile/item/UnloadXiangQian2113.proto\x12\"protoFile.item.UnloadXiangQian2113\"U\n\x16UnLoadXiangQianRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0f\n\x07\x65quipId\x18\x02 \x02(\x05\x12\x0c\n\x04type\x18\x03 \x02(\x05\x12\x10\n\x08position\x18\x04 \x02(\x05\":\n\x17UnLoadXiangQianResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\x08')




_UNLOADXIANGQIANREQUEST = descriptor.Descriptor(
  name='UnLoadXiangQianRequest',
  full_name='protoFile.item.UnloadXiangQian2113.UnLoadXiangQianRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.item.UnloadXiangQian2113.UnLoadXiangQianRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='equipId', full_name='protoFile.item.UnloadXiangQian2113.UnLoadXiangQianRequest.equipId', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='protoFile.item.UnloadXiangQian2113.UnLoadXiangQianRequest.type', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='position', full_name='protoFile.item.UnloadXiangQian2113.UnLoadXiangQianRequest.position', index=3,
      number=4, type=5, cpp_type=1, label=2,
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
  serialized_start=80,
  serialized_end=165,
)


_UNLOADXIANGQIANRESPONSE = descriptor.Descriptor(
  name='UnLoadXiangQianResponse',
  full_name='protoFile.item.UnloadXiangQian2113.UnLoadXiangQianResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.item.UnloadXiangQian2113.UnLoadXiangQianResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.item.UnloadXiangQian2113.UnLoadXiangQianResponse.result', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=167,
  serialized_end=225,
)

DESCRIPTOR.message_types_by_name['UnLoadXiangQianRequest'] = _UNLOADXIANGQIANREQUEST
DESCRIPTOR.message_types_by_name['UnLoadXiangQianResponse'] = _UNLOADXIANGQIANRESPONSE

class UnLoadXiangQianRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UNLOADXIANGQIANREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.item.UnloadXiangQian2113.UnLoadXiangQianRequest)

class UnLoadXiangQianResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UNLOADXIANGQIANRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.item.UnloadXiangQian2113.UnLoadXiangQianResponse)

# @@protoc_insertion_point(module_scope)
