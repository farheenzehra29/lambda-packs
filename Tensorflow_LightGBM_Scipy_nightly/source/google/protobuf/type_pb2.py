# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import source_context_pb2 as google_dot_protobuf_dot_source__context__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/protobuf/type.proto',
  package='google.protobuf',
  syntax='proto3',
  serialized_options=_b('\n\023com.google.protobufB\tTypeProtoP\001Z/google.golang.org/genproto/protobuf/ptype;ptype\370\001\001\242\002\003GPB\252\002\036Google.Protobuf.WellKnownTypes'),
  serialized_pb=_b('\n\x1agoogle/protobuf/type.proto\x12\x0fgoogle.protobuf\x1a\x19google/protobuf/any.proto\x1a$google/protobuf/source_context.proto\"\xd7\x01\n\x04Type\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\x06\x66ields\x18\x02 \x03(\x0b\x32\x16.google.protobuf.Field\x12\x0e\n\x06oneofs\x18\x03 \x03(\t\x12(\n\x07options\x18\x04 \x03(\x0b\x32\x17.google.protobuf.Option\x12\x36\n\x0esource_context\x18\x05 \x01(\x0b\x32\x1e.google.protobuf.SourceContext\x12\'\n\x06syntax\x18\x06 \x01(\x0e\x32\x17.google.protobuf.Syntax\"\xd5\x05\n\x05\x46ield\x12)\n\x04kind\x18\x01 \x01(\x0e\x32\x1b.google.protobuf.Field.Kind\x12\x37\n\x0b\x63\x61rdinality\x18\x02 \x01(\x0e\x32\".google.protobuf.Field.Cardinality\x12\x0e\n\x06number\x18\x03 \x01(\x05\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x10\n\x08type_url\x18\x06 \x01(\t\x12\x13\n\x0boneof_index\x18\x07 \x01(\x05\x12\x0e\n\x06packed\x18\x08 \x01(\x08\x12(\n\x07options\x18\t \x03(\x0b\x32\x17.google.protobuf.Option\x12\x11\n\tjson_name\x18\n \x01(\t\x12\x15\n\rdefault_value\x18\x0b \x01(\t\"\xc8\x02\n\x04Kind\x12\x10\n\x0cTYPE_UNKNOWN\x10\x00\x12\x0f\n\x0bTYPE_DOUBLE\x10\x01\x12\x0e\n\nTYPE_FLOAT\x10\x02\x12\x0e\n\nTYPE_INT64\x10\x03\x12\x0f\n\x0bTYPE_UINT64\x10\x04\x12\x0e\n\nTYPE_INT32\x10\x05\x12\x10\n\x0cTYPE_FIXED64\x10\x06\x12\x10\n\x0cTYPE_FIXED32\x10\x07\x12\r\n\tTYPE_BOOL\x10\x08\x12\x0f\n\x0bTYPE_STRING\x10\t\x12\x0e\n\nTYPE_GROUP\x10\n\x12\x10\n\x0cTYPE_MESSAGE\x10\x0b\x12\x0e\n\nTYPE_BYTES\x10\x0c\x12\x0f\n\x0bTYPE_UINT32\x10\r\x12\r\n\tTYPE_ENUM\x10\x0e\x12\x11\n\rTYPE_SFIXED32\x10\x0f\x12\x11\n\rTYPE_SFIXED64\x10\x10\x12\x0f\n\x0bTYPE_SINT32\x10\x11\x12\x0f\n\x0bTYPE_SINT64\x10\x12\"t\n\x0b\x43\x61rdinality\x12\x17\n\x13\x43\x41RDINALITY_UNKNOWN\x10\x00\x12\x18\n\x14\x43\x41RDINALITY_OPTIONAL\x10\x01\x12\x18\n\x14\x43\x41RDINALITY_REQUIRED\x10\x02\x12\x18\n\x14\x43\x41RDINALITY_REPEATED\x10\x03\"\xce\x01\n\x04\x45num\x12\x0c\n\x04name\x18\x01 \x01(\t\x12-\n\tenumvalue\x18\x02 \x03(\x0b\x32\x1a.google.protobuf.EnumValue\x12(\n\x07options\x18\x03 \x03(\x0b\x32\x17.google.protobuf.Option\x12\x36\n\x0esource_context\x18\x04 \x01(\x0b\x32\x1e.google.protobuf.SourceContext\x12\'\n\x06syntax\x18\x05 \x01(\x0e\x32\x17.google.protobuf.Syntax\"S\n\tEnumValue\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06number\x18\x02 \x01(\x05\x12(\n\x07options\x18\x03 \x03(\x0b\x32\x17.google.protobuf.Option\";\n\x06Option\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any*.\n\x06Syntax\x12\x11\n\rSYNTAX_PROTO2\x10\x00\x12\x11\n\rSYNTAX_PROTO3\x10\x01\x42}\n\x13\x63om.google.protobufB\tTypeProtoP\x01Z/google.golang.org/genproto/protobuf/ptype;ptype\xf8\x01\x01\xa2\x02\x03GPB\xaa\x02\x1eGoogle.Protobuf.WellKnownTypesb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_protobuf_dot_source__context__pb2.DESCRIPTOR,])

_SYNTAX = _descriptor.EnumDescriptor(
  name='Syntax',
  full_name='google.protobuf.Syntax',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SYNTAX_PROTO2', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYNTAX_PROTO3', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1413,
  serialized_end=1459,
)
_sym_db.RegisterEnumDescriptor(_SYNTAX)

Syntax = enum_type_wrapper.EnumTypeWrapper(_SYNTAX)
SYNTAX_PROTO2 = 0
SYNTAX_PROTO3 = 1


_FIELD_KIND = _descriptor.EnumDescriptor(
  name='Kind',
  full_name='google.protobuf.Field.Kind',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPE_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_DOUBLE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_FLOAT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_INT64', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_UINT64', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_INT32', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_FIXED64', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_FIXED32', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_BOOL', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_STRING', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_GROUP', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_MESSAGE', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_BYTES', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_UINT32', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_ENUM', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_SFIXED32', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_SFIXED64', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_SINT32', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_SINT64', index=18, number=18,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=610,
  serialized_end=938,
)
_sym_db.RegisterEnumDescriptor(_FIELD_KIND)

_FIELD_CARDINALITY = _descriptor.EnumDescriptor(
  name='Cardinality',
  full_name='google.protobuf.Field.Cardinality',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CARDINALITY_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CARDINALITY_OPTIONAL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CARDINALITY_REQUIRED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CARDINALITY_REPEATED', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=940,
  serialized_end=1056,
)
_sym_db.RegisterEnumDescriptor(_FIELD_CARDINALITY)


_TYPE = _descriptor.Descriptor(
  name='Type',
  full_name='google.protobuf.Type',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.protobuf.Type.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fields', full_name='google.protobuf.Type.fields', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oneofs', full_name='google.protobuf.Type.oneofs', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='google.protobuf.Type.options', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_context', full_name='google.protobuf.Type.source_context', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='syntax', full_name='google.protobuf.Type.syntax', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=113,
  serialized_end=328,
)


_FIELD = _descriptor.Descriptor(
  name='Field',
  full_name='google.protobuf.Field',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='kind', full_name='google.protobuf.Field.kind', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cardinality', full_name='google.protobuf.Field.cardinality', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='number', full_name='google.protobuf.Field.number', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.protobuf.Field.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type_url', full_name='google.protobuf.Field.type_url', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oneof_index', full_name='google.protobuf.Field.oneof_index', index=5,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packed', full_name='google.protobuf.Field.packed', index=6,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='google.protobuf.Field.options', index=7,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='json_name', full_name='google.protobuf.Field.json_name', index=8,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default_value', full_name='google.protobuf.Field.default_value', index=9,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FIELD_KIND,
    _FIELD_CARDINALITY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=331,
  serialized_end=1056,
)


_ENUM = _descriptor.Descriptor(
  name='Enum',
  full_name='google.protobuf.Enum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.protobuf.Enum.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enumvalue', full_name='google.protobuf.Enum.enumvalue', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='google.protobuf.Enum.options', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_context', full_name='google.protobuf.Enum.source_context', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='syntax', full_name='google.protobuf.Enum.syntax', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1059,
  serialized_end=1265,
)


_ENUMVALUE = _descriptor.Descriptor(
  name='EnumValue',
  full_name='google.protobuf.EnumValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.protobuf.EnumValue.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='number', full_name='google.protobuf.EnumValue.number', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='google.protobuf.EnumValue.options', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1267,
  serialized_end=1350,
)


_OPTION = _descriptor.Descriptor(
  name='Option',
  full_name='google.protobuf.Option',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.protobuf.Option.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.protobuf.Option.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1352,
  serialized_end=1411,
)

_TYPE.fields_by_name['fields'].message_type = _FIELD
_TYPE.fields_by_name['options'].message_type = _OPTION
_TYPE.fields_by_name['source_context'].message_type = google_dot_protobuf_dot_source__context__pb2._SOURCECONTEXT
_TYPE.fields_by_name['syntax'].enum_type = _SYNTAX
_FIELD.fields_by_name['kind'].enum_type = _FIELD_KIND
_FIELD.fields_by_name['cardinality'].enum_type = _FIELD_CARDINALITY
_FIELD.fields_by_name['options'].message_type = _OPTION
_FIELD_KIND.containing_type = _FIELD
_FIELD_CARDINALITY.containing_type = _FIELD
_ENUM.fields_by_name['enumvalue'].message_type = _ENUMVALUE
_ENUM.fields_by_name['options'].message_type = _OPTION
_ENUM.fields_by_name['source_context'].message_type = google_dot_protobuf_dot_source__context__pb2._SOURCECONTEXT
_ENUM.fields_by_name['syntax'].enum_type = _SYNTAX
_ENUMVALUE.fields_by_name['options'].message_type = _OPTION
_OPTION.fields_by_name['value'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['Type'] = _TYPE
DESCRIPTOR.message_types_by_name['Field'] = _FIELD
DESCRIPTOR.message_types_by_name['Enum'] = _ENUM
DESCRIPTOR.message_types_by_name['EnumValue'] = _ENUMVALUE
DESCRIPTOR.message_types_by_name['Option'] = _OPTION
DESCRIPTOR.enum_types_by_name['Syntax'] = _SYNTAX
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Type = _reflection.GeneratedProtocolMessageType('Type', (_message.Message,), dict(
  DESCRIPTOR = _TYPE,
  __module__ = 'google.protobuf.type_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.Type)
  ))
_sym_db.RegisterMessage(Type)

Field = _reflection.GeneratedProtocolMessageType('Field', (_message.Message,), dict(
  DESCRIPTOR = _FIELD,
  __module__ = 'google.protobuf.type_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.Field)
  ))
_sym_db.RegisterMessage(Field)

Enum = _reflection.GeneratedProtocolMessageType('Enum', (_message.Message,), dict(
  DESCRIPTOR = _ENUM,
  __module__ = 'google.protobuf.type_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.Enum)
  ))
_sym_db.RegisterMessage(Enum)

EnumValue = _reflection.GeneratedProtocolMessageType('EnumValue', (_message.Message,), dict(
  DESCRIPTOR = _ENUMVALUE,
  __module__ = 'google.protobuf.type_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.EnumValue)
  ))
_sym_db.RegisterMessage(EnumValue)

Option = _reflection.GeneratedProtocolMessageType('Option', (_message.Message,), dict(
  DESCRIPTOR = _OPTION,
  __module__ = 'google.protobuf.type_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.Option)
  ))
_sym_db.RegisterMessage(Option)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
