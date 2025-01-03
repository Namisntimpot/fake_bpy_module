import typing
import collections.abc
import typing_extensions
import fakebpy.types
import fakebpy_extras.object_utils

class AddTorus(fakebpy.types.Operator, fakebpy_extras.object_utils.AddObjectHelper):
    """Construct a torus mesh"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> fakebpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: fakebpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def draw(self, _context):
        """

        :param _context:
        """

    def execute(self, context):
        """

        :param context:
        """

    def invoke(self, context, _event):
        """

        :param context:
        :param _event:
        """

    def mode_update_callback(self, _context):
        """

        :param _context:
        """

def add_torus(major_rad, minor_rad, major_seg, minor_seg): ...
def add_uvs(mesh, minor_seg, major_seg): ...
