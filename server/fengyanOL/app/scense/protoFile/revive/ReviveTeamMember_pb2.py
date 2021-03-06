# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/revive/ReviveTeamMember.proto',
  package='protoFile.revive.ReviveTeamMember',
  serialized_pb='\n\'protoFile/revive/ReviveTeamMember.proto\x12!protoFile.revive.ReviveTeamMember\"J\n\x17ReviveTeamMemberRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x12\n\nvictimerId\x18\x02 \x02(\x05\x12\x0f\n\x07paytype\x18\x03 \x02(\x05\"z\n\x18ReviveTeamMemberResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12=\n\x04\x64\x61ta\x18\x03 \x02(\x0b\x32/.protoFile.revive.ReviveTeamMember.ResponseData\"4\n\x0cResponseData\x12\x11\n\tfaildtype\x18\x01 \x02(\x05\x12\x11\n\tgoldprice\x18\x02 \x01(\x05')




_REVIVETEAMMEMBERREQUEST = descriptor.Descriptor(
  name='ReviveTeamMemberRequest',
  full_name='protoFile.revive.ReviveTeamMember.ReviveTeamMemberRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.revive.ReviveTeamMember.ReviveTeamMemberRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='victimerId', full_name='protoFile.revive.ReviveTeamMember.ReviveTeamMemberRequest.victimerId', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='paytype', full_name='protoFile.revive.ReviveTeamMember.ReviveTeamMemberRequest.paytype', index=2,
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
  serialized_start=78,
  serialized_end=152,
)


_REVIVETEAMMEMBERRESPONSE = descriptor.Descriptor(
  name='ReviveTeamMemberResponse',
  full_name='protoFile.revive.ReviveTeamMember.ReviveTeamMemberResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.revive.ReviveTeamMember.ReviveTeamMemberResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.revive.ReviveTeamMember.ReviveTeamMemberResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='protoFile.revive.ReviveTeamMember.ReviveTeamMemberResponse.data', index=2,
      number=3, type=11, cpp_type=10, label=2,
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
  serialized_start=154,
  serialized_end=276,
)


_RESPONSEDATA = descriptor.Descriptor(
  name='ResponseData',
  full_name='protoFile.revive.ReviveTeamMember.ResponseData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='faildtype', full_name='protoFile.revive.ReviveTeamMember.ResponseData.faildtype', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='goldprice', full_name='protoFile.revive.ReviveTeamMember.ResponseData.goldprice', index=1,
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
  serialized_start=278,
  serialized_end=330,
)

_REVIVETEAMMEMBERRESPONSE.fields_by_name['data'].message_type = _RESPONSEDATA
DESCRIPTOR.message_types_by_name['ReviveTeamMemberRequest'] = _REVIVETEAMMEMBERREQUEST
DESCRIPTOR.message_types_by_name['ReviveTeamMemberResponse'] = _REVIVETEAMMEMBERRESPONSE
DESCRIPTOR.message_types_by_name['ResponseData'] = _RESPONSEDATA

class ReviveTeamMemberRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REVIVETEAMMEMBERREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.revive.ReviveTeamMember.ReviveTeamMemberRequest)

class ReviveTeamMemberResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REVIVETEAMMEMBERRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.revive.ReviveTeamMember.ReviveTeamMemberResponse)

class ResponseData(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESPONSEDATA
  
  # @@protoc_insertion_point(class_scope:protoFile.revive.ReviveTeamMember.ResponseData)

# @@protoc_insertion_point(module_scope)
