# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/guild/TransferCorpsOrKickMember.proto',
  package='protoFile.guild.TransferCorpsOrKickMember',
  serialized_pb='\n/protoFile/guild/TransferCorpsOrKickMember.proto\x12)protoFile.guild.TransferCorpsOrKickMember\"R\n TransferCorpsOrKickMemberRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x10\n\x08operType\x18\x02 \x02(\x05\x12\x10\n\x08memberId\x18\x03 \x02(\x05\"D\n!TransferCorpsOrKickMemberResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t')




_TRANSFERCORPSORKICKMEMBERREQUEST = descriptor.Descriptor(
  name='TransferCorpsOrKickMemberRequest',
  full_name='protoFile.guild.TransferCorpsOrKickMember.TransferCorpsOrKickMemberRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.guild.TransferCorpsOrKickMember.TransferCorpsOrKickMemberRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='operType', full_name='protoFile.guild.TransferCorpsOrKickMember.TransferCorpsOrKickMemberRequest.operType', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='memberId', full_name='protoFile.guild.TransferCorpsOrKickMember.TransferCorpsOrKickMemberRequest.memberId', index=2,
      number=3, type=5, cpp_type=1, label=2,
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
  serialized_start=94,
  serialized_end=176,
)


_TRANSFERCORPSORKICKMEMBERRESPONSE = descriptor.Descriptor(
  name='TransferCorpsOrKickMemberResponse',
  full_name='protoFile.guild.TransferCorpsOrKickMember.TransferCorpsOrKickMemberResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.guild.TransferCorpsOrKickMember.TransferCorpsOrKickMemberResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.guild.TransferCorpsOrKickMember.TransferCorpsOrKickMemberResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=178,
  serialized_end=246,
)

DESCRIPTOR.message_types_by_name['TransferCorpsOrKickMemberRequest'] = _TRANSFERCORPSORKICKMEMBERREQUEST
DESCRIPTOR.message_types_by_name['TransferCorpsOrKickMemberResponse'] = _TRANSFERCORPSORKICKMEMBERRESPONSE

class TransferCorpsOrKickMemberRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRANSFERCORPSORKICKMEMBERREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.guild.TransferCorpsOrKickMember.TransferCorpsOrKickMemberRequest)

class TransferCorpsOrKickMemberResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRANSFERCORPSORKICKMEMBERRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.guild.TransferCorpsOrKickMember.TransferCorpsOrKickMemberResponse)

# @@protoc_insertion_point(module_scope)