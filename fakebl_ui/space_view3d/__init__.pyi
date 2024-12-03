import typing
import collections.abc
import typing_extensions
import fakebl_ui.properties_grease_pencil_common
import fakebl_ui.properties_paint_common
import fakebl_ui.space_toolsystem_common
import fakebpy.types

class BoneOptions:
    def draw(self, context):
        """

        :param context:
        """

class ShowHideMenu:
    bl_label: typing.Any

    def draw(self, _context):
        """

        :param _context:
        """

class TOPBAR_MT_edit_armature_add(fakebpy.types.Menu):
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

class TOPBAR_MT_edit_curve_add(fakebpy.types.Menu):
    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    bl_translation_context: typing.Any
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

class TOPBAR_PT_annotation_layers(
    fakebpy.types.Panel, fakebl_ui.properties_grease_pencil_common.AnnotationDataPanel
):
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    bl_ui_units_x: typing.Any
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

class TOPBAR_PT_gpencil_materials(
    fakebl_ui.properties_grease_pencil_common.GreasePencilMaterialsPanel, fakebpy.types.Panel
):
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    bl_ui_units_x: typing.Any
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

class TOPBAR_PT_gpencil_vertexcolor(
    fakebl_ui.properties_grease_pencil_common.GreasePencilVertexcolorPanel, fakebpy.types.Panel
):
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    bl_ui_units_x: typing.Any
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

class VIEW3D_AST_sculpt_brushes(
    fakebl_ui.properties_paint_common.BrushAssetShelf, fakebpy.types.AssetShelf
):
    bl_default_preview_size: typing.Any
    bl_options: typing.Any
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

class VIEW3D_HT_header(fakebpy.types.Header):
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

    @staticmethod
    def draw_xform_template(layout, context):
        """

        :param layout:
        :param context:
        """

class VIEW3D_HT_tool_header(fakebpy.types.Header):
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

    def draw_mode_settings(self, context):
        """

        :param context:
        """

    def draw_tool_settings(self, context):
        """

        :param context:
        """

class VIEW3D_MT_add(fakebpy.types.Menu):
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    bl_translation_context: typing.Any
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

class VIEW3D_MT_armature_add(fakebpy.types.Menu):
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

class VIEW3D_MT_armature_context_menu(fakebpy.types.Menu):
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

class VIEW3D_MT_assign_material(fakebpy.types.Menu):
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

class VIEW3D_MT_bone_collections(fakebpy.types.Menu):
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

class VIEW3D_MT_brush_paint_modes(fakebpy.types.Menu):
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

class VIEW3D_MT_camera_add(fakebpy.types.Menu):
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

class VIEW3D_MT_curve_add(fakebpy.types.Menu):
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

    def draw(self, context):
        """

        :param context:
        """

