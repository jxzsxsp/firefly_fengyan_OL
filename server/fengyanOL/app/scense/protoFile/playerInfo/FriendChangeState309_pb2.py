# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/playerInfo/FriendChangeState309.proto',
  package='protoFile.playerInfo.FriendChangeState309',
  serialized_pb='\n/protoFile/playerInfo/FriendChangeState309.proto\x12)protoFile.playerInfo.FriendChangeState309\"7\n\x18\x46riendChangeStateRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0f\n\x07\x63ontent\x18\x02 \x02(\t\"M\n\x19\x46riendChangeStateResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07\x63ontent\x18\x02 \x02(\t\x12\x0f\n\x07message\x18\x03 \x01(\t')




_FRIENDCHANGESTATEREQUEST = descriptor.Descriptor(
  name='FriendChangeStateRequest',
  full_name='protoFile.playerInfo.FriendChangeState309.FriendChangeStateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.playerInfo.FriendChangeState309.FriendChangeStateRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='content', full_name='protoFile.playerInfo.FriendChangeState309.FriendChangeStateRequest.content', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=94,
  serialized_end=149,
)


_FRIENDCHANGESTATERESPONSE = descriptor.Descriptor(
  name='FriendChangeStateResponse',
  full_name='protoFile.playerInfo.FriendChangeState309.FriendChangeStateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.playerInfo.FriendChangeState309.FriendChangeStateResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='content', full_name='protoFile.playerInfo.FriendChangeState309.FriendChangeStateResponse.content', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.playerInfo.FriendChangeState309.FriendChangeStateResponse.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=151,
  serialized_end=228,
)

DESCRIPTOR.message_types_by_name['FriendChangeStateRequest'] = _FRIENDCHANGESTATEREQUEST
DESCRIPTOR.message_types_by_name['FriendChangeStateResponse'] = _FRIENDCHANGESTATERESPONSE

class FriendChangeStateRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FRIENDCHANGESTATEREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.playerInfo.FriendChangeState309.FriendChangeStateRequest)

class FriendChangeStateResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FRIENDCHANGESTATERESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.playerInfo.FriendChangeState309.FriendChangeStateResponse)

# @@protoc_insertion_point(module_scope)