import typing
import collections.abc
import typing_extensions
import fakebl_ui.properties_animviz
import fakebpy.types
import fakerna_prop_ui

class ARMATURE_MT_collection_context_menu(fakebpy.types.Menu):
    bl_label: typing.Any
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

    def draw(self, context):
        """

        :param context:
        """

class ARMATURE_MT_collection_tree_context_menu(fakebpy.types.Menu):
    bl_label: typing.Any
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

    def draw(self, context):
        """

        :param context:
        """

class ArmatureButtonsPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class DATA_PT_bone_collections(ArmatureButtonsPanel, fakebpy.types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def draw(self, context):
        """

        :param context:
        """

class DATA_PT_context_arm(ArmatureButtonsPanel, fakebpy.types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def draw(self, context):
        """

        :param context:
        """

class DATA_PT_custom_props_arm(
    fakerna_prop_ui.PropertyPanel, ArmatureButtonsPanel, fakebpy.types.Panel
):
    """The subclass should have its own poll function
    and the variable '_context_path' MUST be set.
    """

    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_order: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

class DATA_PT_custom_props_bcoll(
    fakerna_prop_ui.PropertyPanel, ArmatureButtonsPanel, fakebpy.types.Panel
):
    """The subclass should have its own poll function
    and the variable '_context_path' MUST be set.
    """

    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_order: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class DATA_PT_display(ArmatureButtonsPanel, fakebpy.types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def draw(self, context):
        """

        :param context:
        """

class DATA_PT_iksolver_itasc(ArmatureButtonsPanel, fakebpy.types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def draw(self, context):
        """

        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class DATA_PT_motion_paths(
    fakebl_ui.properties_animviz.MotionPathButtonsPanel, fakebpy.types.Panel
):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def draw(self, context):
        """

        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class DATA_PT_motion_paths_display(
    fakebl_ui.properties_animviz.MotionPathButtonsPanel_display, fakebpy.types.Panel
):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def draw(self, context):
        """

        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class DATA_PT_pose(ArmatureButtonsPanel, fakebpy.types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def draw(self, context):
        """

        :param context:
        """

class DATA_UL_bone_collections(fakebpy.types.UIList):
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

    def draw_item(
        self,
        _context,
        layout,
        armature,
        bcoll,
        _icon,
        _active_data,
        _active_propname,
        _index,
    ):
        """

        :param _context:
        :param layout:
        :param armature:
        :param bcoll:
        :param _icon:
        :param _active_data:
        :param _active_propname:
        :param _index:
        """

class POSE_MT_selection_set_create(fakebpy.types.Menu):
    bl_label: typing.Any
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

    def draw(self, context):
        """

        :param context:
        """

class POSE_MT_selection_sets_context_menu(fakebpy.types.Menu):
    bl_label: typing.Any
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

    def draw(self, context):
        """

        :param context:
        """

class POSE_MT_selection_sets_select(fakebpy.types.Menu):
    bl_label: typing.Any
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

    def draw(self, context):
        """

        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class POSE_PT_selection_sets(fakebpy.types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def draw(self, context):
        """

        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class POSE_UL_selection_set(fakebpy.types.UIList):
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

    def draw_item(
        self, context, layout, data, item, icon, active_data, active_propname, index
    ):
        """

        :param context:
        :param layout:
        :param data:
        :param item:
        :param icon:
        :param active_data:
        :param active_propname:
        :param index:
        """
