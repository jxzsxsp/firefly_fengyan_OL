# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/guild/CorpsTechnologyDonate.proto',
  package='protoFile.guild.CorpsTechnologyDonate',
  serialized_pb='\n+protoFile/guild/CorpsTechnologyDonate.proto\x12%protoFile.guild.CorpsTechnologyDonate\"S\n\x1c\x43orpsTechnologyDonateRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x11\n\tdonateNum\x18\x02 \x02(\x05\x12\x14\n\x0ctechnologyId\x18\x03 \x02(\x05\"@\n\x1d\x43orpsTechnologyDonateResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t')




_CORPSTECHNOLOGYDONATEREQUEST = descriptor.Descriptor(
  name='CorpsTechnologyDonateRequest',
  full_name='protoFile.guild.CorpsTechnologyDonate.CorpsTechnologyDonateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.guild.CorpsTechnologyDonate.CorpsTechnologyDonateRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='donateNum', full_name='protoFile.guild.CorpsTechnologyDonate.CorpsTechnologyDonateRequest.donateNum', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='technologyId', full_name='protoFile.guild.CorpsTechnologyDonate.CorpsTechnologyDonateRequest.technologyId', index=2,
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
  serialized_start=86,
  serialized_end=169,
)


_CORPSTECHNOLOGYDONATERESPONSE = descriptor.Descriptor(
  name='CorpsTechnologyDonateResponse',
  full_name='protoFile.guild.CorpsTechnologyDonate.CorpsTechnologyDonateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.guild.CorpsTechnologyDonate.CorpsTechnologyDonateResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.guild.CorpsTechnologyDonate.CorpsTechnologyDonateResponse.message', index=1,
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
  serialized_start=171,
  serialized_end=235,
)

DESCRIPTOR.message_types_by_name['CorpsTechnologyDonateRequest'] = _CORPSTECHNOLOGYDONATEREQUEST
DESCRIPTOR.message_types_by_name['CorpsTechnologyDonateResponse'] = _CORPSTECHNOLOGYDONATERESPONSE

class CorpsTechnologyDonateRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CORPSTECHNOLOGYDONATEREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.guild.CorpsTechnologyDonate.CorpsTechnologyDonateRequest)

class CorpsTechnologyDonateResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CORPSTECHNOLOGYDONATERESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.guild.CorpsTechnologyDonate.CorpsTechnologyDonateResponse)

# @@protoc_insertion_point(module_scope)
