# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/map/MapMessage.proto',
  package='protoFile.map.MapMessage',
  serialized_pb='\n\x1eprotoFile/map/MapMessage.proto\x12\x18protoFile.map.MapMessage\"n\n\x0cSceneMapInfo\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05\x63olor\x18\x02 \x02(\x05\x12\x0b\n\x03tax\x18\x03 \x02(\x05\x12\x0e\n\x06income\x18\x04 \x02(\x05\x12\x12\n\nscene_name\x18\x05 \x02(\t\x12\x12\n\nunion_name\x18\x06 \x01(\t\"u\n\x0fInstanceMapInfo\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05\x63olor\x18\x02 \x02(\x05\x12\x0c\n\x04once\x18\x03 \x02(\x05\x12\x0e\n\x06income\x18\x04 \x02(\x05\x12\x15\n\rinstance_name\x18\x05 \x02(\t\x12\x12\n\nunion_name\x18\x06 \x01(\t\"\"\n\x14SceneMapInfosRequest\x12\n\n\x02id\x18\x01 \x02(\x05\"\x83\x01\n\x15SceneMapInfosResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x12\n\nself_color\x18\x02 \x02(\x05\x12\x35\n\x05infos\x18\x03 \x03(\x0b\x32&.protoFile.map.MapMessage.SceneMapInfo\x12\x0f\n\x07message\x18\x04 \x01(\t\"%\n\x17InstanceMapInfosRequest\x12\n\n\x02id\x18\x01 \x02(\x05\"\x89\x01\n\x18InstanceMapInfosResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x12\n\nself_color\x18\x02 \x02(\x05\x12\x38\n\x05infos\x18\x03 \x03(\x0b\x32).protoFile.map.MapMessage.InstanceMapInfo\x12\x0f\n\x07message\x18\x04 \x01(\t\"4\n\x17\x43hangeUnionColorRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05\x63olor\x18\x02 \x02(\x05\"J\n\x18\x43hangeUnionColorResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\r\n\x05\x63olor\x18\x02 \x02(\x05\x12\x0f\n\x07message\x18\x03 \x01(\t')




_SCENEMAPINFO = descriptor.Descriptor(
  name='SceneMapInfo',
  full_name='protoFile.map.MapMessage.SceneMapInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.map.MapMessage.SceneMapInfo.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='color', full_name='protoFile.map.MapMessage.SceneMapInfo.color', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='tax', full_name='protoFile.map.MapMessage.SceneMapInfo.tax', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='income', full_name='protoFile.map.MapMessage.SceneMapInfo.income', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='scene_name', full_name='protoFile.map.MapMessage.SceneMapInfo.scene_name', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='union_name', full_name='protoFile.map.MapMessage.SceneMapInfo.union_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_end=170,
)


_INSTANCEMAPINFO = descriptor.Descriptor(
  name='InstanceMapInfo',
  full_name='protoFile.map.MapMessage.InstanceMapInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.map.MapMessage.InstanceMapInfo.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='color', full_name='protoFile.map.MapMessage.InstanceMapInfo.color', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='once', full_name='protoFile.map.MapMessage.InstanceMapInfo.once', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='income', full_name='protoFile.map.MapMessage.InstanceMapInfo.income', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='instance_name', full_name='protoFile.map.MapMessage.InstanceMapInfo.instance_name', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='union_name', full_name='protoFile.map.MapMessage.InstanceMapInfo.union_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=172,
  serialized_end=289,
)


_SCENEMAPINFOSREQUEST = descriptor.Descriptor(
  name='SceneMapInfosRequest',
  full_name='protoFile.map.MapMessage.SceneMapInfosRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.map.MapMessage.SceneMapInfosRequest.id', index=0,
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
  serialized_start=291,
  serialized_end=325,
)


_SCENEMAPINFOSRESPONSE = descriptor.Descriptor(
  name='SceneMapInfosResponse',
  full_name='protoFile.map.MapMessage.SceneMapInfosResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.map.MapMessage.SceneMapInfosResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='self_color', full_name='protoFile.map.MapMessage.SceneMapInfosResponse.self_color', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='infos', full_name='protoFile.map.MapMessage.SceneMapInfosResponse.infos', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.map.MapMessage.SceneMapInfosResponse.message', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=328,
  serialized_end=459,
)


