# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/hall/CheckMatrixCanUse1823.proto',
  package='protoFile.hall.CheckMatrixCanUse1823',
  serialized_pb='\n*protoFile/hall/CheckMatrixCanUse1823.proto\x12$protoFile.hall.CheckMatrixCanUse1823\"9\n\x18\x43heckMatrixCanUseRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x11\n\tvipMatrix\x18\x02 \x01(\x05\"<\n\x19\x43heckMatrixCanUseResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t')




_CHECKMATRIXCANUSEREQUEST = descriptor.Descriptor(
  name='CheckMatrixCanUseRequest',
  full_name='protoFile.hall.CheckMatrixCanUse1823.CheckMatrixCanUseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.hall.CheckMatrixCanUse1823.CheckMatrixCanUseRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='vipMatrix', full_name='protoFile.hall.CheckMatrixCanUse1823.CheckMatrixCanUseRequest.vipMatrix', index=1,
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
  serialized_start=84,
  serialized_end=141,
)


_CHECKMATRIXCANUSERESPONSE = descriptor.Descriptor(
  name='CheckMatrixCanUseResponse',
  full_name='protoFile.hall.CheckMatrixCanUse1823.CheckMatrixCanUseResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.hall.CheckMatrixCanUse1823.CheckMatrixCanUseResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.hall.CheckMatrixCanUse1823.CheckMatrixCanUseResponse.message', index=1,
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
  serialized_start=143,
  serialized_end=203,
)

DESCRIPTOR.message_types_by_name['CheckMatrixCanUseRequest'] = _CHECKMATRIXCANUSEREQUEST
DESCRIPTOR.message_types_by_name['CheckMatrixCanUseResponse'] = _CHECKMATRIXCANUSERESPONSE

class CheckMatrixCanUseRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHECKMATRIXCANUSEREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.hall.CheckMatrixCanUse1823.CheckMatrixCanUseRequest)

class CheckMatrixCanUseResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHECKMATRIXCANUSERESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.hall.CheckMatrixCanUse1823.CheckMatrixCanUseResponse)

# @@protoc_insertion_point(module_scope)
