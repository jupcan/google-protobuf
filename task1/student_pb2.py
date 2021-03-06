# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: student.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='student.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\rstudent.proto\"\x98\x01\n\x07Student\x12\x0b\n\x03\x44NI\x18\x01 \x02(\t\x12+\n\x04type\x18\x02 \x01(\x0e\x32\x14.Student.StudentType:\x07UNKNOWN\x12\x11\n\tfirstname\x18\x03 \x01(\t\x12\x10\n\x08lastname\x18\x04 \x01(\t\".\n\x0bStudentType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04PASS\x10\x01\x12\x08\n\x04\x46\x41IL\x10\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_STUDENT_STUDENTTYPE = _descriptor.EnumDescriptor(
  name='StudentType',
  full_name='Student.StudentType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PASS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAIL', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=124,
  serialized_end=170,
)
_sym_db.RegisterEnumDescriptor(_STUDENT_STUDENTTYPE)


_STUDENT = _descriptor.Descriptor(
  name='Student',
  full_name='Student',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='DNI', full_name='Student.DNI', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Student.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='firstname', full_name='Student.firstname', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lastname', full_name='Student.lastname', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STUDENT_STUDENTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=170,
)

_STUDENT.fields_by_name['type'].enum_type = _STUDENT_STUDENTTYPE
_STUDENT_STUDENTTYPE.containing_type = _STUDENT
DESCRIPTOR.message_types_by_name['Student'] = _STUDENT

Student = _reflection.GeneratedProtocolMessageType('Student', (_message.Message,), dict(
  DESCRIPTOR = _STUDENT,
  __module__ = 'student_pb2'
  # @@protoc_insertion_point(class_scope:Student)
  ))
_sym_db.RegisterMessage(Student)


# @@protoc_insertion_point(module_scope)