_INSTANCEMAPINFOSREQUEST = descriptor.Descriptor(
  name='InstanceMapInfosRequest',
  full_name='protoFile.map.MapMessage.InstanceMapInfosRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.map.MapMessage.InstanceMapInfosRequest.id', index=0,
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
  serialized_start=461,
  serialized_end=498,
)


_INSTANCEMAPINFOSRESPONSE = descriptor.Descriptor(
  name='InstanceMapInfosResponse',
  full_name='protoFile.map.MapMessage.InstanceMapInfosResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.map.MapMessage.InstanceMapInfosResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='self_color', full_name='protoFile.map.MapMessage.InstanceMapInfosResponse.self_color', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='infos', full_name='protoFile.map.MapMessage.InstanceMapInfosResponse.infos', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.map.MapMessage.InstanceMapInfosResponse.message', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=501,
  serialized_end=638,
)


_CHANGEUNIONCOLORREQUEST = descriptor.Descriptor(
  name='ChangeUnionColorRequest',
  full_name='protoFile.map.MapMessage.ChangeUnionColorRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.map.MapMessage.ChangeUnionColorRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='color', full_name='protoFile.map.MapMessage.ChangeUnionColorRequest.color', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=640,
  serialized_end=692,
)


_CHANGEUNIONCOLORRESPONSE = descriptor.Descriptor(
  name='ChangeUnionColorResponse',
  full_name='protoFile.map.MapMessage.ChangeUnionColorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.map.MapMessage.ChangeUnionColorResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='color', full_name='protoFile.map.MapMessage.ChangeUnionColorResponse.color', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.map.MapMessage.ChangeUnionColorResponse.message', index=2,
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
  serialized_start=694,
  serialized_end=768,
)

_SCENEMAPINFOSRESPONSE.fields_by_name['infos'].message_type = _SCENEMAPINFO
_INSTANCEMAPINFOSRESPONSE.fields_by_name['infos'].message_type = _INSTANCEMAPINFO
DESCRIPTOR.message_types_by_name['SceneMapInfo'] = _SCENEMAPINFO
DESCRIPTOR.message_types_by_name['InstanceMapInfo'] = _INSTANCEMAPINFO
DESCRIPTOR.message_types_by_name['SceneMapInfosRequest'] = _SCENEMAPINFOSREQUEST
DESCRIPTOR.message_types_by_name['SceneMapInfosResponse'] = _SCENEMAPINFOSRESPONSE
DESCRIPTOR.message_types_by_name['InstanceMapInfosRequest'] = _INSTANCEMAPINFOSREQUEST
DESCRIPTOR.message_types_by_name['InstanceMapInfosResponse'] = _INSTANCEMAPINFOSRESPONSE
DESCRIPTOR.message_types_by_name['ChangeUnionColorRequest'] = _CHANGEUNIONCOLORREQUEST
DESCRIPTOR.message_types_by_name['ChangeUnionColorResponse'] = _CHANGEUNIONCOLORRESPONSE

class SceneMapInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SCENEMAPINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.map.MapMessage.SceneMapInfo)

class InstanceMapInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INSTANCEMAPINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.map.MapMessage.InstanceMapInfo)

class SceneMapInfosRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SCENEMAPINFOSREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.map.MapMessage.SceneMapInfosRequest)

class SceneMapInfosResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SCENEMAPINFOSRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.map.MapMessage.SceneMapInfosResponse)

class InstanceMapInfosRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INSTANCEMAPINFOSREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.map.MapMessage.InstanceMapInfosRequest)

class InstanceMapInfosResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INSTANCEMAPINFOSRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.map.MapMessage.InstanceMapInfosResponse)

class ChangeUnionColorRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHANGEUNIONCOLORREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.map.MapMessage.ChangeUnionColorRequest)

class ChangeUnionColorResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHANGEUNIONCOLORRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.map.MapMessage.ChangeUnionColorResponse)

# @@protoc_insertion_point(module_scope)
