# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/hall/JoinGroup.proto',
  package='protoFile.hall.JoinGroup',
  serialized_pb='\n\x1eprotoFile/hall/JoinGroup.proto\x12\x18protoFile.hall.JoinGroup\"A\n\x10JoinGroupRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0f\n\x07groupId\x18\x02 \x02(\x05\x12\x10\n\x08password\x18\x03 \x02(\t\"4\n\x11JoinGroupResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t')




_JOINGROUPREQUEST = descriptor.Descriptor(
  name='JoinGroupRequest',
  full_name='protoFile.hall.JoinGroup.JoinGroupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.hall.JoinGroup.JoinGroupRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='groupId', full_name='protoFile.hall.JoinGroup.JoinGroupRequest.groupId', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='password', full_name='protoFile.hall.JoinGroup.JoinGroupRequest.password', index=2,
      number=3, type=9, cpp_type=9, label=2,
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
  serialized_start=60,
  serialized_end=125,
)


_JOINGROUPRESPONSE = descriptor.Descriptor(
  name='JoinGroupResponse',
  full_name='protoFile.hall.JoinGroup.JoinGroupResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.hall.JoinGroup.JoinGroupResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.hall.JoinGroup.JoinGroupResponse.message', index=1,
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
  serialized_start=127,
  serialized_end=179,
)

DESCRIPTOR.message_types_by_name['JoinGroupRequest'] = _JOINGROUPREQUEST
DESCRIPTOR.message_types_by_name['JoinGroupResponse'] = _JOINGROUPRESPONSE

class JoinGroupRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _JOINGROUPREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.hall.JoinGroup.JoinGroupRequest)

class JoinGroupResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _JOINGROUPRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.hall.JoinGroup.JoinGroupResponse)

# @@protoc_insertion_point(module_scope)
