import typing
import collections.abc
import typing_extensions

def bmesh_linked_uv_islands(bm, uv_layer) -> list:
    """Returns lists of faces connected by UV islands.For meshes use `fakebpy.types.Mesh.mesh_linked_uv_islands` instead.

    :param bm: the fakebmesh used to group with.
    :param uv_layer: the UV layer to source UVs from.
    :return: list of lists containing polygon indices
    :rtype: list
    """

def match_uv(face, vert, uv, uv_layer): ...
