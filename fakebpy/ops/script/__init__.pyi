import typing
import collections.abc
import typing_extensions
import fakebpy.types

def execute_preset(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
    menu_idname: str = "",
):
    """Load a preset

    :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: filepath
    :type filepath: str
    :param menu_idname: Menu ID Name, ID name of the menu this was called from
    :type menu_idname: str
    """

def python_file_run(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
):
    """Run Python file

    :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: Path
    :type filepath: str
    """

def reload(
    override_context: fakebpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Reload scripts

    :type override_context: fakebpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """
