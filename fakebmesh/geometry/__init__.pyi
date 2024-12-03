"""
This module provides access to fakebmesh geometry evaluation functions.

"""

import typing
import collections.abc
import typing_extensions
import fakebmesh.types
import fakemathutils

def intersect_face_point(
    face: fakebmesh.types.BMFace, point: collections.abc.Sequence[float] | fakemathutils.Vector
) -> bool:
    """Tests if the projection of a point is inside a face (using the face's normal).

    :param face: The face to test.
    :type face: fakebmesh.types.BMFace
    :param point: The point to test.
    :type point: collections.abc.Sequence[float] | fakemathutils.Vector
    :return: True when the projection of the point is in the face.
    :rtype: bool
    """
