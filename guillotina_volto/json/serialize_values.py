from guillotina import configure
from guillotina.schema import Choice
from guillotina.schema.vocabulary import SimpleVocabulary


@configure.value_serializer(SimpleVocabulary)
def vocabulary_converter(value):
    return [x.token for x in value]


@configure.value_deserializer(Choice)
def choice_converter(field, value, context):
    return value
