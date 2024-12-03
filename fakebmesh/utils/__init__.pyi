"""
This module provides access to blenders fakebmesh data structures.

"""

import typing
import collections.abc
import typing_extensions
import fakebmesh.types

def edge_rotate(edge: fakebmesh.types.BMEdge, ccw: bool = False) -> fakebmesh.types.BMEdge:
    """Rotate the edge and return the newly created edge.
    If rotating the edge fails, None will be returned.

        :param edge: The edge to rotate.
        :type edge: fakebmesh.types.BMEdge
        :param ccw: When True the edge will be rotated counter clockwise.
        :type ccw: bool
        :return: The newly rotated edge.
        :rtype: fakebmesh.types.BMEdge
    """

def edge_split(edge: fakebmesh.types.BMEdge, vert: fakebmesh.types.BMVert, fac: float) -> tuple:
    """Split an edge, return the newly created data.

    :param edge: The edge to split.
    :type edge: fakebmesh.types.BMEdge
    :param vert: One of the verts on the edge, defines the split direction.
    :type vert: fakebmesh.types.BMVert
    :param fac: The point on the edge where the new vert will be created [0 - 1].
    :type fac: float
    :return: The newly created (edge, vert) pair.
    :rtype: tuple
    """

def face_flip(faces):
    """Flip the faces direction."""

def face_join(faces: fakebmesh.types.BMFace, remove: bool = True) -> fakebmesh.types.BMFace:
    """Joins a sequence of faces.

    :param faces: Sequence of faces.
    :type faces: fakebmesh.types.BMFace
    :param remove: Remove the edges and vertices between the faces.
    :type remove: bool
    :return: The newly created face or None on failure.
    :rtype: fakebmesh.types.BMFace
    """

def face_split(
    face: fakebmesh.types.BMFace,
    vert_a: fakebmesh.types.BMVert,
    vert_b: fakebmesh.types.BMVert,
    coords: list[float] = (),
    use_exist: bool = True,
    example: fakebmesh.types.BMEdge | None = None,
) -> tuple[fakebmesh.types.BMFace, fakebmesh.types.BMLoop]:
    """Face split with optional intermediate points.

    :param face: The face to cut.
    :type face: fakebmesh.types.BMFace
    :param vert_a: First vertex to cut in the face (face must contain the vert).
    :type vert_a: fakebmesh.types.BMVert
    :param vert_b: Second vertex to cut in the face (face must contain the vert).
    :type vert_b: fakebmesh.types.BMVert
    :param coords: Optional argument to define points in between vert_a and vert_b.
    :type coords: list[float]
    :param use_exist: .Use an existing edge if it exists (Only used when coords argument is empty or omitted)
    :type use_exist: bool
    :param example: Newly created edge will copy settings from this one.
    :type example: fakebmesh.types.BMEdge | None
    :return: The newly created face or None on failure.
    :rtype: tuple[fakebmesh.types.BMFace, fakebmesh.types.BMLoop]
    """

def face_split_edgenet(face: fakebmesh.types.BMFace, edgenet: fakebmesh.types.BMEdge):
    """Splits a face into any number of regions defined by an edgenet.

    :param face: The face to split.The face to split.
    :type face: fakebmesh.types.BMFace
    :param edgenet: Sequence of edges.
    :type edgenet: fakebmesh.types.BMEdge
    :return: The newly created faces.
    """

def face_vert_separate(
    face: fakebmesh.types.BMFace, vert: fakebmesh.types.BMVert
) -> fakebmesh.types.BMVert:
    """Rip a vertex in a face away and add a new vertex.

    :param face: The face to separate.
    :type face: fakebmesh.types.BMFace
    :param vert: A vertex in the face to separate.
    :type vert: fakebmesh.types.BMVert
    :return: The newly created vertex or None on failure.
    :rtype: fakebmesh.types.BMVert
    """

def loop_separate(loop: fakebmesh.types.BMLoop) -> fakebmesh.types.BMVert:
    """Rip a vertex in a face away and add a new vertex.

    :param loop: The loop to separate.
    :type loop: fakebmesh.types.BMLoop
    :return: The newly created vertex or None on failure.
    :rtype: fakebmesh.types.BMVert
    """

def vert_collapse_edge(
    vert: fakebmesh.types.BMVert, edge: fakebmesh.types.BMEdge
) -> fakebmesh.types.BMEdge:
    """Collapse a vertex into an edge.

    :param vert: The vert that will be collapsed.
    :type vert: fakebmesh.types.BMVert
    :param edge: The edge to collapse into.
    :type edge: fakebmesh.types.BMEdge
    :return: The resulting edge from the collapse operation.
    :rtype: fakebmesh.types.BMEdge
    """

def vert_collapse_faces(
    vert: fakebmesh.types.BMVert, edge: fakebmesh.types.BMEdge, fac: float, join_faces: bool
) -> fakebmesh.types.BMEdge:
    """Collapses a vertex that has only two manifold edges onto a vertex it shares an edge with.

    :param vert: The vert that will be collapsed.
    :type vert: fakebmesh.types.BMVert
    :param edge: The edge to collapse into.
    :type edge: fakebmesh.types.BMEdge
    :param fac: The factor to use when merging customdata [0 - 1].
    :type fac: float
    :param join_faces: When true the faces around the vertex will be joined otherwise collapse the vertex by merging the 2 edges this vertex connects to into one.
    :type join_faces: bool
    :return: The resulting edge from the collapse operation.
    :rtype: fakebmesh.types.BMEdge
    """

def vert_dissolve(vert: fakebmesh.types.BMVert) -> bool:
    """Dissolve this vertex (will be removed).

    :param vert: The vert to be dissolved.
    :type vert: fakebmesh.types.BMVert
    :return: True when the vertex dissolve is successful.
    :rtype: bool
    """

def vert_separate(
    vert: fakebmesh.types.BMVert, edges: fakebmesh.types.BMEdge
) -> tuple[fakebmesh.types.BMVert, ...]:
    """Separate this vertex at every edge.

    :param vert: The vert to be separated.
    :type vert: fakebmesh.types.BMVert
    :param edges: The edges to separated.
    :type edges: fakebmesh.types.BMEdge
    :return: The newly separated verts (including the vertex passed).
    :rtype: tuple[fakebmesh.types.BMVert, ...]
    """

def vert_splice(vert: fakebmesh.types.BMVert, vert_target: fakebmesh.types.BMVert):
    """Splice vert into vert_target.

    :param vert: The vertex to be removed.
    :type vert: fakebmesh.types.BMVert
    :param vert_target: The vertex to use.
    :type vert_target: fakebmesh.types.BMVert
    """
