# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import app.scense.protoFile.quest.TaskItemInfo_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/quest/TaskPlayerTaskListRequest1416.proto',
  package='protoFile.quest.TaskPlayerTaskListRequest1416',
  serialized_pb='\n3protoFile/quest/TaskPlayerTaskListRequest1416.proto\x12-protoFile.quest.TaskPlayerTaskListRequest1416\x1a\"protoFile/quest/TaskItemInfo.proto\"+\n\x1dTaskPlayerHaveTaskListRequest\x12\n\n\x02id\x18\x01 \x02(\x05\"o\n\x1eTaskPlayerHaveTaskListResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12,\n\x05tasks\x18\x02 \x03(\x0b\x32\x1d.protoFile.quest.TaskItemInfo\x12\x0f\n\x07message\x18\x03 \x01(\t')




_TASKPLAYERHAVETASKLISTREQUEST = descriptor.Descriptor(
  name='TaskPlayerHaveTaskListRequest',
  full_name='protoFile.quest.TaskPlayerTaskListRequest1416.TaskPlayerHaveTaskListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.quest.TaskPlayerTaskListRequest1416.TaskPlayerHaveTaskListRequest.id', index=0,
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
  serialized_start=138,
  serialized_end=181,
)


_TASKPLAYERHAVETASKLISTRESPONSE = descriptor.Descriptor(
  name='TaskPlayerHaveTaskListResponse',
  full_name='protoFile.quest.TaskPlayerTaskListRequest1416.TaskPlayerHaveTaskListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.quest.TaskPlayerTaskListRequest1416.TaskPlayerHaveTaskListResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='tasks', full_name='protoFile.quest.TaskPlayerTaskListRequest1416.TaskPlayerHaveTaskListResponse.tasks', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.quest.TaskPlayerTaskListRequest1416.TaskPlayerHaveTaskListResponse.message', index=2,
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
  serialized_start=183,
  serialized_end=294,
)

_TASKPLAYERHAVETASKLISTRESPONSE.fields_by_name['tasks'].message_type = app.scense.protoFile.quest.TaskItemInfo_pb2._TASKITEMINFO
DESCRIPTOR.message_types_by_name['TaskPlayerHaveTaskListRequest'] = _TASKPLAYERHAVETASKLISTREQUEST
DESCRIPTOR.message_types_by_name['TaskPlayerHaveTaskListResponse'] = _TASKPLAYERHAVETASKLISTRESPONSE

class TaskPlayerHaveTaskListRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TASKPLAYERHAVETASKLISTREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.quest.TaskPlayerTaskListRequest1416.TaskPlayerHaveTaskListRequest)

class TaskPlayerHaveTaskListResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TASKPLAYERHAVETASKLISTRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.quest.TaskPlayerTaskListRequest1416.TaskPlayerHaveTaskListResponse)

# @@protoc_insertion_point(module_scope)