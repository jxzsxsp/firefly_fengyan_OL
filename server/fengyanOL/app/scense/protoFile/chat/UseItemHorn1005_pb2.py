# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/chat/UseItemHorn1005.proto',
  package='protoFile.chat.UseItemHorn1005',
  serialized_pb='\n$protoFile/chat/UseItemHorn1005.proto\x12\x1eprotoFile.chat.UseItemHorn1005\"]\n\x12UseItemHornRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0e\n\x06itemId\x18\x02 \x02(\x05\x12\x16\n\x0eitemTemplateId\x18\x03 \x02(\x05\x12\x13\n\x0bhornContent\x18\x04 \x02(\t\"6\n\x13UseItemHornResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t')




_USEITEMHORNREQUEST = descriptor.Descriptor(
  name='UseItemHornRequest',
  full_name='protoFile.chat.UseItemHorn1005.UseItemHornRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.chat.UseItemHorn1005.UseItemHornRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='itemId', full_name='protoFile.chat.UseItemHorn1005.UseItemHornRequest.itemId', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='itemTemplateId', full_name='protoFile.chat.UseItemHorn1005.UseItemHornRequest.itemTemplateId', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hornContent', full_name='protoFile.chat.UseItemHorn1005.UseItemHornRequest.hornContent', index=3,
      number=4, type=9, cpp_type=9, label=2,
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
  serialized_start=72,
  serialized_end=165,
)


_USEITEMHORNRESPONSE = descriptor.Descriptor(
  name='UseItemHornResponse',
  full_name='protoFile.chat.UseItemHorn1005.UseItemHornResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.chat.UseItemHorn1005.UseItemHornResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.chat.UseItemHorn1005.UseItemHornResponse.message', index=1,
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
  serialized_start=167,
  serialized_end=221,
)

DESCRIPTOR.message_types_by_name['UseItemHornRequest'] = _USEITEMHORNREQUEST
DESCRIPTOR.message_types_by_name['UseItemHornResponse'] = _USEITEMHORNRESPONSE

class UseItemHornRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _USEITEMHORNREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.chat.UseItemHorn1005.UseItemHornRequest)

class UseItemHornResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _USEITEMHORNRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.chat.UseItemHorn1005.UseItemHornResponse)

# @@protoc_insertion_point(module_scope)
