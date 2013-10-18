# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='terminateLobbyOperation.proto',
  package='',
  serialized_pb='\n\x1dterminateLobbyOperation.proto\":\n\x1eterminateLobbyOperationRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0c\n\x04type\x18\x02 \x02(\x05\"]\n\x1fterminateLobbyOperationResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x19\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x0b.dataPacket\"*\n\ndataPacket\x12\r\n\x05\x62onus\x18\x01 \x01(\x05\x12\r\n\x05level\x18\x02 \x01(\x05')




_TERMINATELOBBYOPERATIONREQUEST = descriptor.Descriptor(
  name='terminateLobbyOperationRequest',
  full_name='terminateLobbyOperationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='terminateLobbyOperationRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='terminateLobbyOperationRequest.type', index=1,
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
  serialized_start=33,
  serialized_end=91,
)


_TERMINATELOBBYOPERATIONRESPONSE = descriptor.Descriptor(
  name='terminateLobbyOperationResponse',
  full_name='terminateLobbyOperationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='terminateLobbyOperationResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='terminateLobbyOperationResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='terminateLobbyOperationResponse.data', index=2,
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
  serialized_start=93,
  serialized_end=186,
)


_DATAPACKET = descriptor.Descriptor(
  name='dataPacket',
  full_name='dataPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='bonus', full_name='dataPacket.bonus', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='level', full_name='dataPacket.level', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=188,
  serialized_end=230,
)


_TERMINATELOBBYOPERATIONRESPONSE.fields_by_name['data'].message_type = _DATAPACKET

class terminateLobbyOperationRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TERMINATELOBBYOPERATIONREQUEST
  
  # @@protoc_insertion_point(class_scope:terminateLobbyOperationRequest)

class terminateLobbyOperationResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TERMINATELOBBYOPERATIONRESPONSE
  
  # @@protoc_insertion_point(class_scope:terminateLobbyOperationResponse)

class dataPacket(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DATAPACKET
  
  # @@protoc_insertion_point(class_scope:dataPacket)

# @@protoc_insertion_point(module_scope)
