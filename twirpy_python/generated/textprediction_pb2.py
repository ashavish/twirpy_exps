# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: textprediction.proto

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
  name='textprediction.proto',
  package='twitch.twirp.example',
  syntax='proto3',
  serialized_pb=_b('\n\x14textprediction.proto\x12\x14twitch.twirp.example\"3\n\tSentiment\x12\x11\n\tsentiment\x18\x01 \x01(\t\x12\x13\n\x0bprobability\x18\x02 \x01(\x02\"&\n\x07\x43ontent\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\r\n\x05model\x18\x02 \x01(\t2h\n\x12SentimentPredictor\x12R\n\x10PredictSentiment\x12\x1d.twitch.twirp.example.Content\x1a\x1f.twitch.twirp.example.SentimentB\tZ\x07\x65xampleb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SENTIMENT = _descriptor.Descriptor(
  name='Sentiment',
  full_name='twitch.twirp.example.Sentiment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sentiment', full_name='twitch.twirp.example.Sentiment.sentiment', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='probability', full_name='twitch.twirp.example.Sentiment.probability', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=97,
)


_CONTENT = _descriptor.Descriptor(
  name='Content',
  full_name='twitch.twirp.example.Content',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='twitch.twirp.example.Content.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='model', full_name='twitch.twirp.example.Content.model', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=137,
)

DESCRIPTOR.message_types_by_name['Sentiment'] = _SENTIMENT
DESCRIPTOR.message_types_by_name['Content'] = _CONTENT

Sentiment = _reflection.GeneratedProtocolMessageType('Sentiment', (_message.Message,), dict(
  DESCRIPTOR = _SENTIMENT,
  __module__ = 'textprediction_pb2'
  # @@protoc_insertion_point(class_scope:twitch.twirp.example.Sentiment)
  ))
_sym_db.RegisterMessage(Sentiment)

Content = _reflection.GeneratedProtocolMessageType('Content', (_message.Message,), dict(
  DESCRIPTOR = _CONTENT,
  __module__ = 'textprediction_pb2'
  # @@protoc_insertion_point(class_scope:twitch.twirp.example.Content)
  ))
_sym_db.RegisterMessage(Content)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\007example'))
# @@protoc_insertion_point(module_scope)
