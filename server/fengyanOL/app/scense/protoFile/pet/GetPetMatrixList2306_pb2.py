# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/pet/GetPetMatrixList2306.proto',
  package='protoFile.pet.GetPetMatrixList2306',
  serialized_pb='\n(protoFile/pet/GetPetMatrixList2306.proto\x12\"protoFile.pet.GetPetMatrixList2306\"%\n\x17GetPetMatrixListRequest\x12\n\n\x02id\x18\x01 \x02(\x05\"\x7f\n\x18GetPetMatrixListResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x42\n\nmatrixInfo\x18\x03 \x01(\x0b\x32..protoFile.pet.GetPetMatrixList2306.MatrixInfo\"\x89\x01\n\nMatrixInfo\x12\r\n\x05jwDes\x18\x01 \x01(\t\x12\x0e\n\x06\x63urNum\x18\x02 \x01(\x05\x12\x0e\n\x06maxNum\x18\x03 \x01(\x05\x12L\n\x0fmatrixTitleInfo\x18\x04 \x03(\x0b\x32\x33.protoFile.pet.GetPetMatrixList2306.MatrixTitleInfo\"^\n\x0fMatrixTitleInfo\x12\x10\n\x08titlePos\x18\x01 \x01(\x05\x12\x0e\n\x06hasPet\x18\x02 \x01(\x08\x12\r\n\x05petId\x18\x03 \x01(\x05\x12\x0c\n\x04type\x18\x04 \x01(\x05\x12\x0c\n\x04icon\x18\x05 \x01(\x05')




_GETPETMATRIXLISTREQUEST = descriptor.Descriptor(
  name='GetPetMatrixListRequest',
  full_name='protoFile.pet.GetPetMatrixList2306.GetPetMatrixListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.pet.GetPetMatrixList2306.GetPetMatrixListRequest.id', index=0,
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
  serialized_start=80,
  serialized_end=117,
)


_GETPETMATRIXLISTRESPONSE = descriptor.Descriptor(
  name='GetPetMatrixListResponse',
  full_name='protoFile.pet.GetPetMatrixList2306.GetPetMatrixListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.pet.GetPetMatrixList2306.GetPetMatrixListResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.pet.GetPetMatrixList2306.GetPetMatrixListResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='matrixInfo', full_name='protoFile.pet.GetPetMatrixList2306.GetPetMatrixListResponse.matrixInfo', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=119,
  serialized_end=246,
)


_MATRIXINFO = descriptor.Descriptor(
  name='MatrixInfo',
  full_name='protoFile.pet.GetPetMatrixList2306.MatrixInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='jwDes', full_name='protoFile.pet.GetPetMatrixList2306.MatrixInfo.jwDes', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='curNum', full_name='protoFile.pet.GetPetMatrixList2306.MatrixInfo.curNum', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='maxNum', full_name='protoFile.pet.GetPetMatrixList2306.MatrixInfo.maxNum', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='matrixTitleInfo', full_name='protoFile.pet.GetPetMatrixList2306.MatrixInfo.matrixTitleInfo', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=249,
  serialized_end=386,
)


_MATRIXTITLEINFO = descriptor.Descriptor(
  name='MatrixTitleInfo',
  full_name='protoFile.pet.GetPetMatrixList2306.MatrixTitleInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='titlePos', full_name='protoFile.pet.GetPetMatrixList2306.MatrixTitleInfo.titlePos', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hasPet', full_name='protoFile.pet.GetPetMatrixList2306.MatrixTitleInfo.hasPet', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='petId', full_name='protoFile.pet.GetPetMatrixList2306.MatrixTitleInfo.petId', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='protoFile.pet.GetPetMatrixList2306.MatrixTitleInfo.type', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='icon', full_name='protoFile.pet.GetPetMatrixList2306.MatrixTitleInfo.icon', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=388,
  serialized_end=482,
)

_GETPETMATRIXLISTRESPONSE.fields_by_name['matrixInfo'].message_type = _MATRIXINFO
_MATRIXINFO.fields_by_name['matrixTitleInfo'].message_type = _MATRIXTITLEINFO
DESCRIPTOR.message_types_by_name['GetPetMatrixListRequest'] = _GETPETMATRIXLISTREQUEST
DESCRIPTOR.message_types_by_name['GetPetMatrixListResponse'] = _GETPETMATRIXLISTRESPONSE
DESCRIPTOR.message_types_by_name['MatrixInfo'] = _MATRIXINFO
DESCRIPTOR.message_types_by_name['MatrixTitleInfo'] = _MATRIXTITLEINFO

class GetPetMatrixListRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETPETMATRIXLISTREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.pet.GetPetMatrixList2306.GetPetMatrixListRequest)

class GetPetMatrixListResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETPETMATRIXLISTRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.pet.GetPetMatrixList2306.GetPetMatrixListResponse)

class MatrixInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MATRIXINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.pet.GetPetMatrixList2306.MatrixInfo)

class MatrixTitleInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MATRIXTITLEINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.pet.GetPetMatrixList2306.MatrixTitleInfo)

# @@protoc_insertion_point(module_scope)