class VIEW3D_MT_draw_gpencil(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_armature(fakebpy.types.Menu):
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

class VIEW3D_MT_edit_armature_delete(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_armature_names(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_armature_parent(fakebpy.types.Menu):
    bl_label: typing.Any
    bl_rna: typing.Any
    bl_translation_context: typing.Any
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

class VIEW3D_MT_edit_armature_roll(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_curve(fakebpy.types.Menu):
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

class VIEW3D_MT_edit_curve_clean(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_curve_context_menu(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_curve_ctrlpoints(fakebpy.types.Menu):
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

class VIEW3D_MT_edit_curve_delete(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_curve_segments(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_curve_showhide(ShowHideMenu, fakebpy.types.Menu):
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

class VIEW3D_MT_edit_curves(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_curves_add(fakebpy.types.Menu):
    bl_label: typing.Any
    bl_rna: typing.Any
    bl_translation_context: typing.Any
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

class VIEW3D_MT_edit_curves_context_menu(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_curves_control_points(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_curves_segments(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_curves_select_more_less(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_font(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_font_chars(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_font_context_menu(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_font_delete(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_font_kerning(fakebpy.types.Menu):
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

class VIEW3D_MT_edit_gpencil(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_gpencil_delete(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_gpencil_point(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_gpencil_showhide(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_gpencil_stroke(fakebpy.types.Menu):
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

class VIEW3D_MT_edit_gpencil_transform(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_greasepencil(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_greasepencil_animation(fakebpy.types.Menu):
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

class VIEW3D_MT_edit_greasepencil_cleanup(fakebpy.types.Menu):
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

class VIEW3D_MT_edit_greasepencil_delete(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_greasepencil_point(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_greasepencil_showhide(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_greasepencil_stroke(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_lattice(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_lattice_context_menu(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_mesh(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_mesh_clean(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_mesh_context_menu(fakebpy.types.Menu):
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

class VIEW3D_MT_edit_mesh_delete(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_mesh_edges(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_mesh_extrude(fakebpy.types.Menu):
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

class VIEW3D_MT_edit_mesh_faces(fakebpy.types.Menu):
    bl_idname: typing.Any
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

class VIEW3D_MT_edit_mesh_faces_data(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_mesh_merge(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_mesh_normals(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_mesh_normals_average(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_mesh_normals_select_strength(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_mesh_normals_set_strength(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_mesh_select_by_trait(fakebpy.types.Menu):
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

class VIEW3D_MT_edit_mesh_select_linked(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_mesh_select_loops(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_mesh_select_mode(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_mesh_select_more_less(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_mesh_select_similar(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_mesh_shading(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_mesh_showhide(ShowHideMenu, fakebpy.types.Menu):
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

class VIEW3D_MT_edit_mesh_split(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_mesh_vertices(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_mesh_weights(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_meta(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_meta_showhide(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_metaball_context_menu(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_edit_pointcloud(fakebpy.types.Menu):
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

class VIEW3D_MT_edit_surface(fakebpy.types.Menu):
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

class VIEW3D_MT_editor_menus(fakebpy.types.Menu):
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

class VIEW3D_MT_face_sets(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_face_sets_init(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_gpencil_animation(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class VIEW3D_MT_gpencil_autoweights(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_gpencil_edit_context_menu(fakebpy.types.Menu):
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

class VIEW3D_MT_gpencil_simplify(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_gpencil_vertex_group(fakebpy.types.Menu):
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

class VIEW3D_MT_grease_pencil_add(fakebpy.types.Menu):
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

class VIEW3D_MT_grease_pencil_assign_material(fakebpy.types.Menu):
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

class VIEW3D_MT_greasepencil_edit_context_menu(fakebpy.types.Menu):
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

class VIEW3D_MT_greasepencil_material_active(fakebpy.types.Menu):
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

class VIEW3D_MT_greasepencil_vertex_group(fakebpy.types.Menu):
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

class VIEW3D_MT_hook(fakebpy.types.Menu):
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

class VIEW3D_MT_image_add(fakebpy.types.Menu):
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

class VIEW3D_MT_light_add(fakebpy.types.Menu):
    bl_context: typing.Any
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

class VIEW3D_MT_lightprobe_add(fakebpy.types.Menu):
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

class VIEW3D_MT_make_links(fakebpy.types.Menu):
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

class VIEW3D_MT_make_single_user(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_mask(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_mesh_add(fakebpy.types.Menu):
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

class VIEW3D_MT_metaball_add(fakebpy.types.Menu):
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

class VIEW3D_MT_mirror(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_object(fakebpy.types.Menu):
    bl_context: typing.Any
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

class VIEW3D_MT_object_animation(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_object_apply(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_object_asset(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_object_cleanup(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_object_clear(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_object_collection(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_object_constraints(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_object_context_menu(fakebpy.types.Menu):
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

class VIEW3D_MT_object_convert(fakebpy.types.Menu):
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

class VIEW3D_MT_object_liboverride(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_object_mode_pie(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_object_modifiers(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_object_parent(fakebpy.types.Menu):
    bl_label: typing.Any
    bl_rna: typing.Any
    bl_translation_context: typing.Any
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

class VIEW3D_MT_object_quick_effects(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_object_relations(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_object_rigid_body(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_object_shading(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_object_showhide(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_object_track(fakebpy.types.Menu):
    bl_label: typing.Any
    bl_rna: typing.Any
    bl_translation_context: typing.Any
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

class VIEW3D_MT_orientations_pie(fakebpy.types.Menu):
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

class VIEW3D_MT_paint_gpencil(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_paint_grease_pencil(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_paint_vertex(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_paint_weight(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

    @staticmethod
    def draw_generic(layout, is_editmode=False):
        """

        :param layout:
        :param is_editmode:
        """

class VIEW3D_MT_paint_weight_lock(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_particle(fakebpy.types.Menu):
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

class VIEW3D_MT_particle_context_menu(fakebpy.types.Menu):
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

class VIEW3D_MT_particle_showhide(ShowHideMenu, fakebpy.types.Menu):
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

class VIEW3D_MT_pivot_pie(fakebpy.types.Menu):
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

class VIEW3D_MT_pose(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_pose_apply(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_pose_constraints(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_pose_context_menu(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_pose_ik(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_pose_motion(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_pose_names(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_pose_propagate(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_pose_showhide(ShowHideMenu, fakebpy.types.Menu):
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

class VIEW3D_MT_pose_slide(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_pose_transform(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_proportional_editing_falloff_pie(fakebpy.types.Menu):
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

class VIEW3D_MT_random_mask(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_sculpt(fakebpy.types.Menu):
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

class VIEW3D_MT_sculpt_automasking_pie(fakebpy.types.Menu):
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

class VIEW3D_MT_sculpt_curves(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_sculpt_face_sets_edit_pie(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_sculpt_gpencil_automasking_pie(fakebpy.types.Menu):
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

class VIEW3D_MT_sculpt_mask_edit_pie(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_sculpt_set_pivot(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_sculpt_showhide(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_sculpt_transform(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_sculpt_trim(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_select_edit_armature(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_select_edit_curve(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_select_edit_curves(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_select_edit_gpencil(fakebpy.types.Menu):
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

class VIEW3D_MT_select_edit_grease_pencil(fakebpy.types.Menu):
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

class VIEW3D_MT_select_edit_lattice(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_select_edit_mesh(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_select_edit_metaball(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_select_edit_point_cloud(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_select_edit_surface(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_select_edit_text(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_select_object(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_select_object_more_less(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_select_paint_mask(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_select_paint_mask_vertex(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_select_particle(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_select_pose(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_select_pose_more_less(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_select_sculpt_curves(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_shading_ex_pie(fakebpy.types.Menu):
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

class VIEW3D_MT_shading_pie(fakebpy.types.Menu):
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

class VIEW3D_MT_snap(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_snap_pie(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_surface_add(fakebpy.types.Menu):
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

class VIEW3D_MT_transform(VIEW3D_MT_transform_base, fakebpy.types.Menu):
    bl_category: typing.Any
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

class VIEW3D_MT_transform_armature(VIEW3D_MT_transform_base, fakebpy.types.Menu):
    bl_category: typing.Any
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

class VIEW3D_MT_transform_base:
    bl_category: typing.Any
    bl_label: typing.Any

    def draw(self, context):
        """

        :param context:
        """

class VIEW3D_MT_transform_gizmo_pie(fakebpy.types.Menu):
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

class VIEW3D_MT_transform_object(VIEW3D_MT_transform_base, fakebpy.types.Menu):
    bl_category: typing.Any
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

class VIEW3D_MT_uv_map(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_vertex_group(fakebpy.types.Menu):
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

class VIEW3D_MT_view(fakebpy.types.Menu):
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

class VIEW3D_MT_view_align(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_view_align_selected(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_view_cameras(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_view_local(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_view_navigation(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_view_pie(fakebpy.types.Menu):
    bl_idname: typing.Any
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_view_regions(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_view_viewpoint(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_volume_add(fakebpy.types.Menu):
    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    bl_translation_context: typing.Any
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

class VIEW3D_MT_weight_gpencil(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_weight_grease_pencil(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_MT_wpaint_vgroup_lock_pie(fakebpy.types.Menu):
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

    def draw(self, _context):
        """

        :param _context:
        """

class VIEW3D_PT_active_tool(
    fakebpy.types.Panel, fakebl_ui.space_toolsystem_common.ToolActivePanelHelper
):
    bl_category: typing.Any
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

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class VIEW3D_PT_active_tool_duplicate(
    fakebpy.types.Panel, fakebl_ui.space_toolsystem_common.ToolActivePanelHelper
):
    bl_category: typing.Any
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

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class VIEW3D_PT_annotation_onion(
    fakebl_ui.properties_grease_pencil_common.AnnotationOnionSkin, fakebpy.types.Panel
):
    bl_category: typing.Any
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

class VIEW3D_PT_collections(fakebpy.types.Panel):
    bl_category: typing.Any
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

class VIEW3D_PT_context_properties(fakebpy.types.Panel):
    bl_category: typing.Any
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

class VIEW3D_PT_curves_sculpt_add_shape(fakebpy.types.Panel):
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

class VIEW3D_PT_curves_sculpt_grow_shrink_scaling(fakebpy.types.Panel):
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    bl_ui_units_x: typing.Any
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

class VIEW3D_PT_curves_sculpt_parameter_falloff(fakebpy.types.Panel):
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

class VIEW3D_PT_gizmo_display(fakebpy.types.Panel):
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    bl_ui_units_x: typing.Any
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

class VIEW3D_PT_gpencil_curve_edit(fakebpy.types.Panel):
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

class VIEW3D_PT_gpencil_draw_context_menu(fakebpy.types.Panel):
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    bl_ui_units_x: typing.Any
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

class VIEW3D_PT_gpencil_guide(fakebpy.types.Panel):
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

class VIEW3D_PT_gpencil_lock(fakebpy.types.Panel):
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

class VIEW3D_PT_gpencil_multi_frame(fakebpy.types.Panel):
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

class VIEW3D_PT_gpencil_origin(fakebpy.types.Panel):
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

class VIEW3D_PT_gpencil_sculpt_automasking(fakebpy.types.Panel):
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    bl_ui_units_x: typing.Any
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

class VIEW3D_PT_gpencil_sculpt_context_menu(fakebpy.types.Panel):
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    bl_ui_units_x: typing.Any
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

class VIEW3D_PT_gpencil_vertex_context_menu(fakebpy.types.Panel):
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    bl_ui_units_x: typing.Any
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

class VIEW3D_PT_gpencil_weight_context_menu(fakebpy.types.Panel):
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    bl_ui_units_x: typing.Any
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

class VIEW3D_PT_grease_pencil(
    fakebl_ui.properties_grease_pencil_common.AnnotationDataPanel, fakebpy.types.Panel
):
    bl_category: typing.Any
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

class VIEW3D_PT_grease_pencil_multi_frame(fakebpy.types.Panel):
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

class VIEW3D_PT_object_type_visibility(fakebpy.types.Panel):
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    bl_ui_units_x: typing.Any
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

    def draw_ex(self, _context, view, show_select):
        """

        :param _context:
        :param view:
        :param show_select:
        """

class VIEW3D_PT_overlay(fakebpy.types.Panel):
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    bl_ui_units_x: typing.Any
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

class VIEW3D_PT_overlay_bones(fakebpy.types.Panel):
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

    @staticmethod
    def is_using_wireframe(context):
        """

        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class VIEW3D_PT_overlay_edit_curve(fakebpy.types.Panel):
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

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class VIEW3D_PT_overlay_edit_mesh(fakebpy.types.Panel):
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    bl_ui_units_x: typing.Any
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

class VIEW3D_PT_overlay_edit_mesh_freestyle(fakebpy.types.Panel):
    bl_label: typing.Any
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

class VIEW3D_PT_overlay_edit_mesh_measurement(fakebpy.types.Panel):
    bl_label: typing.Any
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

class VIEW3D_PT_overlay_edit_mesh_normals(fakebpy.types.Panel):
    bl_label: typing.Any
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

class VIEW3D_PT_overlay_edit_mesh_shading(fakebpy.types.Panel):
    bl_label: typing.Any
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

class VIEW3D_PT_overlay_geometry(fakebpy.types.Panel):
    bl_label: typing.Any
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

class VIEW3D_PT_overlay_gpencil_options(fakebpy.types.Panel):
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    bl_ui_units_x: typing.Any
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

class VIEW3D_PT_overlay_grease_pencil_options(fakebpy.types.Panel):
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    bl_ui_units_x: typing.Any
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

class VIEW3D_PT_overlay_guides(fakebpy.types.Panel):
    bl_label: typing.Any
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

class VIEW3D_PT_overlay_motion_tracking(fakebpy.types.Panel):
    bl_label: typing.Any
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

    def draw_header(self, context):
        """

        :param context:
        """

class VIEW3D_PT_overlay_object(fakebpy.types.Panel):
    bl_label: typing.Any
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

class VIEW3D_PT_overlay_sculpt(fakebpy.types.Panel):
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

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class VIEW3D_PT_overlay_sculpt_curves(fakebpy.types.Panel):
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

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class VIEW3D_PT_overlay_texture_paint(fakebpy.types.Panel):
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

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class VIEW3D_PT_overlay_vertex_paint(fakebpy.types.Panel):
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

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class VIEW3D_PT_overlay_viewer_node(fakebpy.types.Panel):
    bl_label: typing.Any
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

class VIEW3D_PT_overlay_weight_paint(fakebpy.types.Panel):
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    bl_ui_units_x: typing.Any
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

class VIEW3D_PT_paint_texture_context_menu(fakebpy.types.Panel):
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

class VIEW3D_PT_paint_vertex_context_menu(fakebpy.types.Panel):
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

class VIEW3D_PT_paint_weight_context_menu(fakebpy.types.Panel):
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

class VIEW3D_PT_proportional_edit(fakebpy.types.Panel):
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    bl_ui_units_x: typing.Any
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

class VIEW3D_PT_quad_view(fakebpy.types.Panel):
    bl_category: typing.Any
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

class VIEW3D_PT_sculpt_automasking(fakebpy.types.Panel):
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    bl_ui_units_x: typing.Any
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

class VIEW3D_PT_sculpt_context_menu(fakebpy.types.Panel):
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

class VIEW3D_PT_sculpt_snapping(fakebpy.types.Panel):
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

class VIEW3D_PT_shading(fakebpy.types.Panel):
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    bl_ui_units_x: typing.Any
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

    @classmethod
    def get_shading(cls, context):
        """

        :param context:
        """

class VIEW3D_PT_shading_color(fakebpy.types.Panel):
    bl_label: typing.Any
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

class VIEW3D_PT_shading_compositor(fakebpy.types.Panel):
    bl_label: typing.Any
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

    def draw(self, context):
        """

        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class VIEW3D_PT_shading_lighting(fakebpy.types.Panel):
    bl_label: typing.Any
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

class VIEW3D_PT_shading_options(fakebpy.types.Panel):
    bl_label: typing.Any
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

class VIEW3D_PT_shading_options_shadow(fakebpy.types.Panel):
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

class VIEW3D_PT_shading_options_ssao(fakebpy.types.Panel):
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

class VIEW3D_PT_shading_render_pass(fakebpy.types.Panel):
    COMPAT_ENGINES: typing.Any
    bl_label: typing.Any
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

class VIEW3D_PT_snapping(fakebpy.types.Panel):
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

class VIEW3D_PT_transform_orientations(fakebpy.types.Panel):
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    bl_ui_units_x: typing.Any
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

class VIEW3D_PT_view3d_cursor(fakebpy.types.Panel):
    bl_category: typing.Any
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

class VIEW3D_PT_view3d_lock(fakebpy.types.Panel):
    bl_category: typing.Any
    bl_label: typing.Any
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

class VIEW3D_PT_view3d_properties(fakebpy.types.Panel):
    bl_category: typing.Any
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

class VIEW3D_PT_view3d_stereo(fakebpy.types.Panel):
    bl_category: typing.Any
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

class VIEW3D_PT_viewport_debug(fakebpy.types.Panel):
    bl_label: typing.Any
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

class _draw_tool_settings_context_mode:
    @staticmethod
    def PAINT_GPENCIL(context, layout, tool):
        """

        :param context:
        :param layout:
        :param tool:
        """

    @staticmethod
    def PAINT_GREASE_PENCIL(context, layout, tool):
        """

        :param context:
        :param layout:
        :param tool:
        """

    @staticmethod
    def PAINT_TEXTURE(context, layout, tool):
        """

        :param context:
        :param layout:
        :param tool:
        """

    @staticmethod
    def PAINT_VERTEX(context, layout, tool):
        """

        :param context:
        :param layout:
        :param tool:
        """

    @staticmethod
    def PAINT_WEIGHT(context, layout, tool):
        """

        :param context:
        :param layout:
        :param tool:
        """

    @staticmethod
    def PARTICLE(context, layout, tool):
        """

        :param context:
        :param layout:
        :param tool:
        """

    @staticmethod
    def SCULPT(context, layout, tool):
        """

        :param context:
        :param layout:
        :param tool:
        """

    @staticmethod
    def SCULPT_CURVES(context, layout, tool):
        """

        :param context:
        :param layout:
        :param tool:
        """

    @staticmethod
    def SCULPT_GPENCIL(context, layout, tool):
        """

        :param context:
        :param layout:
        :param tool:
        """

    @staticmethod
    def SCULPT_GREASE_PENCIL(context, layout, tool):
        """

        :param context:
        :param layout:
        :param tool:
        """

    @staticmethod
    def VERTEX_GPENCIL(context, layout, tool):
        """

        :param context:
        :param layout:
        :param tool:
        """

    @staticmethod
    def WEIGHT_GPENCIL(context, layout, tool):
        """

        :param context:
        :param layout:
        :param tool:
        """

    @staticmethod
    def WEIGHT_GREASE_PENCIL(context, layout, tool):
        """

        :param context:
        :param layout:
        :param tool:
        """

class VIEW3D_MT_bone_options_disable(fakebpy.types.Menu, BoneOptions):
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    type: typing.Any

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

class VIEW3D_MT_bone_options_enable(fakebpy.types.Menu, BoneOptions):
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    type: typing.Any

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

class VIEW3D_MT_bone_options_toggle(fakebpy.types.Menu, BoneOptions):
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    type: typing.Any

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

def draw_curve(self_, _context): ...
def draw_gpencil_layer_active(context, layout): ...
def draw_gpencil_material_active(context, layout): ...
