# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: suggestion.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10suggestion.proto\x12\x11suggestionPackage\"\x17\n\x05Reply\x12\x0e\n\x06\x63hance\x18\x01 \x01(\x02\".\n\rPersonalities\x12\r\n\x05\x66irst\x18\x01 \x03(\x05\x12\x0e\n\x06second\x18\x02 \x03(\x05\x32U\n\nSuggestion\x12G\n\tgetChance\x12 .suggestionPackage.Personalities\x1a\x18.suggestionPackage.Replyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'suggestion_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REPLY._serialized_start=39
  _REPLY._serialized_end=62
  _PERSONALITIES._serialized_start=64
  _PERSONALITIES._serialized_end=110
  _SUGGESTION._serialized_start=112
  _SUGGESTION._serialized_end=197
# @@protoc_insertion_point(module_scope)
