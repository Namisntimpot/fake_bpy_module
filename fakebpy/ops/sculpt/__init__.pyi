import typing
import collections.abc
import typing_extensions
import fakebpy.types
import fakemathutils

def brush_stroke(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    stroke: fakebpy.types.bpy_prop_collection[fakebpy.types.OperatorStrokeElement]
    | None = None,
    mode: typing.Literal["NORMAL", "INVERT", "SMOOTH"] | None = "NORMAL",
    ignore_background_click: bool | None = False,
):
    """Sculpt a stroke into the geometry

        :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param stroke: Stroke
        :type stroke: fakebpy.types.bpy_prop_collection[fakebpy.types.OperatorStrokeElement] | None
        :param mode: Stroke Mode, Action taken when a paint stroke is made

    NORMAL
    Regular -- Apply brush normally.

    INVERT
    Invert -- Invert action of brush for duration of stroke.

    SMOOTH
    Smooth -- Switch brush to smooth mode for duration of stroke.
        :type mode: typing.Literal['NORMAL','INVERT','SMOOTH'] | None
        :param ignore_background_click: Ignore Background Click, Clicks on the background do not start the stroke
        :type ignore_background_click: bool | None
    """

def cloth_filter(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    start_mouse: collections.abc.Iterable[int] | None = (0, 0),
    area_normal_radius: float | None = 0.25,
    strength: float | None = 1.0,
    iteration_count: int | None = 1,
    event_history: fakebpy.types.bpy_prop_collection[fakebpy.types.OperatorStrokeElement]
    | None = None,
    type: typing.Literal["GRAVITY", "INFLATE", "EXPAND", "PINCH", "SCALE"]
    | None = "GRAVITY",
    force_axis: set[typing.Literal["X", "Y", "Z"]] | None = {"X", "Y", "Z"},
    orientation: typing.Literal["LOCAL", "WORLD", "VIEW"] | None = "LOCAL",
    cloth_mass: float | None = 1.0,
    cloth_damping: float | None = 0.0,
    use_face_sets: bool | None = False,
    use_collisions: bool | None = False,
):
    """Applies a cloth simulation deformation to the entire mesh

        :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param start_mouse: Starting Mouse
        :type start_mouse: collections.abc.Iterable[int] | None
        :param area_normal_radius: Normal Radius, Radius used for calculating area normal on initial click,in percentage of brush radius
        :type area_normal_radius: float | None
        :param strength: Strength, Filter strength
        :type strength: float | None
        :param iteration_count: Repeat, How many times to repeat the filter
        :type iteration_count: int | None
        :type event_history: fakebpy.types.bpy_prop_collection[fakebpy.types.OperatorStrokeElement] | None
        :param type: Filter Type, Operation that is going to be applied to the mesh

    GRAVITY
    Gravity -- Applies gravity to the simulation.

    INFLATE
    Inflate -- Inflates the cloth.

    EXPAND
    Expand -- Expands the cloth's dimensions.

    PINCH
    Pinch -- Pulls the cloth to the cursor's start position.

    SCALE
    Scale -- Scales the mesh as a soft body using the origin of the object as scale.
        :type type: typing.Literal['GRAVITY','INFLATE','EXPAND','PINCH','SCALE'] | None
        :param force_axis: Force Axis, Apply the force in the selected axis

    X
    X -- Apply force in the X axis.

    Y
    Y -- Apply force in the Y axis.

    Z
    Z -- Apply force in the Z axis.
        :type force_axis: set[typing.Literal['X','Y','Z']] | None
        :param orientation: Orientation, Orientation of the axis to limit the filter force

    LOCAL
    Local -- Use the local axis to limit the force and set the gravity direction.

    WORLD
    World -- Use the global axis to limit the force and set the gravity direction.

    VIEW
    View -- Use the view axis to limit the force and set the gravity direction.
        :type orientation: typing.Literal['LOCAL','WORLD','VIEW'] | None
        :param cloth_mass: Cloth Mass, Mass of each simulation particle
        :type cloth_mass: float | None
        :param cloth_damping: Cloth Damping, How much the applied forces are propagated through the cloth
        :type cloth_damping: float | None
        :param use_face_sets: Use Face Sets, Apply the filter only to the Face Set under the cursor
        :type use_face_sets: bool | None
        :param use_collisions: Use Collisions, Collide with other collider objects in the scene
        :type use_collisions: bool | None
    """

