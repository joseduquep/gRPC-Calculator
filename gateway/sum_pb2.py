# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: sum.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'sum.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tsum.proto\x12\x03sum\"\"\n\nSumRequest\x12\t\n\x01\x61\x18\x01 \x01(\x02\x12\t\n\x01\x62\x18\x02 \x01(\x02\"\x1a\n\x08SumReply\x12\x0e\n\x06result\x18\x01 \x01(\x02\x32\x35\n\nSumService\x12\'\n\x05\x44oSum\x12\x0f.sum.SumRequest\x1a\r.sum.SumReplyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sum_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SUMREQUEST']._serialized_start=18
  _globals['_SUMREQUEST']._serialized_end=52
  _globals['_SUMREPLY']._serialized_start=54
  _globals['_SUMREPLY']._serialized_end=80
  _globals['_SUMSERVICE']._serialized_start=82
  _globals['_SUMSERVICE']._serialized_end=135
# @@protoc_insertion_point(module_scope)
