# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/pet/ModifyPetName2303.proto',
  package='protoFile.pet.ModifyPetName2303',
  serialized_pb='\n%protoFile/pet/ModifyPetName2303.proto\x12\x1fprotoFile.pet.ModifyPetName2303\"B\n\x14ModifyPetNameRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05petId\x18\x02 \x02(\x05\x12\x0f\n\x07petName\x18\x03 \x02(\t\"8\n\x15ModifyPetNameResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t')




_MODIFYPETNAMEREQUEST = descriptor.Descriptor(
  name='ModifyPetNameRequest',
  full_name='protoFile.pet.ModifyPetName2303.ModifyPetNameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.pet.ModifyPetName2303.ModifyPetNameRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='petId', full_name='protoFile.pet.ModifyPetName2303.ModifyPetNameRequest.petId', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='petName', full_name='protoFile.pet.ModifyPetName2303.ModifyPetNameRequest.petName', index=2,
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
  serialized_start=74,
  serialized_end=140,
)


_MODIFYPETNAMERESPONSE = descriptor.Descriptor(
  name='ModifyPetNameResponse',
  full_name='protoFile.pet.ModifyPetName2303.ModifyPetNameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.pet.ModifyPetName2303.ModifyPetNameResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.pet.ModifyPetName2303.ModifyPetNameResponse.message', index=1,
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
  serialized_start=142,
  serialized_end=198,
)

DESCRIPTOR.message_types_by_name['ModifyPetNameRequest'] = _MODIFYPETNAMEREQUEST
DESCRIPTOR.message_types_by_name['ModifyPetNameResponse'] = _MODIFYPETNAMERESPONSE

class ModifyPetNameRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MODIFYPETNAMEREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.pet.ModifyPetName2303.ModifyPetNameRequest)

class ModifyPetNameResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MODIFYPETNAMERESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.pet.ModifyPetName2303.ModifyPetNameResponse)

# @@protoc_insertion_point(module_scope)
