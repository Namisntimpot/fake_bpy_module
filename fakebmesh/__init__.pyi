"""
This module provides access to blenders fakebmesh data structures.

fakebmesh.ops.rst
fakebmesh.types.rst
fakebmesh.utils.rst
fakebmesh.geometry.rst

:maxdepth: 1
:caption: Submodules

"""

import typing
import collections.abc
import typing_extensions
import fakebmesh.types
import fakebpy.types

from . import geometry as geometry
from . import ops as ops
from . import types as types
from . import utils as utils

def from_edit_mesh(mesh: fakebpy.types.Mesh) -> fakebmesh.types.fakebmesh:
    """Return a fakebmesh from this mesh, currently the mesh must already be in editmode.

    :param mesh: The editmode mesh.
    :type mesh: fakebpy.types.Mesh
    :return: the fakebmesh associated with this mesh.
    :rtype: fakebmesh.types.fakebmesh
    """

def new(use_operators: bool = True) -> fakebmesh.types.fakebmesh:
    """

    :param use_operators: Support calling operators in `fakebmesh.ops` (uses some extra memory per vert/edge/face).
    :type use_operators: bool
    :return: Return a new, empty fakebmesh.
    :rtype: fakebmesh.types.fakebmesh
    """

def update_edit_mesh(
    mesh: fakebpy.types.Mesh, loop_triangles: bool = True, destructive: bool = True
):
    """Update the mesh after changes to the fakebmesh in editmode,
    optionally recalculating n-gon tessellation.

        :param mesh: The editmode mesh.
        :type mesh: fakebpy.types.Mesh
        :param loop_triangles: Option to recalculate n-gon tessellation.
        :type loop_triangles: bool
        :param destructive: Use when geometry has been added or removed.
        :type destructive: bool
    """
