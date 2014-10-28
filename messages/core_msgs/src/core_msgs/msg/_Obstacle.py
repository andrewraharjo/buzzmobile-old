"""autogenerated by genpy from core_msgs/Obstacle.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class Obstacle(genpy.Message):
  _md5sum = "e85019b57cf217e7d529d6333370e839"
  _type = "core_msgs/Obstacle"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """#
# Obstacle messages are used to report any non-drivable object or region
# detected at a given time.
#
#

# A set of polygons to describe the obstacle.  It is assumed that
# the walls and interior of all of the polygons are non-drivable.
geometry_msgs/Polygon[] polygons

================================================================================
MSG: geometry_msgs/Polygon
#A specification of a polygon where the first and last points are assumed to be connected
Point32[] points

================================================================================
MSG: geometry_msgs/Point32
# This contains the position of a point in free space(with 32 bits of precision).
# It is recommeded to use Point wherever possible instead of Point32.  
# 
# This recommendation is to promote interoperability.  
#
# This message is designed to take up less space when sending
# lots of points at once, as in the case of a PointCloud.  

float32 x
float32 y
float32 z
"""
  __slots__ = ['polygons']
  _slot_types = ['geometry_msgs/Polygon[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       polygons

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Obstacle, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.polygons is None:
        self.polygons = []
    else:
      self.polygons = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.polygons)
      buff.write(_struct_I.pack(length))
      for val1 in self.polygons:
        length = len(val1.points)
        buff.write(_struct_I.pack(length))
        for val2 in val1.points:
          _x = val2
          buff.write(_struct_3f.pack(_x.x, _x.y, _x.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.polygons is None:
        self.polygons = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.polygons = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Polygon()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.points = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Point32()
          _x = val2
          start = end
          end += 12
          (_x.x, _x.y, _x.z,) = _struct_3f.unpack(str[start:end])
          val1.points.append(val2)
        self.polygons.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.polygons)
      buff.write(_struct_I.pack(length))
      for val1 in self.polygons:
        length = len(val1.points)
        buff.write(_struct_I.pack(length))
        for val2 in val1.points:
          _x = val2
          buff.write(_struct_3f.pack(_x.x, _x.y, _x.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.polygons is None:
        self.polygons = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.polygons = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Polygon()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.points = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Point32()
          _x = val2
          start = end
          end += 12
          (_x.x, _x.y, _x.z,) = _struct_3f.unpack(str[start:end])
          val1.points.append(val2)
        self.polygons.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3f = struct.Struct("<3f")