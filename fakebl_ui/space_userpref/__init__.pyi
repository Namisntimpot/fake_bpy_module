import typing
import collections.abc
import typing_extensions
import fakebl_ui.utils
import fakebpy.types

class AddOnPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

class AnimationPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

class CenterAlignMixIn:
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    def draw(self, context):
        """

        :param context:
        """

class EditingPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

class ExperimentalPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any
    url_prefix: typing.Any

    @classmethod
    def poll(cls, _context):
        """

        :param _context:
        """

class ExtensionsPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

class FilePathsPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

class InputPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

class InterfacePanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

class KeymapPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

class NavigationPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

class PreferenceThemeSpacePanel:
    ui_delimiters: typing.Any

    def draw(self, context):
        """

        :param context:
        """

    def draw_header(self, _context):
        """

        :param _context:
        """

class PreferenceThemeWidgetColorPanel:
    bl_parent_id: typing.Any

    def draw(self, context):
        """

        :param context:
        """

class PreferenceThemeWidgetShadePanel:
    def draw(self, context):
        """

        :param context:
        """

    def draw_header(self, context):
        """

        :param context:
        """

class SaveLoadPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

class StudioLightPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

class StudioLightPanelMixin:
    def draw(self, context):
        """

        :param context:
        """

    def draw_light_list(self, layout, lights):
        """

        :param layout:
        :param lights:
        """

    def draw_studio_light(self, layout, studio_light):
        """

        :param layout:
        :param studio_light:
        """

    def get_error_message(self): ...

class SystemPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

class ThemeGenericClassGenerator:
    @staticmethod
    def generate_panel_classes_for_wcols(): ...
    @staticmethod
    def generate_panel_classes_from_theme_areas(): ...
    @staticmethod
    def generate_theme_area_child_panel_classes(
        parent_id, rna_type, theme_area, datapath
    ):
        """

        :param parent_id:
        :param rna_type:
        :param theme_area:
        :param datapath:
        """

class ThemePanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

class USERPREF_HT_header(fakebpy.types.Header):
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
    def draw_buttons(layout, context):
        """

        :param layout:
        :param context:
        """

class USERPREF_MT_editor_menus(fakebpy.types.Menu):
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

class USERPREF_MT_extensions_active_repo(fakebpy.types.Menu):
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

class USERPREF_MT_extensions_active_repo_remove(fakebpy.types.Menu):
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

class USERPREF_MT_interface_theme_presets(fakebpy.types.Menu):
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    preset_operator: typing.Any
    preset_subdir: typing.Any
    preset_type: typing.Any
    preset_xml_map: typing.Any
    preset_xml_secure_types: typing.Any

    def bl_rna_get_subclass(self) -> fakebpy.types.Struct:
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
    def post_cb(context, filepath):
        """

        :param context:
        :param filepath:
        """

    @staticmethod
    def reset_cb(_context, _filepath):
        """

        :param _context:
        :param _filepath:
        """

class USERPREF_MT_keyconfigs(fakebpy.types.Menu):
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    preset_operator: typing.Any
    preset_subdir: typing.Any

    def bl_rna_get_subclass(self) -> fakebpy.types.Struct:
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

class USERPREF_MT_save_load(fakebpy.types.Menu):
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

class USERPREF_MT_view(fakebpy.types.Menu):
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

class USERPREF_PT_addons(AddOnPanel, fakebpy.types.Panel):
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

    @staticmethod
    def draw_addon_preferences(layout, context, addon_preferences):
        """

        :param layout:
        :param context:
        :param addon_preferences:
        """

    @staticmethod
    def draw_error(layout, message):
        """

        :param layout:
        :param message:
        """

    @staticmethod
    def is_user_addon(mod, user_addon_paths):
        """

        :param mod:
        :param user_addon_paths:
        """

class USERPREF_PT_addons_filter(fakebpy.types.Panel):
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