def color_filter(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    start_mouse: collections.abc.Iterable[int] | None = (0, 0),
    area_normal_radius: float | None = 0.25,
    strength: float | None = 1.0,
    iteration_count: int | None = 1,
    event_history: fakebpy.types.bpy_prop_collection[fakebpy.types.OperatorStrokeElement]
    | None = None,
    type: typing.Literal[
        "FILL",
        "HUE",
        "SATURATION",
        "VALUE",
        "BRIGHTNESS",
        "CONTRAST",
        "SMOOTH",
        "RED",
        "GREEN",
        "BLUE",
    ]
    | None = "FILL",
    fill_color: collections.abc.Sequence[float] | fakemathutils.Color | None = (
        1.0,
        1.0,
        1.0,
    ),
):
    """Applies a filter to modify the active color attribute

        :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param start_mouse: Starting Mouse
        :type start_mouse: collections.abc.Iterable[int] | None
        :param area_normal_radius: Normal Radius, Radius used for calculating area normal on initial click,in percentage of brush radius
        :type area_normal_radius: float | None
        :param strength: Strength, Filter strength
        :type strength: float | None
        :param iteration_count: Repeat, How many times to repeat the filter
        :type iteration_count: int | None
        :type event_history: fakebpy.types.bpy_prop_collection[fakebpy.types.OperatorStrokeElement] | None
        :param type: Filter Type

    FILL
    Fill -- Fill with a specific color.

    HUE
    Hue -- Change hue.

    SATURATION
    Saturation -- Change saturation.

    VALUE
    Value -- Change value.

    BRIGHTNESS
    Brightness -- Change brightness.

    CONTRAST
    Contrast -- Change contrast.

    SMOOTH
    Smooth -- Smooth colors.

    RED
    Red -- Change red channel.

    GREEN
    Green -- Change green channel.

    BLUE
    Blue -- Change blue channel.
        :type type: typing.Literal['FILL','HUE','SATURATION','VALUE','BRIGHTNESS','CONTRAST','SMOOTH','RED','GREEN','BLUE'] | None
        :param fill_color: Fill Color
        :type fill_color: collections.abc.Sequence[float] | fakemathutils.Color | None
    """

