import typing
import collections.abc
import typing_extensions
import fakebpy.types
import fakebpy.typing

def bake(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Bake dynamic paint image sequence surface

    :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def output_toggle(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    output: typing.Literal["A", "B"] | None = "A",
):
    """Add or remove Dynamic Paint output data layer

    :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param output: Output Toggle
    :type output: typing.Literal['A','B'] | None
    """

def surface_slot_add(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add a new Dynamic Paint surface slot

    :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def surface_slot_remove(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove the selected surface slot

    :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def type_toggle(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: fakebpy.typing.PropDynamicpaintTypeItems | None = "CANVAS",
):
    """Toggle whether given type is active or not

    :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: fakebpy.typing.PropDynamicpaintTypeItems | None
    """