class USERPREF_PT_animation_fcurves(CenterAlignMixIn, AnimationPanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_animation_keyframes(
    CenterAlignMixIn, AnimationPanel, fakebpy.types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_animation_timeline(CenterAlignMixIn, AnimationPanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_edit_annotations(CenterAlignMixIn, EditingPanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_edit_cursor(CenterAlignMixIn, EditingPanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_edit_gpencil(CenterAlignMixIn, EditingPanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_edit_misc(CenterAlignMixIn, EditingPanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_edit_node_editor(CenterAlignMixIn, EditingPanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_edit_objects(EditingPanel, fakebpy.types.Panel):
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

class USERPREF_PT_edit_objects_duplicate_data(
    CenterAlignMixIn, EditingPanel, fakebpy.types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_edit_objects_new(CenterAlignMixIn, EditingPanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_edit_sequence_editor(CenterAlignMixIn, EditingPanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_edit_text_editor(CenterAlignMixIn, EditingPanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_edit_weight_paint(CenterAlignMixIn, EditingPanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_experimental_debugging(ExperimentalPanel, fakebpy.types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any
    url_prefix: typing.Any

    def bl_rna_get_subclass(self) -> fakebpy.types.Struct:
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
    def poll(cls, _context):
        """

        :param _context:
        """

class USERPREF_PT_experimental_new_features(ExperimentalPanel, fakebpy.types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any
    url_prefix: typing.Any

    def bl_rna_get_subclass(self) -> fakebpy.types.Struct:
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

class USERPREF_PT_experimental_prototypes(ExperimentalPanel, fakebpy.types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any
    url_prefix: typing.Any

    def bl_rna_get_subclass(self) -> fakebpy.types.Struct:
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

class USERPREF_PT_extensions(ExtensionsPanel, fakebpy.types.Panel):
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

class USERPREF_PT_extensions_repos(fakebpy.types.Panel):
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

    def draw(self, context):
        """

        :param context:
        """

class USERPREF_PT_file_paths_applications(FilePathsPanel, fakebpy.types.Panel):
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

class USERPREF_PT_file_paths_asset_libraries(FilePathsPanel, fakebpy.types.Panel):
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

class USERPREF_PT_file_paths_data(FilePathsPanel, fakebpy.types.Panel):
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

class USERPREF_PT_file_paths_development(FilePathsPanel, fakebpy.types.Panel):
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

class USERPREF_PT_file_paths_render(FilePathsPanel, fakebpy.types.Panel):
    bl_context: typing.Any
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

class USERPREF_PT_file_paths_script_directories(FilePathsPanel, fakebpy.types.Panel):
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

class USERPREF_PT_input_keyboard(CenterAlignMixIn, InputPanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_input_mouse(CenterAlignMixIn, InputPanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_input_ndof(CenterAlignMixIn, InputPanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class USERPREF_PT_input_tablet(CenterAlignMixIn, InputPanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_input_touchpad(CenterAlignMixIn, InputPanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class USERPREF_PT_interface_display(CenterAlignMixIn, InterfacePanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_interface_editors(CenterAlignMixIn, InterfacePanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_interface_menus(InterfacePanel, fakebpy.types.Panel):
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

class USERPREF_PT_interface_menus_mouse_over(
    CenterAlignMixIn, InterfacePanel, fakebpy.types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

    def draw_header(self, context):
        """

        :param context:
        """

class USERPREF_PT_interface_menus_pie(
    CenterAlignMixIn, InterfacePanel, fakebpy.types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_interface_statusbar(
    CenterAlignMixIn, InterfacePanel, fakebpy.types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_interface_temporary_windows(
    CenterAlignMixIn, InterfacePanel, fakebpy.types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_interface_text(CenterAlignMixIn, InterfacePanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_interface_translation(
    CenterAlignMixIn, InterfacePanel, fakebpy.types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

    @classmethod
    def poll(cls, _context):
        """

        :param _context:
        """

class USERPREF_PT_keymap(KeymapPanel, fakebpy.types.Panel):
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

class USERPREF_PT_navigation_bar(fakebpy.types.Panel):
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

class USERPREF_PT_navigation_fly_walk(
    CenterAlignMixIn, NavigationPanel, fakebpy.types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_navigation_fly_walk_gravity(
    CenterAlignMixIn, NavigationPanel, fakebpy.types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
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

class USERPREF_PT_navigation_fly_walk_navigation(
    CenterAlignMixIn, NavigationPanel, fakebpy.types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class USERPREF_PT_navigation_orbit(CenterAlignMixIn, NavigationPanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_navigation_zoom(CenterAlignMixIn, NavigationPanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_ndof_settings(fakebpy.types.Panel):
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

    @staticmethod
    def draw_settings(layout, props, show_3dview_settings=True):
        """

        :param layout:
        :param props:
        :param show_3dview_settings:
        """

class USERPREF_PT_save_preferences(fakebpy.types.Panel):
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

class USERPREF_PT_saveload_autorun(FilePathsPanel, fakebpy.types.Panel):
    bl_context: typing.Any
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

class USERPREF_PT_saveload_blend(CenterAlignMixIn, SaveLoadPanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_saveload_file_browser(
    CenterAlignMixIn, SaveLoadPanel, fakebpy.types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_studiolight_light_editor(StudioLightPanel, fakebpy.types.Panel):
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

    @staticmethod
    def opengl_light_buttons(layout, light):
        """

        :param layout:
        :param light:
        """

class USERPREF_PT_studiolight_lights(
    StudioLightPanelMixin, StudioLightPanel, fakebpy.types.Panel
):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any
    sl_type: typing.Any

    def bl_rna_get_subclass(self) -> fakebpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: fakebpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def draw_header_preset(self, _context):
        """

        :param _context:
        """

    def get_error_message(self): ...

class USERPREF_PT_studiolight_matcaps(
    StudioLightPanelMixin, StudioLightPanel, fakebpy.types.Panel
):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any
    sl_type: typing.Any

    def bl_rna_get_subclass(self) -> fakebpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: fakebpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def draw_header_preset(self, _context):
        """

        :param _context:
        """

    def get_error_message(self): ...

class USERPREF_PT_studiolight_world(
    StudioLightPanelMixin, StudioLightPanel, fakebpy.types.Panel
):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any
    sl_type: typing.Any

    def bl_rna_get_subclass(self) -> fakebpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: fakebpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def draw_header_preset(self, _context):
        """

        :param _context:
        """

    def get_error_message(self): ...

class USERPREF_PT_system_cycles_devices(CenterAlignMixIn, SystemPanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_system_memory(CenterAlignMixIn, SystemPanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_system_network(CenterAlignMixIn, SystemPanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_system_os_settings(CenterAlignMixIn, SystemPanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

    @classmethod
    def poll(cls, _context):
        """

        :param _context:
        """

class USERPREF_PT_system_sound(CenterAlignMixIn, SystemPanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_system_video_sequencer(
    CenterAlignMixIn, SystemPanel, fakebpy.types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_text_editor(FilePathsPanel, fakebpy.types.Panel):
    bl_context: typing.Any
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

    def draw_header_preset(self, _context):
        """

        :param _context:
        """

class USERPREF_PT_text_editor_presets(fakebl_ui.utils.PresetPanel, fakebpy.types.Panel):
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any
    preset_add_operator: typing.Any
    preset_operator: typing.Any
    preset_subdir: typing.Any

    def bl_rna_get_subclass(self) -> fakebpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: fakebpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class USERPREF_PT_theme(ThemePanel, fakebpy.types.Panel):
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

class USERPREF_PT_theme_bone_color_sets(CenterAlignMixIn, ThemePanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

    def draw_header(self, _context):
        """

        :param _context:
        """

class USERPREF_PT_theme_collection_colors(
    CenterAlignMixIn, ThemePanel, fakebpy.types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

    def draw_header(self, _context):
        """

        :param _context:
        """

class USERPREF_PT_theme_interface_gizmos(CenterAlignMixIn, ThemePanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_theme_interface_icons(CenterAlignMixIn, ThemePanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_theme_interface_state(CenterAlignMixIn, ThemePanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_theme_interface_styles(CenterAlignMixIn, ThemePanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_theme_interface_transparent_checker(
    CenterAlignMixIn, ThemePanel, fakebpy.types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_theme_strip_colors(CenterAlignMixIn, ThemePanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

    def draw_header(self, _context):
        """

        :param _context:
        """

class USERPREF_PT_theme_text_style(CenterAlignMixIn, ThemePanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

    def draw_header(self, _context):
        """

        :param _context:
        """

class USERPREF_PT_theme_user_interface(CenterAlignMixIn, ThemePanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_header(self, _context):
        """

        :param _context:
        """

class USERPREF_PT_viewport_display(CenterAlignMixIn, ViewportPanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_viewport_quality(CenterAlignMixIn, ViewportPanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_viewport_selection(CenterAlignMixIn, ViewportPanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_PT_viewport_subdivision(
    CenterAlignMixIn, ViewportPanel, fakebpy.types.Panel
):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class USERPREF_PT_viewport_textures(CenterAlignMixIn, ViewportPanel, fakebpy.types.Panel):
    """Base class for panels to center align contents with some horizontal margin.
    Deriving classes need to implement a draw_centered(context, layout) function.
    """

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

    def draw_centered(self, context, layout):
        """

        :param context:
        :param layout:
        """

class USERPREF_UL_asset_libraries(fakebpy.types.UIList):
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

class USERPREF_UL_extension_repos(fakebpy.types.UIList):
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

    def filter_items(self, _context, data, propname):
        """

        :param _context:
        :param data:
        :param propname:
        """

class ViewportPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any