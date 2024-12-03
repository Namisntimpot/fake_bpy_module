"""
This module provides access to Blender's image manipulation API.

It provides access to image buffers outside of Blender's
fakebpy.types.Image data-block context.

fakeimbuf.types.rst

:maxdepth: 1
:caption: Submodules

"""

import typing
import collections.abc
import typing_extensions
import fakeimbuf.types

from . import types as types

def load(filepath: bytes | str) -> fakeimbuf.types.fakeimbuf:
    """Load an image from a file.

    :param filepath: the filepath of the image.
    :type filepath: bytes | str
    :return: the newly loaded image.
    :rtype: fakeimbuf.types.fakeimbuf
    """

def new(size) -> fakeimbuf.types.fakeimbuf:
    """Load a new image.

    :param size: The size of the image in pixels.
    :return: the newly loaded image.
    :rtype: fakeimbuf.types.fakeimbuf
    """

def write(image: fakeimbuf.types.fakeimbuf, filepath: bytes | str = image.filepath):
    """Write an image.

    :param image: the image to write.
    :type image: fakeimbuf.types.fakeimbuf
    :param filepath: Optional filepath of the image (fallback to the images file path).
    :type filepath: bytes | str
    """
