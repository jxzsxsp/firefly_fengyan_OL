# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/packageInfo/splitItemsInPack.proto',
  package='protoFile.packageInfo.splitItemsInPack',
  serialized_pb='\n,protoFile/packageInfo/splitItemsInPack.proto\x12&protoFile.packageInfo.splitItemsInPack\"v\n\x17splitItemsInPackRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x13\n\x0bpackageType\x18\x02 \x02(\x05\x12\x14\n\x0c\x66romposition\x18\x03 \x02(\x05\x12\x12\n\ntoposition\x18\x04 \x02(\x05\x12\x10\n\x08splitnum\x18\x05 \x02(\x05\"I\n\x18splitItemsInPackResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x05')




_SPLITITEMSINPACKREQUEST = descriptor.Descriptor(
  name='splitItemsInPackRequest',
  full_name='protoFile.packageInfo.splitItemsInPack.splitItemsInPackRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.packageInfo.splitItemsInPack.splitItemsInPackRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='packageType', full_name='protoFile.packageInfo.splitItemsInPack.splitItemsInPackRequest.packageType', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='fromposition', full_name='protoFile.packageInfo.splitItemsInPack.splitItemsInPackRequest.fromposition', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='toposition', full_name='protoFile.packageInfo.splitItemsInPack.splitItemsInPackRequest.toposition', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='splitnum', full_name='protoFile.packageInfo.splitItemsInPack.splitItemsInPackRequest.splitnum', index=4,
      number=5, type=5, cpp_type=1, label=2,
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
  serialized_start=88,
  serialized_end=206,
)


_SPLITITEMSINPACKRESPONSE = descriptor.Descriptor(
  name='splitItemsInPackResponse',
  full_name='protoFile.packageInfo.splitItemsInPack.splitItemsInPackResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.packageInfo.splitItemsInPack.splitItemsInPackResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.packageInfo.splitItemsInPack.splitItemsInPackResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='protoFile.packageInfo.splitItemsInPack.splitItemsInPackResponse.data', index=2,
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
  serialized_start=208,
  serialized_end=281,
)

DESCRIPTOR.message_types_by_name['splitItemsInPackRequest'] = _SPLITITEMSINPACKREQUEST
DESCRIPTOR.message_types_by_name['splitItemsInPackResponse'] = _SPLITITEMSINPACKRESPONSE

class splitItemsInPackRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SPLITITEMSINPACKREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.packageInfo.splitItemsInPack.splitItemsInPackRequest)

class splitItemsInPackResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SPLITITEMSINPACKRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.packageInfo.splitItemsInPack.splitItemsInPackResponse)

# @@protoc_insertion_point(module_scope)
