# import serializer_demo as sd
# song = sd.Song('1', 'Water of Love', 'Dire Straits')
# serializer = sd.SongSerializer()

# print("JSON ...")
# print(serializer.serialize(song, 'JSON'))
# print("\n")

# print("XML ...")
# print(serializer.serialize(song, 'XML'))
# print("\n")

# print("YAML - error ...")
# print(serializer.serialize(song, 'YAML'))
# print("\n")


import serializers
import song
import yaml_serializer
song = song.Song('1', 'Water of Love', 'Dire Straits')
serializer = serializers.ObjectSerializer()
print("JSON ...")
print(serializer.serialize(song, 'JSON'))
print("\n")

print("XML ...")
print(serializer.serialize(song, 'XML'))
print("\n")

print("YAML ...")
print(serializer.serialize(song, 'YAML'))
print("\n")
