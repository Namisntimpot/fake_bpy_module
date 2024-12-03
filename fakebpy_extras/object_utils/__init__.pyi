import typing
import collections.abc
import typing_extensions
import fakebpy.types
import fakemathutils

class AddObjectHelper:
    def align_update_callback(self, _context):
        """

        :param _context:
        """

def add_object_align_init(
    context: fakebpy.types.Context | None, operator: fakebpy.types.Operator
) -> fakemathutils.Matrix:
    """Return a matrix using the operator settings and view context.

    :param context: The context to use.
    :type context: fakebpy.types.Context | None
    :param operator: The operator, checked for location and rotation properties.
    :type operator: fakebpy.types.Operator
    :return: the matrix from the context and settings.
    :rtype: fakemathutils.Matrix
    """

def object_add_grid_scale(context):
    """Return scale which should be applied on object
    data to align it to grid scale

    """

def object_add_grid_scale_apply_operator(operator, context):
    """Scale an operators distance values by the grid size."""

def object_data_add(
    context: fakebpy.types.Context | None,
    obdata,
    operator: fakebpy.types.Operator | None = None,
    name: str | None = None,
) -> fakebpy.types.Object:
    """Add an object using the view context and preference to initialize the
    location, rotation and layer.

        :param context: The context to use.
        :type context: fakebpy.types.Context | None
        :param obdata: the data used for the new object.
        :param operator: The operator, checked for location and rotation properties.
        :type operator: fakebpy.types.Operator | None
        :param name: Optional name
        :type name: str | None
        :return: the newly created object in the scene.
        :rtype: fakebpy.types.Object
    """

def object_report_if_active_shape_key_is_locked(
    obj: fakebpy.types.Object, operator: fakebpy.types.Operator
):
    """Checks if the active shape key of the specified object is locked, and reports an error if so.If the object has no shape keys, there is nothing to lock, and the function returns False.

    :param obj: Object to check.
    :type obj: fakebpy.types.Object
    :param operator: Currently running operator to report the error through. Use None to suppress emitting the message.
    :type operator: fakebpy.types.Operator
    :return: True if the shape key was locked.
    """

def world_to_camera_view(
    scene: fakebpy.types.Scene,
    obj: fakebpy.types.Object,
    coord: collections.abc.Sequence[float] | fakemathutils.Vector,
) -> fakemathutils.Vector:
    """Returns the camera space coords for a 3d point.
    (also known as: normalized device coordinates - NDC).Where (0, 0) is the bottom left and (1, 1)
    is the top right of the camera frame.
    values outside 0-1 are also supported.
    A negative 'z' value means the point is behind the camera.Takes shift-x/y, lens angle and sensor size into account
    as well as perspective/ortho projections.

        :param scene: Scene to use for frame size.
        :type scene: fakebpy.types.Scene
        :param obj: Camera object.
        :type obj: fakebpy.types.Object
        :param coord: World space location.
        :type coord: collections.abc.Sequence[float] | fakemathutils.Vector
        :return: a vector where X and Y map to the view plane and
    Z is the depth on the view axis.
        :rtype: fakemathutils.Vector
    """
