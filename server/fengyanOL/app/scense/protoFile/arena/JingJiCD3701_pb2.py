# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/arena/JingJiCD3701.proto',
  package='protoFile.arena.JingJiCD3701',
  serialized_pb='\n\"protoFile/arena/JingJiCD3701.proto\x12\x1cprotoFile.arena.JingJiCD3701\"\"\n\x10JingJiCDResponse\x12\x0e\n\x06\x63\x64Time\x18\x01 \x01(\x05')




_JINGJICDRESPONSE = descriptor.Descriptor(
  name='JingJiCDResponse',
  full_name='protoFile.arena.JingJiCD3701.JingJiCDResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='cdTime', full_name='protoFile.arena.JingJiCD3701.JingJiCDResponse.cdTime', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=68,
  serialized_end=102,
)

DESCRIPTOR.message_types_by_name['JingJiCDResponse'] = _JINGJICDRESPONSE

class JingJiCDResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _JINGJICDRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.arena.JingJiCD3701.JingJiCDResponse)

# @@protoc_insertion_point(module_scope)
