import typing
import collections.abc
import typing_extensions
import fakebpy.types

class AnnotationDataPanel:
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any

    def draw(self, context):
        """

        :param context:
        """

    def draw_header(self, context):
        """

        :param context:
        """

    def draw_layers(self, context, layout, gpd):
        """

        :param context:
        :param layout:
        :param gpd:
        """

class AnnotationDrawingToolsPanel:
    bl_category: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any

    def draw(self, context):
        """

        :param context:
        """

class AnnotationOnionSkin:
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any

    def draw(self, context):
        """

        :param context:
        """

    def draw_header(self, context):
        """

        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class GPENCIL_MT_cleanup(fakebpy.types.Menu):
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

class GPENCIL_MT_gpencil_draw_delete(fakebpy.types.Menu):
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

class GPENCIL_MT_layer_active(fakebpy.types.Menu):
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

class GPENCIL_MT_layer_mask_menu(fakebpy.types.Menu):
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

class GPENCIL_MT_material_active(fakebpy.types.Menu):
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

class GPENCIL_MT_move_to_layer(fakebpy.types.Menu):
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

class GPENCIL_MT_snap(fakebpy.types.Menu):
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

class GPENCIL_MT_snap_pie(fakebpy.types.Menu):
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

class GPENCIL_UL_annotation_layer(fakebpy.types.UIList):
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
        _data,
        item,
        icon,
        _active_data,
        _active_propname,
        _index,
    ):
        """

        :param _context:
        :param layout:
        :param _data:
        :param item:
        :param icon:
        :param _active_data:
        :param _active_propname:
        :param _index:
        """

class GPENCIL_UL_layer(fakebpy.types.UIList):
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
        _data,
        item,
        icon,
        _active_data,
        _active_propname,
        _index,
    ):
        """

        :param _context:
        :param layout:
        :param _data:
        :param item:
        :param icon:
        :param _active_data:
        :param _active_propname:
        :param _index:
        """

class GPENCIL_UL_masks(fakebpy.types.UIList):
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
        _data,
        item,
        icon,
        _active_data,
        _active_propname,
        _index,
    ):
        """

        :param _context:
        :param layout:
        :param _data:
        :param item:
        :param icon:
        :param _active_data:
        :param _active_propname:
        :param _index:
        """

class GREASE_PENCIL_MT_layer_active(fakebpy.types.Menu):
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

class GREASE_PENCIL_MT_move_to_layer(fakebpy.types.Menu):
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

class GREASE_PENCIL_MT_snap(fakebpy.types.Menu):
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

class GREASE_PENCIL_MT_snap_pie(fakebpy.types.Menu):
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

class GreasePencilBrushFalloff:
    bl_label: typing.Any
    bl_options: typing.Any

    def draw(self, context):
        """

        :param context:
        """

class GreasePencilDisplayPanel:
    bl_label: typing.Any
    bl_options: typing.Any

    def draw(self, context):
        """

        :param context:
        """

    def draw_header(self, context):
        """

        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class GreasePencilFlipTintColors(fakebpy.types.Operator):
    """Switch tint colors"""

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

    def execute(self, context):
        """

        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class GreasePencilLayerAdjustmentsPanel:
    def draw(self, context):
        """

        :param context:
        """

class GreasePencilLayerDisplayPanel:
    def draw(self, context):
        """

        :param context:
        """

class GreasePencilLayerMasksPanel:
    def draw(self, context):
        """

        :param context:
        """

    def draw_header(self, context):
        """

        :param context:
        """

class GreasePencilLayerRelationsPanel:
    def draw(self, context):
        """

        :param context:
        """

class GreasePencilLayerTransformPanel:
    def draw(self, context):
        """

        :param context:
        """

class GreasePencilMaterialsPanel:
    def draw(self, context):
        """

        :param context:
        """

class GreasePencilSculptAdvancedPanel:
    def draw(self, context):
        """

        :param context:
        """

class GreasePencilSimplifyPanel:
    def draw(self, context):
        """

        :param context:
        """

    def draw_header(self, context):
        """

        :param context:
        """

class GreasePencilVertexcolorPanel:
    def draw(self, context):
        """

        :param context:
        """
