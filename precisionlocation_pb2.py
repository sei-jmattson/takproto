# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: precisionlocation.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='precisionlocation.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('H\003'),
  serialized_pb=_b('\n\x17precisionlocation.proto\"8\n\x11PrecisionLocation\x12\x13\n\x0bgeopointsrc\x18\x01 \x01(\t\x12\x0e\n\x06\x61ltsrc\x18\x02 \x01(\tB\x02H\x03\x62\x06proto3')
)




_PRECISIONLOCATION = _descriptor.Descriptor(
  name='PrecisionLocation',
  full_name='PrecisionLocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='geopointsrc', full_name='PrecisionLocation.geopointsrc', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='altsrc', full_name='PrecisionLocation.altsrc', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=83,
)

DESCRIPTOR.message_types_by_name['PrecisionLocation'] = _PRECISIONLOCATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PrecisionLocation = _reflection.GeneratedProtocolMessageType('PrecisionLocation', (_message.Message,), dict(
  DESCRIPTOR = _PRECISIONLOCATION,
  __module__ = 'precisionlocation_pb2'
  # @@protoc_insertion_point(class_scope:PrecisionLocation)
  ))
_sym_db.RegisterMessage(PrecisionLocation)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)