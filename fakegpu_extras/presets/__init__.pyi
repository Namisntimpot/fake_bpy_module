import typing
import collections.abc
import typing_extensions
import fakegpu.types
import fakemathutils

def draw_circle_2d(
    position: collections.abc.Sequence[float] | fakemathutils.Vector,
    color,
    radius: float,
    *,
    segments: int | None = None,
):
    """Draw a circle.

        :param position: Position where the circle will be drawn.
        :type position: collections.abc.Sequence[float] | fakemathutils.Vector
        :param color: Color of the circle. To use transparency GL_BLEND has to be enabled.
        :param radius: Radius of the circle.
        :type radius: float
        :param segments: How many segments will be used to draw the circle.
    Higher values give better results but the drawing will take longer.
    If None or not specified, an automatic value will be calculated.
        :type segments: int | None
    """

def draw_texture_2d(
    texture: fakegpu.types.GPUTexture,
    position: collections.abc.Sequence[float] | fakemathutils.Vector,
    width: float,
    height: float,
):
    """Draw a 2d texture.

        :param texture: GPUTexture to draw (e.g. fakegpu.texture.from_image(image) for `fakebpy.types.Image`).
        :type texture: fakegpu.types.GPUTexture
        :param position: Position of the lower left corner.
        :type position: collections.abc.Sequence[float] | fakemathutils.Vector
        :param width: Width of the image when drawn (not necessarily
    the original width of the texture).
        :type width: float
        :param height: Height of the image when drawn.
        :type height: float
    """
