# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='JoinBattle4407.proto',
  package='protoFile.campaign.JoinBattle4407',
  serialized_pb='\n\x14JoinBattle4407.proto\x12!protoFile.campaign.JoinBattle4407\"\x1f\n\x11JoinBattleRequest\x12\n\n\x02id\x18\x01 \x02(\x05\"5\n\x12JoinBattleResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\x08')




_JOINBATTLEREQUEST = descriptor.Descriptor(
  name='JoinBattleRequest',
  full_name='protoFile.campaign.JoinBattle4407.JoinBattleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.campaign.JoinBattle4407.JoinBattleRequest.id', index=0,
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
  serialized_start=59,
  serialized_end=90,
)


_JOINBATTLERESPONSE = descriptor.Descriptor(
  name='JoinBattleResponse',
  full_name='protoFile.campaign.JoinBattle4407.JoinBattleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.campaign.JoinBattle4407.JoinBattleResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.campaign.JoinBattle4407.JoinBattleResponse.result', index=1,
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
  serialized_start=92,
  serialized_end=145,
)

DESCRIPTOR.message_types_by_name['JoinBattleRequest'] = _JOINBATTLEREQUEST
DESCRIPTOR.message_types_by_name['JoinBattleResponse'] = _JOINBATTLERESPONSE

class JoinBattleRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _JOINBATTLEREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.campaign.JoinBattle4407.JoinBattleRequest)

class JoinBattleResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _JOINBATTLERESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.campaign.JoinBattle4407.JoinBattleResponse)

# @@protoc_insertion_point(module_scope)
