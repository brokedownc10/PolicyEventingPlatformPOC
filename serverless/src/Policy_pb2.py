# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Policy.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Policy.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cPolicy.proto\"J\n\x06Policy\x12\x14\n\x0cpolicyNumber\x18\x01 \x01(\r\x12\x13\n\x0bpolicyPrice\x18\x02 \x01(\x01\x12\x15\n\rpolicyDetails\x18\x03 \x01(\tb\x06proto3'
)




_POLICY = _descriptor.Descriptor(
  name='Policy',
  full_name='Policy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='policyNumber', full_name='Policy.policyNumber', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='policyPrice', full_name='Policy.policyPrice', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='policyDetails', full_name='Policy.policyDetails', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=16,
  serialized_end=90,
)

DESCRIPTOR.message_types_by_name['Policy'] = _POLICY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Policy = _reflection.GeneratedProtocolMessageType('Policy', (_message.Message,), {
  'DESCRIPTOR' : _POLICY,
  '__module__' : 'Policy_pb2'
  # @@protoc_insertion_point(class_scope:Policy)
  })
_sym_db.RegisterMessage(Policy)


# @@protoc_insertion_point(module_scope)
