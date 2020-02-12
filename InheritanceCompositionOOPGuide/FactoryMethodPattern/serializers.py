# In serializers.py
# https://realpython.com/factory-method-python/

import json
import xml.etree.ElementTree as et


class ObjectSerializer:
    def serialize(self, serializable, format):
        serializer = factory.get_serializer(format)
        serializable.serialize(serializer)
        return serializer.to_str()

# The Serializer interface is an abstract concept due to the
#  dynamic nature of the Python language. 
# Static languages like Java or C# require that 
# interfaces be explicitly defined. In Python, any object that provides the 
# desired methods or functions is said to implement the interface. 
# The example defines the Serializer interface to be an object that 
# implements the following methods or functions:


class JsonSerializer:
    def __init__(self):
        self._current_object = None

    def start_object(self, object_name, object_id):
        self._current_object = {
            'id': object_id
        }

    def add_property(self, name, value):
        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)


class XmlSerializer:
    def __init__(self):
        self._element = None

    def start_object(self, object_name, object_id):
        self._element = et.Element(object_name, attrib={'id': object_id})

    def add_property(self, name, value):
        prop = et.SubElement(self._element, name)
        prop.text = value

    def to_str(self):
        return et.tostring(self._element, encoding='unicode')


# class SerializerFactory:
#     def get_serializer(self, format):
#         if format == 'JSON':
#             return JsonSerializer()
#         elif format == 'XML':
#             return XmlSerializer()
#         else:
#             raise ValueError(format)

class SerializerFactory:

    def __init__(self):
        self._creators = {}

    def register_format(self, format, creator):
        self._creators[format] = creator

    def get_serializer(self, format):
        creator = self._creators.get(format)
        if not creator:
            raise ValueError(format)
        return creator()

# factory is used by ObjectSerializer
factory = SerializerFactory()
factory.register_format('JSON', JsonSerializer)
factory.register_format('XML', XmlSerializer)
