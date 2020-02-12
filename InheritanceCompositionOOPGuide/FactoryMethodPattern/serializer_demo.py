# In serializer_demo.py

import json
import xml.etree.ElementTree as et


class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist


# 0-Case >>> Hard Coded !!!

# class SongSerializer:
#     def serialize(self, song, format):
#         if format == 'JSON':
#             song_info = {
#                 'id': song.song_id,
#                 'title': song.title,
#                 'artist': song.artist
#             }
#             return json.dumps(song_info)
#         elif format == 'XML':
#             song_info = et.Element('song', attrib={'id': song.song_id})
#             title = et.SubElement(song_info, 'title')
#             title.text = song.title
#             artist = et.SubElement(song_info, 'artist')
#             artist.text = song.artist
#             return et.tostring(song_info, encoding='unicode')
#         else:
#             raise ValueError(format)

# 1-Case >>> Refactoring Code Into the Desired Interface
# 2-Case >>> Basic Implementation of Factory Method

# A client (SongSerializer.serialize())
class SongSerializer:
    def serialize(self, song, format):
        serializer = _get_serializer(format)
        return serializer(song)

    # def serialize(self, song, format):
    #     if format == 'JSON':
    #         return self._serialize_to_json(song)
    #     elif format == 'XML':
    #         return self._serialize_to_xml(song)
    #     else:
    #         raise ValueError(format)

# creator component (get_serializer()) using some sort of identifier (format).
# Note: The ._get_serializer() method does not call the concrete
# implementation, and it just returns the function object itself.
def _get_serializer(format):
    if format == 'JSON':
        return _serialize_to_json
    elif format == 'XML':
        return _serialize_to_xml
    else:
        raise ValueError(format)



def _serialize_to_json(song):
    payload = {
        'id': song.song_id,
        'title': song.title,
        'artist': song.artist
    }
    return json.dumps(payload)

def _serialize_to_xml(song):
    song_element = et.Element('song', attrib={'id': song.song_id})
    title = et.SubElement(song_element, 'title')
    title.text = song.title
    artist = et.SubElement(song_element, 'artist')
    artist.text = song.artist
    return et.tostring(song_element, encoding='unicode')



# The .serialize() method in SongSerializer will require changes for 
# many different reasons. 
# This increases the risk of introducing new defects or breaking 
# existing functionality when changes are made. Let’s take a look 
# at all the situations that will require modifications to the implementation:

# 1. When a new format is introduced: 
#       The method will have to change to implement the serialization to 
#       that format.

# 2. When the Song object changes: 
#       Adding or removing properties to the Song class will 
#       require the implementation to change in order to accommodate 
#       the new structure.

# 3. When the string representation for a format changes
#       (plain JSON vs JSON API): The .serialize() 
#       method will have to change if the desired string
#        representation for a format changes because 
#       the representation is hard-coded in the .serialize() 
#       method implementation.
