"""
This module provides utils for textures.

"""

import typing
import collections.abc
import typing_extensions
import fakebpy.types
import fakegpu.types

def from_image(image: fakebpy.types.Image) -> fakegpu.types.GPUTexture:
    """Get GPUTexture corresponding to an Image datablock. The GPUTexture memory is shared with Blender.
    Note: Colors read from the texture will be in scene linear color space and have premultiplied or straight alpha matching the image alpha mode.

        :param image: The Image datablock.
        :type image: fakebpy.types.Image
        :return: The GPUTexture used by the image.
        :rtype: fakegpu.types.GPUTexture
    """