def detail_flood_fill(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Flood fill the mesh with the selected detail setting

    :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def dynamic_topology_toggle(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Dynamic topology alters the mesh topology while sculpting

    :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def dyntopo_detail_size_edit(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Modify the detail size of dyntopo interactively

    :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def expand(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    target: typing.Literal["MASK", "FACE_SETS", "COLOR"] | None = "MASK",
    falloff_type: typing.Literal[
        "GEODESIC",
        "TOPOLOGY",
        "TOPOLOGY_DIAGONALS",
        "NORMALS",
        "SPHERICAL",
        "BOUNDARY_TOPOLOGY",
        "BOUNDARY_FACE_SET",
        "ACTIVE_FACE_SET",
    ]
    | None = "GEODESIC",
    invert: bool | None = False,
    use_mask_preserve: bool | None = False,
    use_falloff_gradient: bool | None = False,
    use_modify_active: bool | None = False,
    use_reposition_pivot: bool | None = True,
    max_geodesic_move_preview: int | None = 10000,
    use_auto_mask: bool | None = False,
    normal_falloff_smooth: int | None = 2,
):
    """Generic sculpt expand operator

    :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param target: Data Target, Data that is going to be modified in the expand operation
    :type target: typing.Literal['MASK','FACE_SETS','COLOR'] | None
    :param falloff_type: Falloff Type, Initial falloff of the expand operation
    :type falloff_type: typing.Literal['GEODESIC','TOPOLOGY','TOPOLOGY_DIAGONALS','NORMALS','SPHERICAL','BOUNDARY_TOPOLOGY','BOUNDARY_FACE_SET','ACTIVE_FACE_SET'] | None
    :param invert: Invert, Invert the expand active elements
    :type invert: bool | None
    :param use_mask_preserve: Preserve Previous, Preserve the previous state of the target data
    :type use_mask_preserve: bool | None
    :param use_falloff_gradient: Falloff Gradient, Expand Using a linear falloff
    :type use_falloff_gradient: bool | None
    :param use_modify_active: Modify Active, Modify the active Face Set instead of creating a new one
    :type use_modify_active: bool | None
    :param use_reposition_pivot: Reposition Pivot, Reposition the sculpt transform pivot to the boundary of the expand active area
    :type use_reposition_pivot: bool | None
    :param max_geodesic_move_preview: Max Vertex Count for Geodesic Move Preview, Maximum number of vertices in the mesh for using geodesic falloff when moving the origin of expand. If the total number of vertices is greater than this value, the falloff will be set to spherical when moving
    :type max_geodesic_move_preview: int | None
    :param use_auto_mask: Auto Create, Fill in mask if nothing is already masked
    :type use_auto_mask: bool | None
    :param normal_falloff_smooth: Normal Smooth, Blurring steps for normal falloff
    :type normal_falloff_smooth: int | None
    """

def face_set_box_gesture(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
    use_front_faces_only: bool | None = False,
):
    """Add a face set in a rectangle defined by the cursor

    :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param xmin: X Min
    :type xmin: int | None
    :param xmax: X Max
    :type xmax: int | None
    :param ymin: Y Min
    :type ymin: int | None
    :param ymax: Y Max
    :type ymax: int | None
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool | None
    :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
    :type use_front_faces_only: bool | None
    """

def face_set_change_visibility(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: typing.Literal["TOGGLE", "SHOW_ACTIVE", "HIDE_ACTIVE"] | None = "TOGGLE",
):
    """Change the visibility of the Face Sets of the sculpt

        :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode

    TOGGLE
    Toggle Visibility -- Hide all Face Sets except for the active one.

    SHOW_ACTIVE
    Show Active Face Set -- Show Active Face Set.

    HIDE_ACTIVE
    Hide Active Face Sets -- Hide Active Face Sets.
        :type mode: typing.Literal['TOGGLE','SHOW_ACTIVE','HIDE_ACTIVE'] | None
    """

def face_set_edit(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    active_face_set: int | None = 1,
    mode: typing.Literal[
        "GROW", "SHRINK", "DELETE_GEOMETRY", "FAIR_POSITIONS", "FAIR_TANGENCY"
    ]
    | None = "GROW",
    strength: float | None = 1.0,
    modify_hidden: bool | None = False,
):
    """Edits the current active Face Set

        :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param active_face_set: Active Face Set
        :type active_face_set: int | None
        :param mode: Mode

    GROW
    Grow Face Set -- Grows the Face Sets boundary by one face based on mesh topology.

    SHRINK
    Shrink Face Set -- Shrinks the Face Sets boundary by one face based on mesh topology.

    DELETE_GEOMETRY
    Delete Geometry -- Deletes the faces that are assigned to the Face Set.

    FAIR_POSITIONS
    Fair Positions -- Creates a smooth as possible geometry patch from the Face Set minimizing changes in vertex positions.

    FAIR_TANGENCY
    Fair Tangency -- Creates a smooth as possible geometry patch from the Face Set minimizing changes in vertex tangents.
        :type mode: typing.Literal['GROW','SHRINK','DELETE_GEOMETRY','FAIR_POSITIONS','FAIR_TANGENCY'] | None
        :param strength: Strength
        :type strength: float | None
        :param modify_hidden: Modify Hidden, Apply the edit operation to hidden geometry
        :type modify_hidden: bool | None
    """

def face_set_lasso_gesture(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    path: fakebpy.types.bpy_prop_collection[fakebpy.types.OperatorMousePath] | None = None,
    use_front_faces_only: bool | None = False,
):
    """Add a face set in a shape defined by the cursor

    :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param path: Path
    :type path: fakebpy.types.bpy_prop_collection[fakebpy.types.OperatorMousePath] | None
    :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
    :type use_front_faces_only: bool | None
    """

def face_set_line_gesture(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    xstart: int | None = 0,
    xend: int | None = 0,
    ystart: int | None = 0,
    yend: int | None = 0,
    flip: bool | None = False,
    cursor: int | None = 5,
    use_front_faces_only: bool | None = False,
    use_limit_to_segment: bool | None = False,
):
    """Add a face set to one side of a line defined by the cursor

    :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param xstart: X Start
    :type xstart: int | None
    :param xend: X End
    :type xend: int | None
    :param ystart: Y Start
    :type ystart: int | None
    :param yend: Y End
    :type yend: int | None
    :param flip: Flip
    :type flip: bool | None
    :param cursor: Cursor, Mouse cursor style to use during the modal operator
    :type cursor: int | None
    :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
    :type use_front_faces_only: bool | None
    :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
    :type use_limit_to_segment: bool | None
    """

def face_set_polyline_gesture(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    path: fakebpy.types.bpy_prop_collection[fakebpy.types.OperatorMousePath] | None = None,
    use_front_faces_only: bool | None = False,
):
    """Add a face set in a shape defined by the cursor

    :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param path: Path
    :type path: fakebpy.types.bpy_prop_collection[fakebpy.types.OperatorMousePath] | None
    :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
    :type use_front_faces_only: bool | None
    """

def face_sets_create(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: typing.Literal["MASKED", "VISIBLE", "ALL", "SELECTION"] | None = "MASKED",
):
    """Create a new Face Set

        :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode

    MASKED
    Face Set from Masked -- Create a new Face Set from the masked faces.

    VISIBLE
    Face Set from Visible -- Create a new Face Set from the visible vertices.

    ALL
    Face Set Full Mesh -- Create an unique Face Set with all faces in the sculpt.

    SELECTION
    Face Set from Edit Mode Selection -- Create an Face Set corresponding to the Edit Mode face selection.
        :type mode: typing.Literal['MASKED','VISIBLE','ALL','SELECTION'] | None
    """

def face_sets_init(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: typing.Literal[
        "LOOSE_PARTS",
        "MATERIALS",
        "NORMALS",
        "UV_SEAMS",
        "CREASES",
        "BEVEL_WEIGHT",
        "SHARP_EDGES",
        "FACE_SET_BOUNDARIES",
    ]
    | None = "LOOSE_PARTS",
    threshold: float | None = 0.5,
):
    """Initializes all Face Sets in the mesh

        :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode

    LOOSE_PARTS
    Face Sets from Loose Parts -- Create a Face Set per loose part in the mesh.

    MATERIALS
    Face Sets from Material Slots -- Create a Face Set per Material Slot.

    NORMALS
    Face Sets from Mesh Normals -- Create Face Sets for Faces that have similar normal.

    UV_SEAMS
    Face Sets from UV Seams -- Create Face Sets using UV Seams as boundaries.

    CREASES
    Face Sets from Edge Creases -- Create Face Sets using Edge Creases as boundaries.

    BEVEL_WEIGHT
    Face Sets from Bevel Weight -- Create Face Sets using Bevel Weights as boundaries.

    SHARP_EDGES
    Face Sets from Sharp Edges -- Create Face Sets using Sharp Edges as boundaries.

    FACE_SET_BOUNDARIES
    Face Sets from Face Set Boundaries -- Create a Face Set per isolated Face Set.
        :type mode: typing.Literal['LOOSE_PARTS','MATERIALS','NORMALS','UV_SEAMS','CREASES','BEVEL_WEIGHT','SHARP_EDGES','FACE_SET_BOUNDARIES'] | None
        :param threshold: Threshold, Minimum value to consider a certain attribute a boundary when creating the Face Sets
        :type threshold: float | None
    """

def face_sets_randomize_colors(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Generates a new set of random colors to render the Face Sets in the viewport

    :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def mask_by_color(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    contiguous: bool | None = False,
    invert: bool | None = False,
    preserve_previous_mask: bool | None = False,
    threshold: float | None = 0.35,
):
    """Creates a mask based on the active color attribute

    :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param contiguous: Contiguous, Mask only contiguous color areas
    :type contiguous: bool | None
    :param invert: Invert, Invert the generated mask
    :type invert: bool | None
    :param preserve_previous_mask: Preserve Previous Mask, Preserve the previous mask and add or subtract the new one generated by the colors
    :type preserve_previous_mask: bool | None
    :param threshold: Threshold, How much changes in color affect the mask generation
    :type threshold: float | None
    """

def mask_filter(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filter_type: typing.Literal[
        "SMOOTH", "SHARPEN", "GROW", "SHRINK", "CONTRAST_INCREASE", "CONTRAST_DECREASE"
    ]
    | None = "SMOOTH",
    iterations: int | None = 1,
    auto_iteration_count: bool | None = True,
):
    """Applies a filter to modify the current mask

    :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filter_type: Type, Filter that is going to be applied to the mask
    :type filter_type: typing.Literal['SMOOTH','SHARPEN','GROW','SHRINK','CONTRAST_INCREASE','CONTRAST_DECREASE'] | None
    :param iterations: Iterations, Number of times that the filter is going to be applied
    :type iterations: int | None
    :param auto_iteration_count: Auto Iteration Count, Use an automatic number of iterations based on the number of vertices of the sculpt
    :type auto_iteration_count: bool | None
    """

def mask_from_cavity(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mix_mode: typing.Literal["MIX", "MULTIPLY", "DIVIDE", "ADD", "SUBTRACT"]
    | None = "MIX",
    mix_factor: float | None = 1.0,
    settings_source: typing.Literal["OPERATOR", "BRUSH", "SCENE"] | None = "OPERATOR",
    factor: float | None = 0.5,
    blur_steps: int | None = 2,
    use_curve: bool | None = False,
    invert: bool | None = False,
):
    """Creates a mask based on the curvature of the surface

        :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mix_mode: Mode, Mix mode
        :type mix_mode: typing.Literal['MIX','MULTIPLY','DIVIDE','ADD','SUBTRACT'] | None
        :param mix_factor: Mix Factor
        :type mix_factor: float | None
        :param settings_source: Settings, Use settings from here

    OPERATOR
    Operator -- Use settings from operator properties.

    BRUSH
    Brush -- Use settings from brush.

    SCENE
    Scene -- Use settings from scene.
        :type settings_source: typing.Literal['OPERATOR','BRUSH','SCENE'] | None
        :param factor: Factor, The contrast of the cavity mask
        :type factor: float | None
        :param blur_steps: Blur, The number of times the cavity mask is blurred
        :type blur_steps: int | None
        :param use_curve: Custom Curve
        :type use_curve: bool | None
        :param invert: Cavity (Inverted)
        :type invert: bool | None
    """

def mask_init(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: typing.Literal[
        "RANDOM_PER_VERTEX", "RANDOM_PER_FACE_SET", "RANDOM_PER_LOOSE_PART"
    ]
    | None = "RANDOM_PER_VERTEX",
):
    """Creates a new mask for the entire mesh

    :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: typing.Literal['RANDOM_PER_VERTEX','RANDOM_PER_FACE_SET','RANDOM_PER_LOOSE_PART'] | None
    """

def mesh_filter(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    start_mouse: collections.abc.Iterable[int] | None = (0, 0),
    area_normal_radius: float | None = 0.25,
    strength: float | None = 1.0,
    iteration_count: int | None = 1,
    event_history: fakebpy.types.bpy_prop_collection[fakebpy.types.OperatorStrokeElement]
    | None = None,
    type: typing.Literal[
        "SMOOTH",
        "SCALE",
        "INFLATE",
        "SPHERE",
        "RANDOM",
        "RELAX",
        "RELAX_FACE_SETS",
        "SURFACE_SMOOTH",
        "SHARPEN",
        "ENHANCE_DETAILS",
        "ERASE_DISCPLACEMENT",
    ]
    | None = "INFLATE",
    deform_axis: set[typing.Literal["X", "Y", "Z"]] | None = {"X", "Y", "Z"},
    orientation: typing.Literal["LOCAL", "WORLD", "VIEW"] | None = "LOCAL",
    surface_smooth_shape_preservation: float | None = 0.5,
    surface_smooth_current_vertex: float | None = 0.5,
    sharpen_smooth_ratio: float | None = 0.35,
    sharpen_intensify_detail_strength: float | None = 0.0,
    sharpen_curvature_smooth_iterations: int | None = 0,
):
    """Applies a filter to modify the current mesh

        :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param start_mouse: Starting Mouse
        :type start_mouse: collections.abc.Iterable[int] | None
        :param area_normal_radius: Normal Radius, Radius used for calculating area normal on initial click,in percentage of brush radius
        :type area_normal_radius: float | None
        :param strength: Strength, Filter strength
        :type strength: float | None
        :param iteration_count: Repeat, How many times to repeat the filter
        :type iteration_count: int | None
        :type event_history: fakebpy.types.bpy_prop_collection[fakebpy.types.OperatorStrokeElement] | None
        :param type: Filter Type, Operation that is going to be applied to the mesh

    SMOOTH
    Smooth -- Smooth mesh.

    SCALE
    Scale -- Scale mesh.

    INFLATE
    Inflate -- Inflate mesh.

    SPHERE
    Sphere -- Morph into sphere.

    RANDOM
    Random -- Randomize vertex positions.

    RELAX
    Relax -- Relax mesh.

    RELAX_FACE_SETS
    Relax Face Sets -- Smooth the edges of all the Face Sets.

    SURFACE_SMOOTH
    Surface Smooth -- Smooth the surface of the mesh, preserving the volume.

    SHARPEN
    Sharpen -- Sharpen the cavities of the mesh.

    ENHANCE_DETAILS
    Enhance Details -- Enhance the high frequency surface detail.

    ERASE_DISCPLACEMENT
    Erase Displacement -- Deletes the displacement of the Multires Modifier.
        :type type: typing.Literal['SMOOTH','SCALE','INFLATE','SPHERE','RANDOM','RELAX','RELAX_FACE_SETS','SURFACE_SMOOTH','SHARPEN','ENHANCE_DETAILS','ERASE_DISCPLACEMENT'] | None
        :param deform_axis: Deform Axis, Apply the deformation in the selected axis

    X
    X -- Deform in the X axis.

    Y
    Y -- Deform in the Y axis.

    Z
    Z -- Deform in the Z axis.
        :type deform_axis: set[typing.Literal['X','Y','Z']] | None
        :param orientation: Orientation, Orientation of the axis to limit the filter displacement

    LOCAL
    Local -- Use the local axis to limit the displacement.

    WORLD
    World -- Use the global axis to limit the displacement.

    VIEW
    View -- Use the view axis to limit the displacement.
        :type orientation: typing.Literal['LOCAL','WORLD','VIEW'] | None
        :param surface_smooth_shape_preservation: Shape Preservation, How much of the original shape is preserved when smoothing
        :type surface_smooth_shape_preservation: float | None
        :param surface_smooth_current_vertex: Per Vertex Displacement, How much the position of each individual vertex influences the final result
        :type surface_smooth_current_vertex: float | None
        :param sharpen_smooth_ratio: Smooth Ratio, How much smoothing is applied to polished surfaces
        :type sharpen_smooth_ratio: float | None
        :param sharpen_intensify_detail_strength: Intensify Details, How much creases and valleys are intensified
        :type sharpen_intensify_detail_strength: float | None
        :param sharpen_curvature_smooth_iterations: Curvature Smooth Iterations, How much smooth the resulting shape is, ignoring high frequency details
        :type sharpen_curvature_smooth_iterations: int | None
    """

def optimize(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Recalculate the sculpt BVH to improve performance

    :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def project_line_gesture(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    xstart: int | None = 0,
    xend: int | None = 0,
    ystart: int | None = 0,
    yend: int | None = 0,
    flip: bool | None = False,
    cursor: int | None = 5,
    use_front_faces_only: bool | None = False,
    use_limit_to_segment: bool | None = False,
):
    """Project the geometry onto a plane defined by a line

    :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param xstart: X Start
    :type xstart: int | None
    :param xend: X End
    :type xend: int | None
    :param ystart: Y Start
    :type ystart: int | None
    :param yend: Y End
    :type yend: int | None
    :param flip: Flip
    :type flip: bool | None
    :param cursor: Cursor, Mouse cursor style to use during the modal operator
    :type cursor: int | None
    :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
    :type use_front_faces_only: bool | None
    :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
    :type use_limit_to_segment: bool | None
    """

def sample_color(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Sample the vertex color of the active vertex

    :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def sample_detail_size(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    location: collections.abc.Iterable[int] | None = (0, 0),
    mode: typing.Literal["DYNTOPO", "VOXEL"] | None = "DYNTOPO",
):
    """Sample the mesh detail on clicked point

        :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param location: Location, Screen coordinates of sampling
        :type location: collections.abc.Iterable[int] | None
        :param mode: Detail Mode, Target sculpting workflow that is going to use the sampled size

    DYNTOPO
    Dyntopo -- Sample dyntopo detail.

    VOXEL
    Voxel -- Sample mesh voxel size.
        :type mode: typing.Literal['DYNTOPO','VOXEL'] | None
    """

def sculptmode_toggle(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Toggle sculpt mode in 3D view

    :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def set_persistent_base(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Reset the copy of the mesh that is being sculpted on

    :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def set_pivot_position(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: typing.Literal["ORIGIN", "UNMASKED", "BORDER", "ACTIVE", "SURFACE"]
    | None = "UNMASKED",
    mouse_x: float | None = 0.0,
    mouse_y: float | None = 0.0,
):
    """Sets the sculpt transform pivot position

        :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode

    ORIGIN
    Origin -- Sets the pivot to the origin of the sculpt.

    UNMASKED
    Unmasked -- Sets the pivot position to the average position of the unmasked vertices.

    BORDER
    Mask Border -- Sets the pivot position to the center of the border of the mask.

    ACTIVE
    Active Vertex -- Sets the pivot position to the active vertex position.

    SURFACE
    Surface -- Sets the pivot position to the surface under the cursor.
        :type mode: typing.Literal['ORIGIN','UNMASKED','BORDER','ACTIVE','SURFACE'] | None
        :param mouse_x: Mouse Position X, Position of the mouse used for "Surface" mode
        :type mouse_x: float | None
        :param mouse_y: Mouse Position Y, Position of the mouse used for "Surface" mode
        :type mouse_y: float | None
    """

def symmetrize(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    merge_tolerance: float | None = 0.0005,
):
    """Symmetrize the topology modifications

    :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param merge_tolerance: Merge Distance, Distance within which symmetrical vertices are merged
    :type merge_tolerance: float | None
    """

def trim_box_gesture(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
    use_front_faces_only: bool | None = False,
    location: collections.abc.Iterable[int] | None = (0, 0),
    trim_mode: typing.Literal["DIFFERENCE", "UNION", "JOIN"] | None = "DIFFERENCE",
    use_cursor_depth: bool | None = False,
    trim_orientation: typing.Literal["VIEW", "SURFACE"] | None = "VIEW",
    trim_extrude_mode: typing.Literal["PROJECT", "FIXED"] | None = "FIXED",
    trim_solver: typing.Literal["EXACT", "FAST"] | None = "FAST",
):
    """Execute a boolean operation on the mesh and a rectangle defined by the cursor

        :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param xmin: X Min
        :type xmin: int | None
        :param xmax: X Max
        :type xmax: int | None
        :param ymin: Y Min
        :type ymin: int | None
        :param ymax: Y Max
        :type ymax: int | None
        :param wait_for_input: Wait for Input
        :type wait_for_input: bool | None
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
        :type use_front_faces_only: bool | None
        :param location: Location, Mouse location
        :type location: collections.abc.Iterable[int] | None
        :param trim_mode: Trim Mode

    DIFFERENCE
    Difference -- Use a difference boolean operation.

    UNION
    Union -- Use a union boolean operation.

    JOIN
    Join -- Join the new mesh as separate geometry, without performing any boolean operation.
        :type trim_mode: typing.Literal['DIFFERENCE','UNION','JOIN'] | None
        :param use_cursor_depth: Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape
        :type use_cursor_depth: bool | None
        :param trim_orientation: Shape Orientation

    VIEW
    View -- Use the view to orientate the trimming shape.

    SURFACE
    Surface -- Use the surface normal to orientate the trimming shape.
        :type trim_orientation: typing.Literal['VIEW','SURFACE'] | None
        :param trim_extrude_mode: Extrude Mode

    PROJECT
    Project -- Align trim geometry with the perspective of the current view for a tapered shape.

    FIXED
    Fixed -- Align trim geometry orthogonally for a shape with 90 degree angles.
        :type trim_extrude_mode: typing.Literal['PROJECT','FIXED'] | None
        :param trim_solver: Solver

    EXACT
    Exact -- Use the exact boolean solver.

    FAST
    Fast -- Use the fast float boolean solver.
        :type trim_solver: typing.Literal['EXACT','FAST'] | None
    """

def trim_lasso_gesture(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    path: fakebpy.types.bpy_prop_collection[fakebpy.types.OperatorMousePath] | None = None,
    use_front_faces_only: bool | None = False,
    location: collections.abc.Iterable[int] | None = (0, 0),
    trim_mode: typing.Literal["DIFFERENCE", "UNION", "JOIN"] | None = "DIFFERENCE",
    use_cursor_depth: bool | None = False,
    trim_orientation: typing.Literal["VIEW", "SURFACE"] | None = "VIEW",
    trim_extrude_mode: typing.Literal["PROJECT", "FIXED"] | None = "FIXED",
    trim_solver: typing.Literal["EXACT", "FAST"] | None = "FAST",
):
    """Execute a boolean operation on the mesh and a shape defined by the cursor

        :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param path: Path
        :type path: fakebpy.types.bpy_prop_collection[fakebpy.types.OperatorMousePath] | None
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
        :type use_front_faces_only: bool | None
        :param location: Location, Mouse location
        :type location: collections.abc.Iterable[int] | None
        :param trim_mode: Trim Mode

    DIFFERENCE
    Difference -- Use a difference boolean operation.

    UNION
    Union -- Use a union boolean operation.

    JOIN
    Join -- Join the new mesh as separate geometry, without performing any boolean operation.
        :type trim_mode: typing.Literal['DIFFERENCE','UNION','JOIN'] | None
        :param use_cursor_depth: Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape
        :type use_cursor_depth: bool | None
        :param trim_orientation: Shape Orientation

    VIEW
    View -- Use the view to orientate the trimming shape.

    SURFACE
    Surface -- Use the surface normal to orientate the trimming shape.
        :type trim_orientation: typing.Literal['VIEW','SURFACE'] | None
        :param trim_extrude_mode: Extrude Mode

    PROJECT
    Project -- Align trim geometry with the perspective of the current view for a tapered shape.

    FIXED
    Fixed -- Align trim geometry orthogonally for a shape with 90 degree angles.
        :type trim_extrude_mode: typing.Literal['PROJECT','FIXED'] | None
        :param trim_solver: Solver

    EXACT
    Exact -- Use the exact boolean solver.

    FAST
    Fast -- Use the fast float boolean solver.
        :type trim_solver: typing.Literal['EXACT','FAST'] | None
    """

def trim_line_gesture(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    xstart: int | None = 0,
    xend: int | None = 0,
    ystart: int | None = 0,
    yend: int | None = 0,
    flip: bool | None = False,
    cursor: int | None = 5,
    use_front_faces_only: bool | None = False,
    use_limit_to_segment: bool | None = False,
    location: collections.abc.Iterable[int] | None = (0, 0),
    trim_mode: typing.Literal["DIFFERENCE", "UNION", "JOIN"] | None = "DIFFERENCE",
    use_cursor_depth: bool | None = False,
    trim_orientation: typing.Literal["VIEW", "SURFACE"] | None = "VIEW",
    trim_extrude_mode: typing.Literal["PROJECT", "FIXED"] | None = "FIXED",
    trim_solver: typing.Literal["EXACT", "FAST"] | None = "FAST",
):
    """Remove a portion of the mesh on one side of a line

        :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param xstart: X Start
        :type xstart: int | None
        :param xend: X End
        :type xend: int | None
        :param ystart: Y Start
        :type ystart: int | None
        :param yend: Y End
        :type yend: int | None
        :param flip: Flip
        :type flip: bool | None
        :param cursor: Cursor, Mouse cursor style to use during the modal operator
        :type cursor: int | None
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
        :type use_front_faces_only: bool | None
        :param use_limit_to_segment: Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
        :type use_limit_to_segment: bool | None
        :param location: Location, Mouse location
        :type location: collections.abc.Iterable[int] | None
        :param trim_mode: Trim Mode

    DIFFERENCE
    Difference -- Use a difference boolean operation.

    UNION
    Union -- Use a union boolean operation.

    JOIN
    Join -- Join the new mesh as separate geometry, without performing any boolean operation.
        :type trim_mode: typing.Literal['DIFFERENCE','UNION','JOIN'] | None
        :param use_cursor_depth: Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape
        :type use_cursor_depth: bool | None
        :param trim_orientation: Shape Orientation

    VIEW
    View -- Use the view to orientate the trimming shape.

    SURFACE
    Surface -- Use the surface normal to orientate the trimming shape.
        :type trim_orientation: typing.Literal['VIEW','SURFACE'] | None
        :param trim_extrude_mode: Extrude Mode

    PROJECT
    Project -- Align trim geometry with the perspective of the current view for a tapered shape.

    FIXED
    Fixed -- Align trim geometry orthogonally for a shape with 90 degree angles.
        :type trim_extrude_mode: typing.Literal['PROJECT','FIXED'] | None
        :param trim_solver: Solver

    EXACT
    Exact -- Use the exact boolean solver.

    FAST
    Fast -- Use the fast float boolean solver.
        :type trim_solver: typing.Literal['EXACT','FAST'] | None
    """

def trim_polyline_gesture(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    path: fakebpy.types.bpy_prop_collection[fakebpy.types.OperatorMousePath] | None = None,
    use_front_faces_only: bool | None = False,
    location: collections.abc.Iterable[int] | None = (0, 0),
    trim_mode: typing.Literal["DIFFERENCE", "UNION", "JOIN"] | None = "DIFFERENCE",
    use_cursor_depth: bool | None = False,
    trim_orientation: typing.Literal["VIEW", "SURFACE"] | None = "VIEW",
    trim_extrude_mode: typing.Literal["PROJECT", "FIXED"] | None = "FIXED",
    trim_solver: typing.Literal["EXACT", "FAST"] | None = "FAST",
):
    """Execute a boolean operation on the mesh and a polygonal shape defined by the cursor

        :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param path: Path
        :type path: fakebpy.types.bpy_prop_collection[fakebpy.types.OperatorMousePath] | None
        :param use_front_faces_only: Front Faces Only, Affect only faces facing towards the view
        :type use_front_faces_only: bool | None
        :param location: Location, Mouse location
        :type location: collections.abc.Iterable[int] | None
        :param trim_mode: Trim Mode

    DIFFERENCE
    Difference -- Use a difference boolean operation.

    UNION
    Union -- Use a union boolean operation.

    JOIN
    Join -- Join the new mesh as separate geometry, without performing any boolean operation.
        :type trim_mode: typing.Literal['DIFFERENCE','UNION','JOIN'] | None
        :param use_cursor_depth: Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape
        :type use_cursor_depth: bool | None
        :param trim_orientation: Shape Orientation

    VIEW
    View -- Use the view to orientate the trimming shape.

    SURFACE
    Surface -- Use the surface normal to orientate the trimming shape.
        :type trim_orientation: typing.Literal['VIEW','SURFACE'] | None
        :param trim_extrude_mode: Extrude Mode

    PROJECT
    Project -- Align trim geometry with the perspective of the current view for a tapered shape.

    FIXED
    Fixed -- Align trim geometry orthogonally for a shape with 90 degree angles.
        :type trim_extrude_mode: typing.Literal['PROJECT','FIXED'] | None
        :param trim_solver: Solver

    EXACT
    Exact -- Use the exact boolean solver.

    FAST
    Fast -- Use the fast float boolean solver.
        :type trim_solver: typing.Literal['EXACT','FAST'] | None
    """

def uv_sculpt_grab(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_invert: bool | None = False,
):
    """Grab UVs

    :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_invert: Invert, Invert action for the duration of the stroke
    :type use_invert: bool | None
    """

def uv_sculpt_pinch(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_invert: bool | None = False,
):
    """Pinch UVs

    :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_invert: Invert, Invert action for the duration of the stroke
    :type use_invert: bool | None
    """

def uv_sculpt_relax(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_invert: bool | None = False,
    relax_method: typing.Literal["LAPLACIAN", "HC", "COTAN"] | None = "COTAN",
):
    """Relax UVs

        :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param use_invert: Invert, Invert action for the duration of the stroke
        :type use_invert: bool | None
        :param relax_method: Relax Method, Algorithm used for UV relaxation

    LAPLACIAN
    Laplacian -- Use Laplacian method for relaxation.

    HC
    HC -- Use HC method for relaxation.

    COTAN
    Geometry -- Use Geometry (cotangent) relaxation, making UVs follow the underlying 3D geometry.
        :type relax_method: typing.Literal['LAPLACIAN','HC','COTAN'] | None
    """