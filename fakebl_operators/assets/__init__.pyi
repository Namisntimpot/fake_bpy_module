import typing
import collections.abc
import typing_extensions
import fakebpy.types

class ASSET_OT_open_containing_blend_file(fakebpy.types.Operator):
    """Open the blend file that contains the active asset"""

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

    def cancel(self, context):
        """

        :param context:
        """

    def execute(self, context):
        """

        :param context:
        """

    def modal(self, context, event):
        """

        :param context:
        :param event:
        """

    def open_in_new_blender(self, filepath):
        """

        :param filepath:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class ASSET_OT_tag_add(AssetBrowserMetadataOperator, fakebpy.types.Operator):
    """Add a new keyword tag to the active asset"""

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

    def execute(self, context):
        """

        :param context:
        """

class ASSET_OT_tag_remove(AssetBrowserMetadataOperator, fakebpy.types.Operator):
    """Remove an existing keyword tag from the active asset"""

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

    def execute(self, context):
        """

        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class AssetBrowserMetadataOperator:
    @classmethod
    def poll(cls, context):
        """

        :param context:
        """
