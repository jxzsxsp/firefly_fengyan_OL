# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/friend/addReport.proto',
  package='protoFile.friend.addReport',
  serialized_pb='\n protoFile/friend/addReport.proto\x12\x1aprotoFile.friend.addReport\"?\n\x10getReportRequest\x12\x0b\n\x03\x63id\x18\x01 \x02(\x05\x12\r\n\x05tocid\x18\x02 \x02(\x05\x12\x0f\n\x07\x63ontext\x18\x03 \x01(\t\"B\n\x11getReportResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x05')




_GETREPORTREQUEST = descriptor.Descriptor(
  name='getReportRequest',
  full_name='protoFile.friend.addReport.getReportRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='cid', full_name='protoFile.friend.addReport.getReportRequest.cid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='tocid', full_name='protoFile.friend.addReport.getReportRequest.tocid', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='context', full_name='protoFile.friend.addReport.getReportRequest.context', index=2,
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
  serialized_start=64,
  serialized_end=127,
)


_GETREPORTRESPONSE = descriptor.Descriptor(
  name='getReportResponse',
  full_name='protoFile.friend.addReport.getReportResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.friend.addReport.getReportResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.friend.addReport.getReportResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='protoFile.friend.addReport.getReportResponse.data', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=129,
  serialized_end=195,
)

DESCRIPTOR.message_types_by_name['getReportRequest'] = _GETREPORTREQUEST
DESCRIPTOR.message_types_by_name['getReportResponse'] = _GETREPORTRESPONSE

class getReportRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETREPORTREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.friend.addReport.getReportRequest)

class getReportResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETREPORTRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.friend.addReport.getReportResponse)

# @@protoc_insertion_point(module_scope)
